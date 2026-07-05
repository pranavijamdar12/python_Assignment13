Max  = lambda no1,no2:(no1 if no1 > no2 else no2)
def main():
    no1 = int(input("Enter the number you want:"))
    no2 = int(input("Enter the number you want:"))
    ret = Max(no1,no2)
    print("The Maximum number is :",ret)
if __name__ == "__main__":
    main()
