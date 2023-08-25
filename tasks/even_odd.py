__all__ = (
    'even_odd',
)


def even_odd(arr: list[int]) -> float:
    chetSum = 0
    nechetSum = 0
    for number in arr:
        if number%2 == 0:
            chetSum+=number
        else:
            nechetSum += number
    return(chetSum/nechetSum)
