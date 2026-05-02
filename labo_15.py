import statistics
from my_statistics import st

def main():
    try:
        user_input = input("Введіть числа через пробіл: ")
        data = [float(x) for x in user_input.split()]
        
        if not data:
            print("Список порожній!")
            return

        # Використовуємо твій пакет
        my_report = st.summarize(data)
        
        # Використовуємо стандартну бібліотеку
        std_report = {
            "mean": statistics.mean(data),
            "median": statistics.median(data),
            "mode": statistics.mode(data),
            "variance": statistics.pvariance(data),
            "std_dev": statistics.pstdev(data)
        }

        print(f"\n{'Показник':<15} | {'Мій пакет':<15} | {'Standard Lib':<15}")
        print("-" * 50)
        for key in my_report:
            print(f"{key:<15} | {my_report[key]:<15.4f} | {std_report[key]:<15.4f}")

    except ValueError:
        print("Помилка! Вводьте лише числа.")

if __name__ == "__main__":
    main()
