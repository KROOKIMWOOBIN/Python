def solution(arr1, arr2):
    return [[a + b for a, b in zip(sub_arr1, sub_arr2)] for sub_arr1, sub_arr2 in zip(arr1, arr2)]
