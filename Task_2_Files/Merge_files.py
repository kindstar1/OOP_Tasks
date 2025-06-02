def know_info_about_files(num):
    list_for_files = []
    for i in range(num):
        a = input('Введите название файла с указанием расширения (пример: 1.txt): ')
        list_for_files.append(a)
    return list_for_files

know_files = know_info_about_files(3)

# know_files = ["1.txt", "2.txt", "3.txt"] - для упрощенного тестирования

count_lines_dict = {}

for file in know_files:
    count = 0
    with open(file, 'r', encoding="utf-8") as f:
        for line in f:
            count += 1
    if file in count_lines_dict:
        count_lines_dict[file] = count
    else:
        count_lines_dict[file] = count

sorted_count_lines_dict = dict(sorted(count_lines_dict.items(), key=lambda item: item[1]))

for key, value in sorted_count_lines_dict.items():
    with open('Fin.txt', 'a', encoding="utf-8") as f:
        f.write(key + '\n')
        f.write(str(value) + '\n')
        with open(key, 'r', encoding="utf-8") as f2:
            for line in f2:
                f.write(line)
            f.write('\n')

            
                    