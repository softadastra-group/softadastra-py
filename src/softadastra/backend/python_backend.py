DB = {
    "products": []
}

def create(ressource, data):
    #Simule l'insertion
    data["id"] = len(DB[ressource]) + 1
    DB[ressource].append(data)
    return data

def list(ressource, limit=100, offset=0):
    return DB[ressource][offset:offset+limit]

def update(ressource, id, data):
    for item in DB[ressource]:
        if item["id"] == id:
            item.update(data)
            return item
    return ValueError("Not found")

def delete(ressource, id):
    for i, item in enumerate(DB[ressource]):
        if item["id"] == id:
            return DB[ressource].pop(i)
    raise ValueError("Not found")
    