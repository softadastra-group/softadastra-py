import pytest
from typing import Any
from softadastra.algorithms.sorting import insertion_sort  

# 1. Tri simple (nombres)
def test_insertion_sort_simple():
    assert insertion_sort([4, 2, 5, 1, 3]) == [1, 2, 3, 4, 5]
    assert insertion_sort([4, 2, 5, 1, 3], reverse=True) == [5, 4, 3, 2, 1]

# 2. Tri avec key (par valeur absolue)
def test_insertion_sort_with_key():
    data = [-3, -1, 2, -2, 0]
    result = insertion_sort(data, key=abs)
    assert set(result) == set(data)
    assert all(abs(result[i]) <= abs(result[i+1]) for i in range(len(result)-1))


# 3. Liste vide
def test_insertion_sort_empty():
    assert insertion_sort([]) == []

# 4. Liste déjà triée
def test_insertion_sort_sorted_input():
    assert insertion_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

# 5. Liste avec doublons
def test_insertion_sort_duplicates():
    assert insertion_sort([3, 1, 2, 3, 1]) == [1, 1, 2, 3, 3]

# 6. Liste de dictionnaires avec key
def test_insertion_sort_dicts_with_key():
    data = [
        {"name": "Alice", "age": 30},
        {"name": "Bob", "age": 25},
        {"name": "Charlie", "age": 35},
    ]
    sorted_data = insertion_sort(data, key=lambda x: x["age"])
    assert [d["name"] for d in sorted_data] == ["Bob", "Alice", "Charlie"]

    sorted_data_desc = insertion_sort(data, reverse=True, key=lambda x: x["age"])
    assert [d["name"] for d in sorted_data_desc] == ["Charlie", "Alice", "Bob"]

# 7. Vérification de non-modification de la liste d'origine
def test_input_list_not_modified():
    original = [3,2,1]
    _ = insertion_sort(original)
    assert original == [3,2,1]
