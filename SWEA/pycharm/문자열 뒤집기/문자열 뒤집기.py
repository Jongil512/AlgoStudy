a = 'algorithm'

def reverse_str(s):
    b = list(s)
    for i in range(len(b) // 2):
        b[i], b[-i-1] = b[-i-1], b[i]
    new_str = ''.join(b)
    return new_str

ans = reverse_str(a)
print(ans)

q = 2457634
w = list(q)
print(w)