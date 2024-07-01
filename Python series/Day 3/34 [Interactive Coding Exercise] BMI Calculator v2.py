height=float(input("Enter Your Height: "))
weight=int(input("Enter Your Weight: "))
bmi=weight/(height*height)
if bmi<18.5:
    print(f"Your BMI is {bmi}, Your are underweight. ")
elif bmi<25:    
    print(f"Your BMI is {bmi}, Your are normal weight. ")
elif bmi<30:    
    print(f"Your BMI is {bmi}, Your are slightly  overweight. ")
elif bmi<35:    
    print(f"Your BMI is {bmi}, Your are obese ")
else:    
    print(f"Your BMI is {bmi}, Your are clinically obese. ")
