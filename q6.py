Evenodd = lambda no: (no % 2 == 0)
def main():
    no = int(input("Enter the number you want:"))
    ret = Evenodd(no)
    print("The value is :",ret)

if __name__ == "__main__":
    main()

