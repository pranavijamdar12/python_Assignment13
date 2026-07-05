Divisible = lambda no:(no % 5 == 0)
def main():
    no = int(input("Enter the number you want:"))
    ret = Divisible(no)
    print("The value is :",ret)

if __name__ == "__main__":
    main()
    
