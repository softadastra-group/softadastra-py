from softadastra.ressources.products import Product

# CRUD simple
p1 = Product.create(name="T-shirt", price=5000)
p2 = Product.create(name="Jeans", price=8000)

# Liste avec pagination
products = Product.all(limit=10)
for p in products:
    print(p.name, p.price)

# Update
p1.update(price=5500)

# Delete
p2.delete()

# Bulk CRUD
bulk_data = {
    "items": [
        {"name": "Hat", "price": 2000},
        {"name": "Socks", "price": 500}
    ],
    "bulk": True
}
Product.create(**bulk_data)
