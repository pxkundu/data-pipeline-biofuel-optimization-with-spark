#!/bin/bash
echo "Setting up Spark cluster..."

# Install dependencies
sudo apt update && sudo apt install -y openjdk-11-jdk scala wget

# Download and configure Spark
wget https://downloads.apache.org/spark/spark-3.3.0/spark-3.3.0-bin-hadoop3.tgz
tar xvf spark-3.3.0-bin-hadoop3.tgz
sudo mv spark-3.3.0-bin-hadoop3 /opt/spark

echo "export SPARK_HOME=/opt/spark" >> ~/.bashrc
echo "export PATH=$PATH:/opt/spark/bin:/opt/spark/sbin" >> ~/.bashrc
source ~/.bashrc

echo "Spark cluster setup complete."
