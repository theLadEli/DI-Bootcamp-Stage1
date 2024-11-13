with open('starwars.txt', 'a+', encoding='utf-8') as f:
    f.seek(0)
    lines = f.readlines()
    print(lines[4])

    f.seek(0)
    five_char = f.read(5)
    print(five_char)

    def file_as_list_of_strings():
        f.seek(0)
        content = []
        content = (f.read().split('\n'))
        return content

    darth_count = file_as_list_of_strings().count('Darth')
    luke_count = file_as_list_of_strings().count('Luke')
    lea_count = file_as_list_of_strings().count('Leah')
    print(f'Darth appears {darth_count} times\nLuke appears {luke_count} times\nLea appears {lea_count} times')

    f.write("\nEli")

    f.seek(0)
    content = f.readlines()
    for i,line in enumerate(content):
        if line == 'Luke':
            content[i] = 'Luke Skywalker'
    f.write("".join(content))