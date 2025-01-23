from kafka import KafkaProducer
import json
import random
import time

producer = KafkaProducer(
    bootstrap_servers="localhost:9092",
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

# Simulate sensor data
def generate_sensor_data():
    return {
        "sensor_id": random.randint(1, 100),
        "temperature": round(random.uniform(15, 100), 2),
        "pressure": round(random.uniform(50, 200), 2),
        "timestamp": time.time()
    }

if __name__ == "__main__":
    print("Starting data ingestion...")
    try:
        while True:
            data = generate_sensor_data()
            producer.send("biofuel-sensor-data", value=data)
            print(f"Sent: {data}")
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nData ingestion stopped.")
