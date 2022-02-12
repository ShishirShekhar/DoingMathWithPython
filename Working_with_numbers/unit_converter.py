"""
Unit converter
"""

def run():
    """
    This function runs the program
    """
    print('Welcome to Conversion module')
    print('Select the type of conversion')
    print('1 for distance conversion')
    print('2 for temperature conversion')
    print('3 for mass conversion')
    choice = int(input())
    if choice == 1:
        dc()
    elif choice == 2:
        tc()
    elif choice == 3:
        mc()
    else:
        print('Please enter the correct option')

def dc():
    """
    This function shows distance conversion menu
    """
    print('Select conversion')
    print('1 for kms to miles')
    print('2 for miles to kms')
    choice = int(input())
    if choice == 1:
        kms_miles()
    elif choice == 2:
        miles_kms()
    else:
        print('Please enter the correct option')

def tc():
    """
    This function shows temperature conversion menu
    """
    print('Select conversion')
    print('1 for C to F')
    print('2 for F to C')
    choice = int(input())
    if choice == 1:
        cf()
    elif choice == 2:
        fc()
    else:
        print('Please enter the correct option')
    
def mc():
    """
    This function shows mass conversion menu
    """
    print('Select conversion')
    print('1 for pounds to kgs')
    print('2 for kgs to pounds')
    choice = int(input())
    if choice == 1:
        pk()
    elif choice == 2:
        kp()
    else:
        print('Please enter the correct option')

def kms_miles():
    """
    This function converts kms values to miles
    """
    kms = int(input('Enter the value in kms: '))
    miles = kms/1.609
    return miles

def miles_kms():
    """
    This function converts miles values to kms values
    """
    miles = int(input('Enter the value in miles: '))
    kms = miles * 1.609
    return kms

def fc():
    """
    This converts F to C
    """
    f = int(input('Enter the value of fahrenheit: '))
    c = (f - 32) * 5/9
    return c

def cf():
    """
    This converts C to F
    """
    c = int(input('Enter the value of Celsius: '))
    f = (c * 9/5) + 32
    return f

def kp():
    """
    This function converts kgs to pounds
    """
    k = int(input('Enter the value in kgs: '))
    p = k * 2.20462262185
    return p

def pk():
    """
    This function converts pounds to kgs
    """
    p = int(input('Enter the value in pounds: '))
    k = p / 2.20462262185
    return k

if __name__ == '__main__':
	while True:
        result = run()
		print(result)
		a = input('Do you want to exit?(y/n)')
		if a == 'y':
			break
