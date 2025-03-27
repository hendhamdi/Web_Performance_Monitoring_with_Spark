from pyspark.sql import SparkSession
from pyspark.sql.functions import col, regexp_extract, avg, count, window
import time

# Création de la session Spark
spark = SparkSession.builder \
    .appName("WebPerformanceMonitoring") \
    .master("local[*]") \
    .getOrCreate()

# Chemin du fichier de logs
LOG_FILE_PATH = "../data/access.log"

# Définition du schéma des logs
log_schema = spark.read.text(LOG_FILE_PATH)

# Extraction des informations avec des expressions régulières
log_df = log_schema.select(
    regexp_extract('value', r'(\d+\.\d+\.\d+\.\d+)', 1).alias("ip"),
    regexp_extract('value', r'\[(.*?)\]', 1).alias("timestamp"),
    regexp_extract('value', r'GET (.*?) HTTP', 1).alias("url"),
    regexp_extract('value', r'HTTP/1.1" (\d+)', 1).cast("integer").alias("status"),
    regexp_extract('value', r'(\d+)$', 1).cast("integer").alias("size")
)

# Calcul du nombre de requêtes et du temps de réponse moyen
metrics = log_df.groupBy(window(col("timestamp"), "1 minute")).agg(
    count("*").alias("total_requests"),
    avg("status").alias("average_status")
)

# Affichage des résultats en continu
query = metrics.writeStream \
    .outputMode("complete") \
    .format("console") \
    .start()

# Maintien du script actif
query.awaitTermination()
