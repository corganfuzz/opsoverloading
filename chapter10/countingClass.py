class Count:
    def __init__(self):
        self.state = 0


def main():
    myCount = Count()
    times = 2

    for i in range(0, 100):
        handleIncrement(myCount, times)

    print(myCount.state, times)


def handleIncrement(counter, timer):
    counter.state += 1
    timer += 1

    # print(counter.state, timer)


main()
