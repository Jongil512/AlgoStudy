import sys
sys.stdin = open('1976_input.txt')

def time_cal(h1, m1, h2, m2):
    # 시간값 초기화
    h = 0
    # 입력받은 분의 합을 m에 저장
    m = m1 + m2
    # m이 60 이상이라면 m을 60으로 나눈 몫을 h에 더한 후
    # 나머지를 m에 다시 저장
    if m >= 60:
        h += m // 60
        m = m % 60
    # 입력받은 시간 값의 합을 기존의 h에 더함
    h += h1 + h2
    # 12시간제이므로 h가 12 이상이라면 h - 12
    if h > 12:
        h = h - 12
    # 시, 분 리턴
    return h, m

T = int(input())
for tc in range(1, T + 1):
    h1, m1, h2, m2 = map(int, input().split())
    print(f'#{tc}', *time_cal(h1, m1, h2, m2))