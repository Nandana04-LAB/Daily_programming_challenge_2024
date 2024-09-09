def dutch_national_flag(arr):
    low, mid, high = 0, 0, len(arr) - 1
    while mid <= high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        else:
            arr[high], arr[mid] = arr[mid], arr[high]
            high -= 1

if __name__ == "__main__":
    arr1 = [0, 1, 2, 1, 0, 2, 1, 0]
    dutch_national_flag(arr1)
    print(arr1)

    arr2 = [2, 2, 2, 2]
    dutch_national_flag(arr2)
    print(arr2)

    arr3 = [0, 0, 0, 0]
    dutch_national_flag(arr3)
    print(arr3)

    arr4 = [1, 1, 1, 1]
    dutch_national_flag(arr4)
    print(arr4)

    arr5 = [2, 0, 1]
    dutch_national_flag(arr5)
    print(arr5)

    arr6 = []
    dutch_national_flag(arr6)
    print(arr6)
