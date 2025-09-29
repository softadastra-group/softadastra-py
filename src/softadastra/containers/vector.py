"""Implémentation d'un conteneur type Vector similaire à std::vector."""

from collections.abc import MutableSequence

class Vector(MutableSequence):
    """Container similaire a std::vector en c++"""

    def __init__(self, iterable=None):
        self._data = list(iterable) if iterable else []

    def __getitem__(self, index):
        return self._data[index]

    def __setitem__(self, index, value):
        self._data[index] = value

    def __len__(self):
        return len(self._data)
    
    def insert(self, index, value):
        self._data.insert(index, value)

        