try:
    height = float(input('Enter your height: '))
    weight = float(input('Enter your weight: '))

    bmi = weight / height**2

    if bmi < 18.5:
        print('you are skinny ')
        print(bmi)
    elif bmi > 18.5:
        print('normal weight')
        print(bmi)
    elif bmi > 25:
        print('u are overweight')
        print(bmi)
    elif bmi > 30:
        print('жирдяй ебаный')
        print(bmi)
except ValueError as e:
    print('Error')

