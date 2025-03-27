import os
import random
import time

# Chemin du dossier et fichier log
LOG_DIR = "data"
LOG_FILE = os.path.join(LOG_DIR, "access.log")

# Vérifier et créer le dossier si nécessaire
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

# Modèle de log
LOG_FORMAT = '{ip} - - [{timestamp}] "GET {url} HTTP/1.1" {status} {size}'

# Données aléatoires
URLS = ["/home", "/about", "/contact", "/products", "/cart"]
STATUS_CODES = [200, 200, 200, 500, 404]  # Simule des erreurs 500 et 404
IPS = ["192.168.1.1", "192.168.1.2", "192.168.1.3"]

def generate_log():
    """ Génère une ligne de log aléatoire """
    log = LOG_FORMAT.format(
        ip=random.choice(IPS),
        timestamp=time.strftime("%d/%b/%Y:%H:%M:%S +0000"),
        url=random.choice(URLS),
        status=random.choice(STATUS_CODES),
        size=random.randint(500, 5000)
    )
    return log

# Écriture des logs dans le fichier
if __name__ == "__main__":
    with open(LOG_FILE, "a") as f:
        while True:
            log_entry = generate_log()
            print(log_entry)  # Afficher dans la console
            f.write(log_entry + "\n")
            time.sleep(1)  # Un log par seconde
