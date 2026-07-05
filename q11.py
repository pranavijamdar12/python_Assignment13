Largest = lambda a, b, c: a if (a >= b and a >= c) else (b if b >= c else c)

def main():
    no1 = int(input("Enter the number:"))
    no2 = int(input("Enter the number"))
    no3 = int(input("Enter the number"))
    ret = Largest(no1,no2,no3)
    print("The largest number is:",ret)

if __name__ == "__main__":
    main()
