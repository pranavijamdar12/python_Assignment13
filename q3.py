Max = lambda no1,no2:( no1 if no1 < no2 else no2)
def main():
    no1 = int(input("Enter the first number:"))
    no2 = int(input("Enter the second number:"))
    ret = Max(no1,no2)
    print("The Maximum number is :",ret)
if __name__ == "__main__":
    main()

