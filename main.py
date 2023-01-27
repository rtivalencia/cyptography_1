
def gcd(a, b):
    if a == 0:
        return b
    if 0 < a < b:
        return a

    return gcd(a % b, b)


# Driver code
if __name__ == "__main__":
    a = int(input("Enter the first value here: "))
    b = int(input("Enter the second value here: "))

    print("gcd(", a, ",", b, ") = ", gcd(a, b))



