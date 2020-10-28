# activity 3
def fun_bonus(job_code, years_service):
    if job_code == "A" and int(years_service) > 10:
        bonus = 10000.00
    elif job_code == "A" and int(years_service) >= 5:
        bonus = 8000.00
    elif job_code == "B" and int(years_service) > 15:
        bonus = 9000.00
    else:
        bonus = 5000.00
    return bonus


last_name = input("Enter your last name:")
job_code = input("Enter job code:")
years_service = input("Enter the years of service:")

bonus = fun_bonus(job_code, years_service)

print("Last name:", last_name)
print("Bonus: $", bonus)
