def enq(node):
    global last
    last += 1
    tree[last] = node

    c = last
    p = c // 2

    while p and tree[p] < tree[c]:
        tree[p], tree[c] = tree[c], tree[p]
        c = p
        p = c // 2

def deq():
    global last
    tmp = tree[1]
    tree[1] = tree[last]
    last -= 1

    p = 1
    c = p * 2   # 왼쪽 자식
    while c <= last:
        # 오른쪽 자식이 있으면 왼쪽과 오른쪽을 비교 후 큰 자식을 선택
        if c + 1 <= last and tree[c] < tree[c+1]:
            c = c + 1
        if tree[p] < tree[c]:   # 부모 자식 노드 비교
            tree[p], tree[c] = tree[c], tree[p]
            p = c
            c = p * 2
        else:
            break
    return tmp

# 최대힙

last = 0    # 힙의 원소의 갯수 (힙의 사이즈)
tree = [0] * 100
enq(4)
enq(15)
enq(13)
enq(11)
enq(19)
enq(20)
enq(23)
print(tree)
deq()
print(tree)
print(last)