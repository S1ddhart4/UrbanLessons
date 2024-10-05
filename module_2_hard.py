def generate_password(n):
    password = ""
    for i in range(1, 21):
        for j in range(i + 1, 21):
            pair_sum = i + j
            if n % pair_sum == 0:
                password += f"{i}{j}"
    return password
n = int(input("Введите число от 3 до 20: "))
if 3 <= n <= 20:
    result = generate_password(n)
    print(f"Пароль для числа {n}: {result}")
else:
    print("Число должно быть в диапазоне от 3 до 20.")
