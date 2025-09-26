from .base_ressource import RessourceBase

class Product(RessourceBase):
    ressource_name = "products"

    def __init__(self, id=None, name = None, price = None):
        self.id = id
        self.name = name
        self.price = price