def is_year_leap(year):
    if year % 4 == 0:
        return True
    else:
        return False


check_year = 2024
check2_year = 2023


result1 = is_year_leap(check_year)
result2 = is_year_leap(check2_year)


print(f"год {check_year}: {result1}")
print(f"год {check2_year}: {result2}")
