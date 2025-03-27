import os

# Configuration des chemins
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(BASE_DIR, "data", "access.log")
LOGS_PATH = os.path.join(BASE_DIR, "logs")

# Paramètres Spark
SPARK_APP_NAME = "WebPerformanceMonitoring"
SPARK_MASTER = "local[*]"  # Exécuter Spark en mode local

# Seuils pour générer des alertes
ERROR_THRESHOLD = 10  # Nombre d'erreurs critiques avant alerte
AVG_RESPONSE_TIME_THRESHOLD = 2.0  # Temps de réponse moyen en secondes
