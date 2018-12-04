import SortHelper as sh
import SelectionSort as ssort


if __name__ == '__main__':

    array_length = 1000
    newArray = sh.SortHelper.generateRandomArray(array_length, 1, 123343)
    ssort.SelectSort.sortFunction(ssort.SelectSort, newArray)



