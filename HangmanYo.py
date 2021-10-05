import random

chance = 6
used = []

infile = open("words.txt", "r")
lines = infile.readlines()
infile.close()

word = random.choice(lines).strip

print("행맨 게임!")
print("단어를 생각했습니다..")
print("." * len(word))
print("6번의 기회가 남았습니다")
print()

while True:
    letter = input("알파벳 소문자를 입력하세요")
    used.append(letter)
    failed = 0

    for ch in word:
        if ch in used:
            print(ch, end="")
        else:
            print(".", end="")
            failed += 1

    print()

    if failed == 0:
        print("축하합니다. 단어를 맞췄습니다")
        break

    if not letter in word:
        chance -= 1
        print("틀렸습니다", end=" ")
        if chance == 0:
            print("\n\n이것도 못맞추네요~ 정답은", word + " 입니다")
            break

    print(str(chance) + "번의 기회가 남았습니다.\n")
    
