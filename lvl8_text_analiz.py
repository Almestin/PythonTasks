text_for_analyze = "Привіт! Ну, як твої справи? Це довге речення."
parasites = ["ну", "коротше", "типу"]
vowels = "аеєиіїоуюяАЕЄИІЇОУЮЯ"
consonants = "бвгґджзйклмнпрстфхцчшщБВГДЖЗЙКЛМНПРСТФХЦЧШЩ"


def clean_text(text):
    words = text.replace(",", "").replace(".", "").replace("!", "").replace("?", "").split()
    return words


def analyze_words(word_list):
    amount_of_words = len(word_list)
    the_longest_word = max(word_list, key=len)
    number_of_letters_max = len(the_longest_word)
    the_shortest_word = min(word_list, key=len)
    number_of_letters_min = len(the_shortest_word)
    total_length = sum(len(word) for word in word_list)
    average_word_length = total_length / amount_of_words
    return [amount_of_words, the_longest_word, number_of_letters_max, \
            the_shortest_word, number_of_letters_min, average_word_length]


def count_letters(text):
    number_of_vowels = 0
    number_of_consonants = 0
    for letter in text:
        if letter in vowels:
            number_of_vowels += 1
        elif letter in consonants:
            number_of_consonants += 1
    return [number_of_vowels, number_of_consonants]


def search_for_parasite(word_list):
    for word in word_list:
        if word.lower() in parasites:
            return [True, word]
    return [False]


print("=== Результати аналізу ===")
print(f"Всього слів: {analyze_words(clean_text(text_for_analyze))[0]}")
print(f"Найдовше слово: '{analyze_words(clean_text(text_for_analyze))[1]}' \
    ({analyze_words(clean_text(text_for_analyze))[2]} літер)")
print(f"Найкоротше слово: '{analyze_words(clean_text(text_for_analyze))[3]}' \
    ({analyze_words(clean_text(text_for_analyze))[4]} літери)")
print(f"Середня довжина слова: {round(analyze_words(clean_text(text_for_analyze))[5], 2)}")
print(f"Кількість голосних: {count_letters(text_for_analyze)[0]}")
print(f"Кількість приголосних: {count_letters(text_for_analyze)[1]}")
if search_for_parasite(clean_text(text_for_analyze))[0]:
    print(f"УВАГА: Знайдено слово-паразит '{search_for_parasite(clean_text(text_for_analyze))[1]}'")
