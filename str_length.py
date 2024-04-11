def sort_strings_by_length(strings):
    sorted_strings_asc = sorted(strings, key=len)
    print("По возрастанию:")
    print(sorted_strings_asc)

    sorted_strings_desc = sorted(strings, key=len, reverse=True)
    print("\nПо убыванию:")
    print(sorted_strings_desc)

strings = ["Яблоко", "Андрей", "Тестовое задание", "Май", "Апрель"]
sort_strings_by_length(strings)
