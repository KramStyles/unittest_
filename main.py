from utility import performance


if __name__ == '__main__':
    @performance
    def check():
        for i in range(100000):
            num = i * 5
        print(num)

    check()
