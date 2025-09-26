def create(ressource, data):
    print(f"[C++] creating {len(data.get('items', [1]))} {ressource} entries")
    return data