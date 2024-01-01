from pyspark.sql import SparkSession
import psutil

def get_memory():
    #return int(psutil.virtual_memory().total * (10**9))
    return int(psutil.virtual_memory().total * (10**-9) * .6)

def launch_spark(driver_memory=get_memory()):
    print(f'Launching spark with {driver_memory} GB of RAM')
    spark = SparkSession \
        .builder \
        .appName("Python Spark SQL basic example") \
        .config("spark.some.config.option", f"{driver_memory}G") \
        .getOrCreate()
    return spark
