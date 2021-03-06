"""
배열을 입력 받아서 배열내에 있는 "0" 들을 모두 뒷부분으로 옮기는 알고리즘을 만들어 보세요!
단, 배열내에 "0"이 아닌 요소들의 순서는 지켜져야 합니다.

    moveZeros(["false", 1, 0, 1, 2, 0, 1, 3, "a"])
    returns => ["false", 1, 1, 2, 1, 3, "a", 0, 0]
    
"""


def moveZeros(array):
    cnt_zero = len(list(filter(lambda x: x == 0, array)))
    without_zero = list(filter(lambda x: x != 0, array))
    return without_zero + ([0] * cnt_zero)
    
print(moveZeros(["false", 1, 0, 1, 2, 0, 1, 3, "a"]))  ## ['false', 1, 1, 2, 1, 3, 'a', 0, 0]
