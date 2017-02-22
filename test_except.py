def raise_func():
    raise IndexError

def except_func():
    try:
        raise_func()
    except Exception:
        print("Errrror")
except_func()