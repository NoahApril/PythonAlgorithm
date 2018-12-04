from typing import TypeVar, Generic
from random import randint

T = TypeVar('T')

class SortHelper:
    currentVersion = "1.0";

    def generateRandomArray(array_len:int, array_range_l:int, array_range_r:int):
        newArray=[]
        for i in range(1, array_len):
            randomValue = randint(array_range_l, array_range_r)
            newArray.append(randomValue)
        return newArray

