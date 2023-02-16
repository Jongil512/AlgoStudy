def solution(dots):
    # (X축의 최댓값 - X축의 최솟값)  *  (Y축의 최댓값 - Y축의 최솟값)
    return (max(dots)[0] - min(dots)[0]) * (max(dots)[1] - min(dots)[1])