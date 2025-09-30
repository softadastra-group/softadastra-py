"""Algorithmes de tri génériques pour séquences Python."""
from typing import Any,Callable

def bubble_sort(arr: list[Any],
                reverse: bool = False,
                key: Callable[[Any], Any] | None = None )-> list[Any]:
    """
    Sort a list the Bubble Sort algorithm.

    Bubble Sort repeatedly compares adjacent elements and swaps them if they are in the wrong order. The largest (or smallest, if reverse=True) element "bubbles" to its correct position after each pass.

    Args:
    arr (list[Any]): The list of elements to sort.
    reverse (bool, optional): If True, sorts in descending order. Defaults to False.
    Key (Callable[[Any], Any] | None = None, optional): A function to extract a comparison key from each element.

    Returns:
        list[Any]: A new sorted list. 
    """
    size = len(arr)
    arr = arr.copy() # Out-of-place to avoid modifying input
    key_func = key if key else lambda x: x

    for i in range(size - 1):
        swapped = False
        for j in range(size - i - 1):
            if (key_func(arr[j]) > key_func(arr[j + 1]) and not reverse) or \
               (key_func(arr[j]) < key_func(arr[j + 1]) and reverse):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

def insertion_sort(arr: list[Any], reverse: bool = False, key: Callable[[Any], Any] | None = None) -> list[Any]:
    """
    Sort a list using the Insertion Sort algorithm.

    Insertion Sort builds the sorted list one element at a time by repeatedly
    taking the next element and inserting it into its correct position in the
    already sorted part of the list.

    Args:
        arr (list[Any]): The list of elements to sort.
        reverse (bool, optional): If True, sorts in descending order. Defaults to False.
        key (Callable[[Any], Any] | None, optional): A function to extract a comparison key from each element.
            If None, elements are compared directly. Defaults to None.

    Returns:
        list[Any]: A new sorted list.
    """

    array_copy = arr.copy()  # Out-of-place to avoid modifying input
    key_func = key if key else lambda x: x
    size = len(array_copy)

    for current_index in range(1, size):
        current_value = array_copy[current_index]
        sorted_index = current_index - 1

        # Déplacer les éléments plus grands vers la droite
        while sorted_index >= 0 and (
            (key_func(array_copy[sorted_index]) > key_func(current_value) and not reverse) or
            (key_func(array_copy[sorted_index]) < key_func(current_value) and reverse)
        ):
            array_copy[sorted_index + 1] = array_copy[sorted_index]
            sorted_index -= 1

        array_copy[sorted_index + 1] = current_value  # Placer l'élément à la bonne position

    return array_copy
