height = float(input('Height: '))
weight = float(input('Weight: '))
bmi = round(weight/height**2, 2)

if bmi < 18.5:
    print(f'Your BMI: {bmi}. You are underweight.')
elif bmi >= 18.5 and bmi < 25:
    print(f'Your BMI: {bmi}. You are normal weight.')
elif bmi >= 25 and bmi < 30:
    print(f'Your BMI: {bmi}. You are overweight.')
elif bmi >= 30:
    print(f'Your BMI: {bmi}. You are obese.')
else:
    print('Howled the scale!')