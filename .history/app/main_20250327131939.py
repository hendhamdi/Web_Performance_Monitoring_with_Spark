from pyspark.sql import SparkSession
from pyspark.sql.functions import regexp_extract, col, avg, count

# Initialisation de Spark
spark = SparkSession.builder.appName("WebLogAnalysis").getOrCreate()

# Définition du schéma des logs
log_pattern = r'(\S+) - - \[(.*?)\] "(\S+) (\S+) HTTP/1.1" (\d+) (\d+)'

# Chargement des logs
df = spark.read.text("../data/access.log")

# Extraction des données importantes
logs_df = df.select(
    regexp_extract("value", log_pattern, 1).alias("ip"),
    regexp_extract("value", log_pattern, 2).alias("timestamp"),
    regexp_extract("value", log_pattern, 3).alias("method"),
    regexp_extract("value", log_pattern, 4).alias("url"),
    regexp_extract("value", log_pattern, 5).cast("integer").alias("status"),
    regexp_extract("value", log_pattern, 6).cast("integer").alias("size")
)

# Calcul des métriques
print("🚀 Top 5 pages les plus visitées")
logs_df.groupBy("url").count().orderBy(col("count").desc()).show(5)

print("📊 Temps de réponse moyen")
logs_df.select(avg("size").alias("Taille moyenne des réponses")).show()

print("❌ Nombre d'erreurs 500")
logs_df.filter(col("status") == 500).agg(count("*").alias("Total Erreurs 500")).show()

# Arrêter Spark
spark.stop()
