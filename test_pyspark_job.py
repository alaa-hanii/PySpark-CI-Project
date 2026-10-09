"""Unit tests for pyspark_job.clean_data."""

import pytest
from pyspark.sql import SparkSession
from pyspark.sql.types import (
    DoubleType,
    StringType,
    StructField,
    StructType,
)

from pyspark_job import clean_data

SCHEMA = StructType(
    [
        StructField("name", StringType(), True),
        StructField("amount", DoubleType(), True),
    ]
)


@pytest.fixture(scope="session")
def spark():
    """Create a local SparkSession shared by all tests."""
    session = (
        SparkSession.builder.master("local[1]")
        .appName("clean_data_tests")
        .config("spark.sql.shuffle.partitions", "1")
        .config("spark.ui.enabled", "false")
        .getOrCreate()
    )
    yield session
    session.stop()


def make_df(spark, rows):
    """Build a DataFrame with the (name, amount) test schema."""
    return spark.createDataFrame(rows, schema=SCHEMA)


def test_valid_records_are_kept(spark):
    df = make_df(spark, [("Alice", 100.0), ("Bob", 50.0)])

    result = clean_data(df)

    names = {row["name"] for row in result.collect()}
    assert result.count() == 2
    assert names == {"Alice", "Bob"}


def test_records_with_non_positive_amount_are_removed(spark):
    df = make_df(
        spark,
        [("Alice", 100.0), ("Zero", 0.0), ("Negative", -10.0)],
    )

    result = clean_data(df)

    names = {row["name"] for row in result.collect()}
    assert names == {"Alice"}


def test_records_with_null_name_are_removed(spark):
    df = make_df(spark, [("Alice", 100.0), (None, 75.0)])

    result = clean_data(df)

    rows = result.collect()
    assert len(rows) == 1
    assert rows[0]["name"] == "Alice"


def test_amount_with_tax_is_calculated_correctly(spark):
    df = make_df(spark, [("Alice", 100.0), ("Bob", 50.0)])

    result = clean_data(df)

    taxed = {row["name"]: row["amount_with_tax"] for row in result.collect()}
    assert taxed["Alice"] == pytest.approx(120.0)
    assert taxed["Bob"] == pytest.approx(60.0)