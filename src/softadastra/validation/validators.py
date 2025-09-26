def validate_fields(data):
    if "name" in data and not isinstance(data["name"], str):
        raise ValueError("Field 'name' musb be a string")
    if "price" in data and not isinstance(data["price"], int):
        raise ValueError("Field 'price' musb be an integer")