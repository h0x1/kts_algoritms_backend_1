from typing import Any

__all__ = (
    'cartesian_product',
)


def cartesian_product(arr1: list[Any], arr2: list[Any]) -> list:
    newarr = []
    minLen = min(len(arr1),len(arr2))
    for i in range(0, minLen):
        for i2 in range(0, minLen):
            newarr.append((arr1[i],arr2[i2]))
    return newarr
