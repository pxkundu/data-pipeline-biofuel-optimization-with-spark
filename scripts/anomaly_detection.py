from pyspark.sql import SparkSession
from pyspark.sql.functions import col

if __name__ == "__main__":
    spark = SparkSession.builder \
        .appName("AnomalyDetection") \
        .master("local[*]") \
        .getOrCreate()

    # Load processed data
    data = spark.read.parquet("data/processed/batch")

    # Define thresholds
    temp_min, temp_max = 20, 80
    pressure_min, pressure_max = 50, 150

    # Detect anomalies
    anomalies = data.filter(
        (col("temperature") < temp_min) | (col("temperature") > temp_max) |
        (col("pressure") < pressure_min) | (col("pressure") > pressure_max)
    )

    # Save anomalies
    anomalies.write \
        .mode("overwrite") \
        .parquet("data/processed/anomalies")

    print("Anomalies detected and saved.")
