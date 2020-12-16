from collections import OrderedDict


class LRU(OrderedDict):

    "Limit size, evicting the least recently looked-up key when full"

    def __init__(self, maxsize=128, /, *args, **kwds):
        self.maxsize = maxsize
        super().__init__(*args, **kwds)

    def __getitem__(self, key):
        try:
            value = super().__getitem__(key)
            self.move_to_end(key)
            return value
        except KeyError:
            return "key not found"

    def __setitem__(self, key, value):
        if key in self:
            self.move_to_end(key)
        super().__setitem__(key, value)
        if len(self) > self.maxsize:
            oldest = next(iter(self))
            del self[oldest]

    def set_value(self, key, value):
        return self.__setitem__(key, value)

    def get_value(self, key):
        data = self.__getitem__(key)
        if data:
            return data
        else:
            return "Not found"

    def get_all(self):
        return self

