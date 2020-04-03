board = [[2, 1, 1],
         [1, 2, 2],
         [2, 1, 1]]

def is_solved(board):
    a1 = board[0][0]
    a2 = board[0][1]
    a3 = board[0][2]
    b1 = board[1][0]
    b2 = board[1][1]
    b3 = board[1][2]
    c1 = board[2][0]
    c2 = board[2][1]
    c3 = board[2][2]
    a = [a1, b1, c1]
    b = [a2, b2, c2] 
    c = [a3, b3, c3]
    d = board[0]
    e = board[1]
    f = board[2]
    g = [a1, b2, c3]
    h = [a3, b2, c1]
    i = sum(a) == 3 and 0 not in a
    j = sum(b) == 3 and 0 not in b
    k = sum(c) == 3 and 0 not in c
    l = sum(d) == 3 and 0 not in d
    m = sum(e) == 3 and 0 not in e
    n = sum(f) == 3 and 0 not in f
    o = sum(g) == 3 and 0 not in g
    p = sum(h) == 3 and 0 not in h
    x_wins = [i, j, k, l, m, n, o, p]
    q = sum(a) == 6
    r = sum(b) == 6
    s = sum(c) == 6
    t = sum(d) == 6
    u = sum(e) == 6
    v = sum(f) == 6
    w = sum(g) == 6
    x = sum(h) == 6
    o_wins = [q, r, s, t, u, v, w, x]
    status = []
    for each_line in board:
        for each in each_line:
            status.append(str(each))
    for each in x_wins:
        if each:
            return 1
    for each in o_wins:
        if each:
            return 2
    if '0' in status:
        return -1
    else:
        return 0