odd = lambda no:(no % 2 != 0)
def main():
    no = int(input("Enter the number you want:"))
    ret = odd(no)
    print("The value returns:",ret)
if __name__ == "__main__":
    main()
    

