import random
import time

# Modèle d’un log
LOG_FORMAT = '{ip} - - [{timestamp}] "GET {url} HTTP/1.1" {status} {size}'

# Liste de pages et adresses IP aléatoires
URLS = ["/home", "/about", "/contact", "/products", "/cart"]
STATUS_CODES = [200, 200, 200, 500, 404]  # Simuler des erreurs
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

# Générer des logs en boucle
if __name__ == "__main__":
    with open("../data/access.log", "a") as f:
        while True:
            log_entry = generate_log()
            print(log_entry)  # Afficher dans la console
            f.write(log_entry + "\n")
            time.sleep(1)  # Simuler un accès toutes les secondes
