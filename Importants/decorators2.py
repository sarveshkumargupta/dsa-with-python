


def lower_it(func):
    def wrapper(*args):
        res = func(args[0])

        return res.lower()

    return wrapper


def split_it(func):
    def wrapper(*args):
        res = func(args[0])

        return res.split(" ")

    return wrapper


@split_it
@lower_it
def my_statement(stmt: str):
    return stmt


print(my_statement("This is Sarvesh"))
