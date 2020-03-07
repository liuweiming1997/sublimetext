#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Base(tuple):
    __slots__ = ()

    def keys(self):
        return list(self._fields)

class MagicTuple(Base):

    def __new__(cls, vals, labels=None):
        t = tuple.__new__(cls, vals)
        if labels:
            t.__dict__.update(zip(labels, vals))
        else:
            labels = []
        t.__dict__["_labels"] = labels
        return t

    def __init__(self, vals, labels=None):
        print('init')

    @property
    def _fields(self):
        return tuple([l for l in self._labels if l is not None])

    def __setattr__(self, key, value):
        raise AttributeError("Can't set attribute: %s" % key)

    def _asdict(self):
        return {key: self.__dict__[key] for key in self.keys()}


a = MagicTuple([1, 2, 3], labels=["one", "two", "three"])


result = [a, a, a]

for one, two, three in result:
    print(one)
    print(two)
    print(three)

# print(a._fields)

# print(a)      # (1, 2, 3)
# print(a[0])   # 1
# print(a.one)  # 1
