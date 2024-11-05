import datetime
class logFile:

    def __init__(self, sessionFile: str):
        ...


def logger(func: function, file: logFile, *args, **kwargs):  # decorator to log to file 
    
    ret = func(*args, **kwargs)