from typing import Any

__all__ = (
    'cartesian_product',
)


def cartesian_product(arr1: list[Any], arr2: list[Any]) -> list:
    newarr = []
    for i in range(0, len(arr1)):
        for i2 in range(0, len(arr2)):
            newarr.append((arr1[i],arr2[i2]))
    return newarr
