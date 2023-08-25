__all__ = (
    'seconds_to_str',
)

def seconds_to_str(seconds: int) -> str:
    if seconds > 0:
        sec = seconds%60
        min = seconds//60
        hour = min//60
        min = min%60
        day = hour//24
        hour = hour%24
        return ( (day > 0 and "%02dd%02dh%02dm"%(day,hour,min)) or (hour > 0 and "%02dh%02dm"%(hour,min)) or (min > 0 and "%02dm"%(min)) or "") + "%02ds"%(sec)
    return "seconds < 0"
