def fib(num):
    x = 0
    y = 1
    for i in range(num):
        print(f"{y:08X}")
        x, y = y, x + y


if __name__ == '__main__':
    fib(11)
