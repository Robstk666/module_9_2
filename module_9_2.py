# Исходные списки
first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

# Создание списка длин строк из first_strings длиной не менее 5
first_result = [len(s) for s in first_strings if len(s) >= 5]

# Создание списка кортежей слов одинаковой длины
second_result = [(word1, word2) for word1 in first_strings for word2 in second_strings if len(word1) == len(word2)]

# Создание словаря строк и их длин для строк четной длины
third_result = {s: len(s) for s in first_strings + second_strings if len(s) % 2 == 0}

# Вывод результатов
print(first_result)
print(second_result)
print(third_result)