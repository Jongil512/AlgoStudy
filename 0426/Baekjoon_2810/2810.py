N = int(input())
arr = list(map(str, input()))
new_arr = ['*']
for i in range(N):
    if arr[i] == 'S':
            new_arr.append('S')
            new_arr.append('*')
    elif arr[i] == 'L':
        new_arr.append('L')
        new_arr.append('L')
        new_arr.append('*')
print(new_arr)
cnt_S = new_arr.count('S')
cnt_L = new_arr.count('L')
cnt_holder = new_arr.count('*')
if cnt_holder >= cnt_S + cnt_L:
    print(cnt_S + cnt_L)
else:
    print(cnt_S + cnt_L - cnt_holder)