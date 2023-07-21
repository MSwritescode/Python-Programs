w=float(input('Enter the weight in Kg:'))
h=float(input('Enter the height in Meters:'))

BMI=w/h**2

print('BMI is',BMI,end='\n')

if BMI<18.5:
    print('...Underweight')
elif BMI>=18.5 and BMI<24.9:
    print('...Normal')
elif BMI>=25 and BMI<29.9:
    print('...Overweight')
else:
    print('...Obese')
