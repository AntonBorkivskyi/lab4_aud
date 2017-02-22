def raise_func():
    raise IndexError("!!!", "verrrry bad")

def except_func():
    try:
        raise_func()
    except IndexError as ie:
        print("Indexxxxx Errrror")
        print(ie)
    except KeyError as ke:
        print("Keeeey Errrror")
        print(ke)
    except Exception:
        print("Anoother Errrror")


class Myexc(Exception):
    def myexcept_raise_func(self):
        except_func()

err = Myexc()
err.myexcept_raise_func()
