def gcd():

    a = int(input("Enter the first value: "))       # 81, prompts for user input
    b = int(input("Enter the second value:  "))     # 57
    r = a % b          # calcs for remainder        # 24
    while (r != 0):     # while loop meanwhile r does not = 0
        a = b           # subs values for calculation of the algorithm
        b = r
        r = a % b       # new remainder and will loop as long as it does not = 0
    print('GCD is:', b) # output, 3




# Driver code
if __name__ == "__main__":
    print (gcd())
