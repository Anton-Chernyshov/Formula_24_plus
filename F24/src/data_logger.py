import datetime


def logger(func: "function", *args, **kwargs):  # decorator to log to file 
    def wrapper(*args, **kwargs):
        ret = func(*args, **kwargs)
        
        time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        data = f"[{time}] -> called function [{func.__name__}] with arguments [{args}, {kwargs}] -> [{ret}]"
        with open(f"log [{time}].logfile", "a") as file:
            file.write(data+"\n")
        
        print(data)
        return ret
    return wrapper




