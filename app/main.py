from pyspark.sql import SparkSession
from pyspark.sql.functions import regexp_extract, col, avg, count

spark = SparkSession.builder.appName("WebLogAnalysis").getOrCreate()

log_pattern = r'(\S+) - - \[(.*?)\] "(\S+) (\S+) HTTP/1.1" (\d+) (\d+)'

import os

data_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../data/access.log"))

if not os.path.exists(data_path):
    raise FileNotFoundError(f" The {data_path} file cannot be found. Check its location.")

df = spark.read.text(data_path)

logs_df = df.select(
    regexp_extract("value", log_pattern, 1).alias("ip"),
    regexp_extract("value", log_pattern, 2).alias("timestamp"),
    regexp_extract("value", log_pattern, 3).alias("method"),
    regexp_extract("value", log_pattern, 4).alias("url"),
    regexp_extract("value", log_pattern, 5).cast("integer").alias("status"),
    regexp_extract("value", log_pattern, 6).cast("integer").alias("size")
)

# Calculation of metrics
print("🚀 Top 5 most visited pages")
logs_df.groupBy("url").count().orderBy(col("count").desc()).show(5)

print("📊 Average response time")
logs_df.select(avg("size").alias("Average response size")).show()

print("❌ Number of errors 500")
logs_df.filter(col("status") == 500).agg(count("*").alias("Total Errors 500")).show()


spark.stop()
