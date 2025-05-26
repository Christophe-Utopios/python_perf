from abc import ABC, abstractmethod
from collections import deque
from copy import deepcopy

# 1. POO avancée : Services
class Service(ABC):
    def __init__(self, nom, base_prix):
        self.nom = nom
        self.base_prix = base_prix

    @abstractmethod
    def calculer_prix(self):
        pass

class Serveur(Service):
    def __init__(self, nom, base_prix, cpu, ram):
        super().__init__(nom, base_prix)
        self.cpu = cpu
        self.ram = ram

    def calculer_prix(self):
        return self.base_prix + (self.cpu * 10) + (self.ram * 5)

class Cloud(Service):
    def __init__(self, nom, base_prix, stockage):
        super().__init__(nom, base_prix)
        self.stockage = stockage

    def calculer_prix(self):
        return self.base_prix + (self.stockage * 2)

class Domaine(Service):
    def __init__(self, nom, base_prix, extension):
        super().__init__(nom, base_prix)
        self.extension = extension

    def calculer_prix(self):
        ext_tarif = {'.com': 10, '.fr': 8, '.io': 20}
        return self.base_prix + ext_tarif.get(self.extension, 5)

# 2. Clients et commandes
clients = {}  # {client_id: [liste_commandes]}
file_commandes = deque()

# 3. Traitement des commandes avec args et kwargs
def passer_commande(client_id, *services, **options):
    if client_id not in clients:
        clients[client_id] = []

    commande = {
        "services": services,
        "urgent": options.get("urgent", False),
        "remise": options.get("remise", 0),
    }
    file_commandes.append((client_id, commande))

# Exemple d’utilisation
s1 = Serveur("Serveur Web", 100, cpu=4, ram=16)
s2 = Cloud("Stockage S3", 50, stockage=500)
s3 = Domaine("mon-site", 15, extension=".io")
passer_commande("client_001", s1, s2, s3, urgent=True, remise=10)

# 4. Facturation avec map, filter
def traiter_commandes():
    historique = []

    while file_commandes:
        client_id, commande = file_commandes.popleft()
        services = commande["services"]
        total = sum(map(lambda s: s.calculer_prix(), services))
        total_apres_remise = total - commande["remise"]
        if commande["urgent"]:
            total_apres_remise *= 1.2

        facture = {
            "total": total_apres_remise,
            "services": [s.nom for s in services],
            # "etat_initial": deepcopy(commande)
        }

        clients[client_id].append(facture)
        historique.append(deepcopy(facture))

    return historique

historique_commandes = traiter_commandes()

# Filtrage des grosses factures
grosses_factures = list(filter(lambda f: f["total"] > 100, historique_commandes))

# Affichage final
for client_id, factures in clients.items():
    print(f"Client {client_id}")
    for facture in factures:
        print(f"  Services: {facture['services']}")
        print(f"  Total: {facture['total']}€")
        print()
