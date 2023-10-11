def solution(arr1, arr2):
    return [[a + b for a, b in zip(sub_arr1, sub_arr2)] for sub_arr1, sub_arr2 in zip(arr1, arr2)]

'''
arr1[(5, 4), (4, 6)]
arr2[(4, 6), (6, 2)]
sub_arr1, sub_arr2 in zip(arr1, arr2)] 여기서 [(5, 4), (4,6)], [(4, 6), (6, 2)] 변환
[a + b for a, b in zip(sub_arr1, sub_arr2)] 여기서 5 + 4, 4 + 6해서
[(9, 10), (10, 8)]로 반환
'''