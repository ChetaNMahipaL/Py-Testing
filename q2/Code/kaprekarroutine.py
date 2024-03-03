"""
    This module calculates as per the question
"""

def main(num):
    """
    Main function is here
    """
    try:
        num_x = int(num)
    except ValueError:
        print("Enter a valid integer")
        return("Enter a valid integer")
    if len(num) != 4 or (len(set(num)) == 1 and len(num) ==4):
        ans = "Enter a valid 4-digit number"
        print(ans)
        return ans
    if num_x == 6174:
        return 6174
    while True:
        digits = [int(x) for x in str(num_x)]
        # Add leading zeros if the length is less than 4
        while len(digits) < 4:
            digits.insert(0, 0)
        digits.sort(reverse=True)
        big_num = int(''.join(map(str, digits)))
        small_num = int(''.join(map(str, sorted(digits))))
        result = big_num - small_num
        if result == 6174:
            print("Routine Successfully Completed")
            return 6174
        num_x = result
    
if __name__ == '__main__':
    number = input("Enter the number: ")
    main(number)
