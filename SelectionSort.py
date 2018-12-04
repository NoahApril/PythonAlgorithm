
class SelectSort:

    def sortFunction(self, newArray:[]):
        # Traverse through all array elements
        for i in range(len(newArray)):
            # Find the minimum element in remaining
            # unsorted array
            min_idx = i
            for j in range(i + 1, len(newArray)):
                if (newArray[min_idx] > newArray[j]):
                    min_idx = j
            # Swap the found minimum element with
            # the first element
            newArray[i], newArray[min_idx] = newArray[min_idx], newArray[i]
            # Driver code to test above
        print("Sorted array")
        for i in range(len(newArray)):
            print("%d" % newArray[i])
        return newArray


