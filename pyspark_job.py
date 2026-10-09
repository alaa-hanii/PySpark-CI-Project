"""PySpark data-processing job.

Contains the `clean_data` transformation used to validate and enrich
transaction records.
"""

from pyspark.sql import DataFrame
from pyspark.sql import functions as F

TAX_RATE = 1.20  # 20% tax multiplier


def clean_data(df: DataFrame) -> DataFrame:
    """Clean a transactions DataFrame and add a tax-inclusive amount.

    Steps:
        1. Drop rows where `amount` is less than or equal to 0.
        2. Drop rows where `name` is NULL.
        3. Add `amount_with_tax` = `amount` * 1.20.

    Args:
        df: Input DataFrame with at least the columns `name` and `amount`.

    Returns:
        A new DataFrame with invalid rows removed and an extra
        `amount_with_tax` column.
    """
    return (
        df.filter(F.col("amount") > 0)
        .filter(F.col("name").isNotNull())
        .withColumn("amount_with_tax", F.col("amount") * TAX_RATE)
    )