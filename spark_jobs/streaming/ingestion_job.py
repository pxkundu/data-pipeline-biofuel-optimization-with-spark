from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col
from pyspark.sql.types import StructType, StructField, StringType, FloatType

# Schema for sensor data
schema = StructType([
    StructField("sensor_id", StringType(), True),
    StructField("temperature", FloatType(), True),
    StructField("pressure", FloatType(), True),
    StructField("timestamp", StringType(), True)
])

if __name__ == "__main__":
    spark = SparkSession.builder \
        .appName("RealTimeDataIngestion") \
        .master("local[*]") \
        .getOrCreate()

    # Read from Kafka
    kafka_stream = spark.readStream \
        .format("kafka") \
        .option("kafka.bootstrap.servers", "localhost:9092") \
        .option("subscribe", "biofuel-sensor-data") \
        .load()

    # Parse Kafka data
    sensor_data = kafka_stream.selectExpr("CAST(value AS STRING)") \
        .select(from_json(col("value"), schema).alias("data")) \
        .select("data.*")

    # Write to Parquet
    query = sensor_data.writeStream \
        .outputMode("append") \
        .format("parquet") \
        .option("path", "data/processed/streaming") \
        .option("checkpointLocation", "data/processed/checkpoints/ingestion") \
        .start()

    query.awaitTermination()
