import random as rd

def random_matrix(n):
    remaining = set(range(1, n * n + 1))
    A = [[None for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            elem = rd.sample(remaining, 1)[0]
            remaining = remaining.difference(set([elem]))
            A[i][j] = elem
    return A

def visuK(x, k, removeN):
    if x < k:
        if removeN:
            return 0
        return str(x) + "-"
    elif x > k:
        if removeN:
            return 1
        return str(x) + "+"
    else:
        return "x"

def printm(A, k=None, removeN=False):
    for i in range(len(A)):
        if k == None:
            print(A[i])
        else:
            print([visuK(x, k, removeN) for x in A[i]])

def iterRows(A):
    n = len(A)
    for i in range(n):
        if i % 2 == 0:
            A[i].sort()
        else:
            A[i].sort(key = lambda x: -x)

def iterColumns(A):
    n = len(A)
    for j in range(n):
        c = [A[i][j] for i in range(n)]
        c.sort()
        for i in range(n):
            A[i][j] = c[i]

def iterate(A):
    iterRows(A)
    iterColumns(A)

def count_good_rows(A, k):
    n = len(A)
    index = None
    for i in range(n):
        for j in range(n):
            if A[i][j] == k:
                index = i
    c = 0
    for i in range(n):
        b = False
        if i < index:
            b = True
            for j in range(n):
                b = b and A[i][j] < k
        if i > index:
            b = True
            for j in range(n):
                b = b and A[i][j] > k
        if b:
            c += 1
    return c

def count_mini_good_rows(A):
    n = len(A)
    mini = n + 1
    id_mini = None
    for k in range(1, n * n + 1):
        c = count_good_rows(A, k)
        if c < mini:
            mini = c
            id_mini = k
    return (id_mini, mini)

A = [[5, 8, 2],
     [9, 1, 7],
     [3, 6, 4]]
