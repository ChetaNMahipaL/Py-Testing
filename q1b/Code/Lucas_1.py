"""
    This module is imported for handling n = 1000000
"""
import decimal

def calculate(index):
    """
        This function calculates the value of required
    """
    if index == 0:
        return -3
    if index == 1:
        return -1
    # Set precision for decimal calculations
    decimal.getcontext().prec = 10000
    l_minus_2 = decimal.Decimal(-3)
    l_minus_1 = decimal.Decimal(-1)
    l_n = decimal.Decimal(0)
    for _ in range(2,index+1):
        l_n = l_minus_1 + l_minus_2
        l_minus_2 = l_minus_1
        l_minus_1 = l_n
    return l_n

def main():
    """
    Main function to take input and show result
    """
    while True:
        var_n = int(input("Please Enter the Value of n: "))
        if 1 < var_n < 1000001:
            result = calculate(var_n)
            print("The value of L is: ",result)
            break
        print("Error: Please enter value in between 1 and 1000001")

if __name__ == "__main__":
    main()
