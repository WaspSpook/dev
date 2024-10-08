# работа со словами

word = 'test'
if len(word) % 2 == 1:
    print(word[len(word) // 2])
else:
    print(word[len(word) // 2 - 1: len(word) // 2 + 1])

