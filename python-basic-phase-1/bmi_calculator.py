def BMIcalculator(w, h_feet):
    h_meters = h_feet * 0.3048
    bmi = w / (h_meters * h_meters)
    print("BMI:", round(bmi, 2))
    
    if bmi < 18.5:
        print("Underweight")
    elif 18.5 <= bmi < 25:
        print("Normal weight")
    elif 25 <= bmi < 30:
        print("Overweight")
    else:
        print("Obese")

BMIcalculator(82, 5.4)
