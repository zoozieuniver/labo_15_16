from text_statistics import statistics_tools as ts

def main():
    #Точка входу в програму: зчитування тексту та вивід аналітики.
    print("=== Система аналізу тексту ===")
    user_input = input("Введіть текст для обробки: ")
    
    # Перевірка на порожній ввід для запобігання помилкам обчислень
    if not user_input.strip():
        print("Помилка: Текст не введено.")
        return

    # Збір та вивід статистичних даних
    sentences = ts.count_sentences(user_input)
    avg_len = ts.avg_sentence_length(user_input)
    diversity = ts.lexical_diversity(user_input)
    bigrams = ts.most_common_bigrams(user_input, n=3)
    hapaxes = ts.hapax_legomena(user_input)

    print("\n--- Результати аналізу ---")
    print(f"Кількість речень: {sentences}")
    print(f"Середня довжина речення: {avg_len} слів")
    print(f"Лексична різноманітність: {round(diversity * 100, 2)}%")
    
    print("\nТоп біграми:")
    for (w1, w2), count in bigrams:
        print(f" - '{w1} {w2}': {count} раз(и)")

    print(f"\nСлів, що зустрічаються один раз: {len(hapaxes)}")
    if hapaxes:
        print(f"Приклади рідкісних слів: {', '.join(hapaxes[:10])}...")

if __name__ == "__main__":
    main()