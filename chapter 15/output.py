# def f(n):
#     if n > 0:
#         f(n - 1)
#         print(n, end=' ')
#
#
# f(5)


def f(n):
    if n != 0:
        print(n, end='')
        f(n // 10)


f(50)
