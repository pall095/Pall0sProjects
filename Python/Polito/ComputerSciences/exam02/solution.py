nameFile = open("parole_italiane.txt","r")

filename = input("please enter the file name: ")
mispellFile = open(filename,"r")

name2mispell = []
for name in mispellFile:
    name = name.rstrip()
    name2mispell.append(name)
print(name2mispell)

italian = []
for name in nameFile:
    name = name.rstrip()
    italian.append(name)
print(italian)

for name in name2mispell:
    print(f"name: {name}")
    for word in italian:
        cnt = 0
        # check if only a letter changed
        if len(name) == len(word):
            for i in range(len(name)):
                if name[i].lower() != word[i].lower():
                    cnt += 1
        if cnt == 1:
            print(word)