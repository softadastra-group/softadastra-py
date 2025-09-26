from softadastra.validation.validators import validate_fields
from softadastra.backend import python_backend, cpp_bindings

class RessourceBase:
    ressource_name = "base"

    @classmethod
    def create(cls, **kwargs):
        validate_fields(kwargs)

        # Choisir backend : C++ si buld ou operation lourde
        if kwargs.get("bulk") or kwargs.get("heavy"):
            result = cpp_bindings.create(cls.ressource_name, kwargs)

            # Gestion bulk : transformer chaque item en instance
            items = result.get("items", [])
            return [cls(**item) for item in items]
        else:
            result = python_backend.create(cls.ressource_name, kwargs)
            return cls(**result)

    @classmethod
    def all(cls, limit=100, offset=0):
        data = python_backend.list(cls.ressource_name, limit=limit, offset=offset)
        return [cls(**item) for item in data]

    def update(self, **kwargs):
        validate_fields(kwargs)
        result = python_backend.update(self.ressource_name, self.id, kwargs)
        for k, v in result.items():
            setattr(self, k, v)
        return self
    
    def delete(self):
        return python_backend.delete(self.ressource_name, self.id)