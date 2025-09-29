"""
Softadastra – boîte à outils inspirée de la STL C++
pour l'écosystème Softadastra.
"""

from .core import types, errors
from .containers import vector, map
from .algorithms import sorting, searching

__all__ = [
    "types",
    "errors",
    "vector",
    "map",
    "sorting",
    "searching",
]
