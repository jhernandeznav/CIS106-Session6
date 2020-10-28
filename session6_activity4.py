# activity 4
def fun_rate(years):
    if int(years) == 5 or int(years) == 10:
        interest_rate = 2
    elif int(years) >= 1 and int(years) <= 3:
        interest_rate = 1
    else:
        interest_rate = 5
    return interest_rate


years = input("Enter the term: ")

interest_rate = fun_rate(years)

print("Term: ", years, "years")
print("CD interest rate: ", interest_rate, "%")
