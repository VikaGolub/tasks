num = input("Input number: ")
def parse_num(num):
    if num % 2 == 0:
        print("even : " + num)
    elif num % 2 == 1:
        print("odd : " + num)        
    else:
        print("False")
