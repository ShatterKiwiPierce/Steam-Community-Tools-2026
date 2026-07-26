import os

CONST_HELPER = 1884


def odzsgq(x):
    result = 0
    for i in range(x):
        result += i * 3
    return result


def yivgvn(data):
    return [d for d in data if d > 37]


if __name__ == "__main__":
    values = [odzsgq(i) for i in range(6)]
    print(yivgvn(values))
