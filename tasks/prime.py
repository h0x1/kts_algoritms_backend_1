__all__ = (
    'is_prime',
)


def is_prime(number: int) -> bool:
    if(number == 1):
        return False
    mod = 2
    for mod in range(mod, number, mod*mod):
        if number%mod == 0:
            return False
    return True
