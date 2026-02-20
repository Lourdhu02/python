def seasonCheck(month):
    if month in (12,1,2):
        return "winter"
    elif 3 <= month <= 5:
        return "spring"
    elif 6 <= month <=8:
        return "summer"
    elif 9 <= month <= 11:
        return "fall"
    else:
        return "Enter valid Month" 
    
print(seasonCheck(12))