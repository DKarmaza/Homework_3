def caching_fibonacci():
    cache = {} # Створення порожньго словника
    def fibonacci(n): 
        if n <= 0:    # Базові випадки та перевірка чи вже обчислено значення
            return 0
        elif n == 1:
            return 1
        elif n in cache:
            return cache[n]
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2) # Обчислення числа Фібоначчі
        return cache[n]
    return fibonacci
fib = caching_fibonacci() # Використання функції
print(fib(10)) # Виклик і обчислення, тут 10го числа