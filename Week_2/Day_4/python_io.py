# # Old wat of opening files in P=py:
# f = open('sample.txt', 'r+')
# content = f.read()
# print(content)
# f.close()

# # New way
with open('sample.txt', 'a+', encoding='utf-8') as f:
    for i in range(10):
        f.write(f'This is line {i}\n')
    f.seek(0)
    content = f.read()
    print(content)