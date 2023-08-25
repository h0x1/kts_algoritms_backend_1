from typing import Any

__all__ = (
    'corresponding_pairs',
)


def corresponding_pairs(arr1: list[Any], arr2: list[Any]) -> list[tuple[Any, Any]]:
    newarr = []
    minLen = min(len(arr1),len(arr2))
    for i in range(0, minLen):
        newarr.append((arr1[i],arr2[i]))
    return newarr
