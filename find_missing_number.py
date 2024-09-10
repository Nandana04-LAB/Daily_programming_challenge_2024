def find_missing_number(arr, n):
   
    total_sum = n * (n + 1) // 2
    array_sum = sum(arr)
    missing_number = total_sum - array_sum
    return missing_number


arr = [1, 2, 4, 5]
n = 5 

missing_number = find_missing_number(arr, n)
print(f"Missing Number: {missing_number}")
