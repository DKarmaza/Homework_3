import re

def generator_numbers(text): # Пошук і розпізнавання чисел у тексті(з точністю 2 знаки після коми)
    numbers = re.findall(r' \d+\.\d+ ', text)
    for number in numbers:
        yield float(number)

def sum_profit(text, func): # Додавання всіх знайдених чисел
    return sum(func(text))


text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів." # Сам текст
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}") # Виведення 