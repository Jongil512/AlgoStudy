# UCPC

def func():
    ans = 'I hate UCPC'
    need = ['U', 'C', 'P', 'C']
    for i in word:
        if i == need[0]:
            need.pop(0)
            if need:
                continue
            else:
                ans = 'I love UCPC'
                return ans
    return ans

word = input()
print(func())