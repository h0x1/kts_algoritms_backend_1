from typing import TypeVar

__all__ = (
    'flip_kv_vk',
    'flip_kv_vk_safe',
)


KT = TypeVar('KT')
KV = TypeVar('KV')


def flip_kv_vk(d: dict[KT, KV]) -> dict[KV, KT]:
    retDict = {}
    for k, v in d.items():
        retDict[v] = k
    return retDict


def flip_kv_vk_safe(d: dict[KT, KV]) -> dict[KV, list[KT]]:
    retDict = {}
    for k, v in d.items():
        if v in retDict:
            retDict[v].append(k)
        else:
            retDict[v] = [k]
    return retDict
