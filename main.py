
all_names = open("./Input/Names/invited_names.txt", "r")
starting_letter = open("./Input/Letters/starting_letter.txt", "r")
names = all_names.readlines()
content = starting_letter.read()

list_of_letters = []

for name in names:
    letters = content.replace("[name]", name.strip())
    list_of_letters.append((name.strip(), letters))


for name, letter in list_of_letters:
    with open(f"./Output/ReadyToSend/letter_for_{name}.txt", "w") as f:
        f.write(letter)