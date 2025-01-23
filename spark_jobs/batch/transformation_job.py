from pyspark.sql import SparkSession

if __name__ == "__main__":
    spark = SparkSession.builder \
        .appName("BatchProcessing") \
        .master("local[*]") \
        .getOrCreate()

    # Read raw data
    raw_data = spark.read.parquet("data/processed/streaming")

    # Perform transformations
    processed_data = raw_data.withColumn("temperature_celsius", (raw_data.temperature - 32) * 5 / 9)

    # Save the transformed data
    processed_data.write \
        .mode("overwrite") \
        .parquet("data/processed/batch")
