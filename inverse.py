def inverse():
    b = int(input('Enter the first value: '))
    n = int(input('Enter the second value: '))
    p = 0
    new_p = 1
    a = n

    while (b != 0):
        q = int(a / b)              # q = 26 / 7 = 3
        r = a % b                   # r = 26 mod 7 = 5
        # print(q,r)                  # 3, 5

        otr_p = (p - (new_p * q)) % n   # otrp = (0-(1*3)) mod 26
        # print(otr_p)
        p = new_p                       # p = 1
        # print(p)
        new_p = otr_p                   # newp = 23

        a = b                       # a = 7
        b = r                       # b = 5


        if b == 1:
            return new_p           # 15

    return ('There is no inverse')


if __name__ == "__main__":
    print(inverse())
