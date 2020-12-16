from cache.lru_cache import LRU
from cache.mru_cache import MRU


def lru():
    cache_size = input(
        "please specify the size of the cache (default is set to 128): \n"
    )
    if not cache_size and cache_size.isnumeric():
        print("not a valid number")
        exit()
    cache_size = int(cache_size) if cache_size else None
    if cache_size:
        cache = LRU(cache_size)
    else:
        cache = LRU()
    exit_flag = False
    while not exit_flag:
        key = input("enter the key to be stored:\n")
        value = input("enter the value stored:\n")
        cache.set_value(key, value)
        exit = input("Y/N")
        exit_flag = True if exit == "Y" else False
    print(cache.get_all())
    fetch_data = input("specify the key to be fetched: ")
    print(cache.get_value(fetch_data))
    print(cache.get_all())


def mru():
    cache_size = input(
        "please specify the size of the cache (default is set to 128): \n"
    )
    if not cache_size and cache_size.isnumeric():
        print("not a valid number")
        exit()
    cache_size = int(cache_size) if cache_size else None
    if cache_size:
        cache = MRU(cache_size)
    else:
        cache = MRU()
    exit_flag = False
    while not exit_flag:
        key = input("enter the key to be stored:\n")
        value = input("enter the value stored:\n")
        cache.set_value(key, value)
        exit = input("Y/N")
        exit_flag = True if exit == "Y" else False
        print(cache.get_all())
        fetch_data = input("specify the key to be fetched: ")
        print(cache.get_value(fetch_data))
        print(cache.get_all())


cache_dictionary = {"l": lru, "m": mru, "e": lambda: exit}


def main(cache_type):
    """TODO: Docstring for main.

    :function: TODO
    :returns: TODO

    """
    cache_dictionary.get(cache_type, lambda: "Invalid")()


if __name__ == "__main__":
    exit_flag = False
    cache_type = input("l: LRU cache\nm: MRU cache\ne: exit\n")
    main(cache_type)
