__all__ = (
    'even_odd',
)


def even_odd(arr: list[int]) -> float:
    chetSum = 0
    nechetSum = 0
    i=0
    if len(arr) == 0:
        return 0
    for number in arr:
        if number%2 == 0:
            chetSum+=number
        else:
            nechetSum += number
    if nechetSum == 0 or chetSum == 0:
        return 0
    return(chetSum/nechetSum)
