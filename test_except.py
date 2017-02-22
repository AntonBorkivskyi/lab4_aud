def raise_func():
    raise IndexError
    raise KeyError

def except_func():
    try:
        raise_func()
    except IndexError:
        print("Indexxxxx Errrror")
    except KeyError:
        print("Keeeey Errrror")
    except Exception:
        print("Anoother Errrror")


class Myexc(Exception):
    def myexcept_raise_func(self):
        except_func()