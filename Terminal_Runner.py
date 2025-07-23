from load_into_table import load_data
from compare_with_table import compare_with_table

input_list = []

run = True
while run:
    print('enter text to embed into DB (x to exit):')
    content = input()

    if content.upper() == "X":
        run = False
        continue

    input_list.append(content)

load_data(input_list)

run = True
while run:
    print('enter text to compare against db for closes match (x to exit):')
    content = input()

    if content.upper() == "X":
        run = False
        continue

    result = compare_with_table(content, 5)

    print(result)