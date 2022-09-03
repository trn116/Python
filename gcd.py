print('This is a program to compute GCD of 2 Numbers')
x=int (input('Please enter first number = '))
y=int (input('Please enter second number = '))

if x>y:
    if x%y==0:
        print('GCD is',y)
    else:
        z = y
        y = y-1
        while y>1:
            if (z%y == 0 and x%y == 0):
                print('GCD is',y)
            y-=1
        if y == 1:
            print('GCD is 1')
else:
     if y%x==0:
        print('GCD is',x)
     else:
        z = x
        x = x-1
        while x>1:
            if (z%x == 0 and y%x == 0):
                print('GCD is',x)
            x-=1
        if x==1:
            print('GCD is 1')
