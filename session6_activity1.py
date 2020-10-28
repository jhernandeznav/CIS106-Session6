# activity 1
def fun_service_award(years_service):
    if int(years_service) > 10:
        service_award = 1000.00
    elif int(years_service) >= 5:
        service_award = 500.00
    else:
        service_award = 100.00
    return service_award


years_service = input("Enter the years in service:")

service_award = fun_service_award(years_service)

print("Service award: $", service_award)
