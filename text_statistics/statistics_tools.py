import re
from collections import Counter

def get_clean_words(text):
    # Очищення тексту від пунктуації та приведення до нижнього регістру.
    return re.findall(r'[\w]+', text.lower())

def count_sentences(text):
    # Підрахунок кількості речень за знаками завершення з перевіркою на пробіл після них.
    return len(re.findall(r'[.!?]+(?=\s|$)', text))

def avg_sentence_length(text):
    # Обчислення середньої кількості слів у реченні з округленням до 2 знаків.
    words = get_clean_words(text)
    s_count = count_sentences(text)
    if s_count == 0:
        return 0.0
    return round(len(words) / s_count, 2)

def lexical_diversity(text):
    # Обчислення відношення унікальних слів до загальної кількості слів.
    words = get_clean_words(text)
    if not words:
        return 0.0
    unique_words = set(words)
    return len(unique_words) / len(words)

def most_common_bigrams(text, n=5):
    # Пошук та підрахунок найчастіших пар слів (біграм) у вигляді кортежів.
    words = get_clean_words(text)
    bigrams = [(words[i], words[i+1]) for i in range(len(words) - 1)]
    return Counter(bigrams).most_common(n)

def hapax_legomena(text):
    # Пошук усіх слів, що зустрічаються в тексті лише один раз.
    words = get_clean_words(text)
    counts = Counter(words)
    return [word for word, count in counts.items() if count == 1]