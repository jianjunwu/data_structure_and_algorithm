#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   myarray.py
@Time    :   2020/10/14 10:34:45
@Author  :   nicholas wu 
@Version :   1.0
@Contact :   nicholas_wu@aliyun.com
@License :    
@Desc    :   None
'''


class MyArray(object):
    """A simple wrapper around List.
    You cannot have -1 in the array.
    """
    def __init__(self, size: int):
        self._data = []
        self._size = size

    def __getitem__(self, position: int) -> object:
        return self._data[position]

    def __setitem__(self, position: int, value: object):
        self._data[position] = value

    def __len__(self) -> int:
        return len(self._data)

    def __iter__(self):
        for item in self._data:
            yield item

    def find(self, index: int) -> object:
        try:
            return self._data[index]
        except IndexError:
            return None

    def insert(self, index: int, value: int) -> bool:
        if len(self) >= self._size:
            return False
        else:
            return self._data.insert(index, value)

    def delete(self, index: int) -> bool:
        try:
            self._data.pop(index)
            return True
        except IndexError:
            return False

    def print_all(self):
        for item in self:
            print(item)


def test_myarray():
    arr = MyArray(3)
    arr.insert(0, 2)
    arr.insert(0, 3)
    arr.insert(1, 5)
    assert arr.insert(0, 6) is False
    assert len(arr) == 3
    assert arr.find(1) == 5
    assert arr.delete(3) is False

    arr.print_all()


if __name__ == "__main__":
    test_myarray()


