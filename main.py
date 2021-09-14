# Program implementing the Binary Search
def binary_search(array, target):
    beg = 0
    end = len(array) - 1

    while beg <= end:
        mid = int((beg + end) / 2)
        if array[mid] < target:
            beg = mid + 1
        elif array[mid] > target:
            end = beg - 1
        else:
            print(f"Item found at postion {mid + 1}")
            return


# static array
prices = [25, 35, 45, 55, 65, 75, 85, 95]

binary_search(prices, 75)