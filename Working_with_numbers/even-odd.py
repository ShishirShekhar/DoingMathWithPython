def even_odd(num):
    """
    This function print whether the number is even or odd
    and print next 9 even or odd numbers to it.
    """
    if float(num).is_integer():
        if num % 2 == 0:
            print(f'{num} is even')
            for i in range(num, num*10+1):
                if i % 2 == 0:
                    print(i)
        else:
            print(f'{num} is odd')
            for i in range(num, num*20):
                if i % 2 != 0:
                    print(i)
    else:
        print('Please enter a interger!')

if __name__ == '__main__':
	while True:
		print(even_odd(5))
		a = input('Do you want to exit?(y/n)')
		if a == 'y':
			break
