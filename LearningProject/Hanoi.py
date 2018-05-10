def move (n, first, buffer, end):
    if n == 1:
        print(first, '-->', end)
    else:
        move (n-1, first, end, buffer )
        move (1, first, buffer, end )
        move (n-1, buffer, first, end)

move(3, 'A', 'B', 'C')