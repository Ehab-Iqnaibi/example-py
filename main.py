def isprime(num):
    i=2
    while i< number:
        if number % i == 0:
            print(str(number) + ' is not prime ')
            break
        i = i + 1
    else:
        print(str(number) + ' is prime ')

while True:
    number = int(input('Enter number '))
    cho=int(input('choose a number 1 or 2 '))
    if cho==1:
        i = 2
        while i < number:
            if number % i == 0:
                print(str(number) + ' is not prime ')
                break
            i = i + 1
        else:
            print(str(number) + ' is prime ')
    elif cho ==2:
        isprime(number)




