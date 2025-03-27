import os

# Path configuration
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(BASE_DIR, "data", "access.log")
LOGS_PATH = os.path.join(BASE_DIR, "logs")

SPARK_APP_NAME = "WebPerformanceMonitoring"
SPARK_MASTER = "local[*]"  

ERROR_THRESHOLD = 10 
AVG_RESPONSE_TIME_THRESHOLD = 2.0  
