import sys

def total_size(o, seen=None):
    """Retourne la taille mémoire approximative d'un objet et de ses membres récursivement."""
    if seen is None:
        seen = set()

    obj_id = id(o)
    if obj_id in seen:
        return 0
    
    seen.add(obj_id)
    size = sys.getsizeof(o, default=0)

    if isinstance(o, dict):
        size += sum((total_size(k, seen) + total_size(v, seen)) for k, v in o.items())
    elif isinstance(o, (list, tuple, set, frozenset)):
        size += sum(total_size(i, seen) for i in o)

    return size
