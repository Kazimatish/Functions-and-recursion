names = ['kalam','salam','kalam','qadeer','kaleem','sagheer']
word = input("Enter a word: ")
for i in names:
    if(word == i):
        names.remove(i)

print(names)


# new_names = []

# for i in names:
#     if i != word:
#         new_names.append(i)

# names = new_names
# print(names)