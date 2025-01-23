from pyspark.sql import SparkSession
from pyspark.ml.regression import LinearRegression
from pyspark.ml.feature import VectorAssembler

if __name__ == "__main__":
    spark = SparkSession.builder \
        .appName("PredictiveMaintenance") \
        .master("local[*]") \
        .getOrCreate()

    # Load data
    data = spark.read.parquet("data/processed/batch")

    # Prepare data for ML model
    assembler = VectorAssembler(inputCols=["temperature", "pressure"], outputCol="features")
    training_data = assembler.transform(data).select("features", "sensor_id")

    # Train Linear Regression Model
    lr = LinearRegression(featuresCol="features", labelCol="sensor_id")
    model = lr.fit(training_data)

    print("Predictive Maintenance Model trained.")
