"""
Multiplication Table printer
"""

def multi_table(num, upto):
    """
    This function returns the multiplication talble of the
    number upto given value.
    """
    if float(num).is_integer():
        print(f'Multiplication table of {num}')
        for i in range(1, upto+1):
            print(f'{num} X {i} = {num*i}')
    else:
        print('Enter an integer!')

if __name__ == '__main__':
    while True:
        num = int(input('Enter the number'))
        upto = int(input('Enter the number upto which you want multiplication'))
        multi_table(num, upto)
        a = input('Do you want to exit?(y/n)')
        if a == 'y':
            break