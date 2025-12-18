def is_year_leap(year):
    return True if year % 4 == 0 else False


date = int(input("Введите число: "))
result = is_year_leap(date)
print(f"Год {date}: - {result}")
