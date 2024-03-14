print("Projekt_1.py: první projekt do Engeto Online Python Akademie")
print("author: Tomáš Komárek")
print("email: tomaskomi@gmail.com")
print("discord: tomaskomi")

separator = "-" * 40
print(separator)

users = {
"bob" : "123", "ann" : "pass123", "mike" : "password123", "liz" : "pass123"
}

username = input("Enter username: ")
password = input("Enter password: ")

if username in users and users[username] == password:
    print("Welcome to the app,", username)
else:
    print("Unregistered user, terminating the program.")
    exit()

TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

print("We have 3 texts to be analyzed.")

print(separator)

number_choice = input("Enter a number btw. 1 and 3 to select: ")
if not number_choice.isnumeric():
    print("Wrong choice")
    exit()
number_choice = int(number_choice)
if number_choice not in range(1, 4):
    print("Wrong choice")
    exit()

text_choice = (TEXTS [number_choice - 1]).split()

print(separator)

cleaned_words = list()
for word in text_choice:
    cleaned_words.append(word.strip(",.:;"))
print("There are", len(cleaned_words),  "words in the selected text.")


titlecase_words = list()
for word in cleaned_words:
    if word[0].isupper():
        titlecase_words.append(word)
print("There are", len(titlecase_words), "titlecase words.")


uppercase_words = list()
for word in cleaned_words:
    if word.isupper() and word.isalpha():
        uppercase_words.append(word)
print("There are", len(uppercase_words), "uppercase words.")


lowercase_words = list ()
for word in cleaned_words:
    if word.islower():
        lowercase_words.append(word)
print("There are", len(lowercase_words), "lowercase words.")


numeric = list ()
for word in cleaned_words:
    if word.isdigit():
        numeric.append(word)
print("There are", len(numeric), "numeric strings.")

sum_numeric = 0
for number in numeric:
    sum_numeric += int(number)
print("The sum of all the numbers ", sum_numeric, ".", sep="")


word_lengths = {}
word_frequency = {}
for word in cleaned_words:
    word_lengths[word] = len(word)
    word_length = len(word)
    word_frequency[word_length] = word_frequency.get(word_length, 0) + 1


print(separator)

print("|{} | {:^17} |{} |".format("LEN", "OCCURENCES", "NR."))

print(separator)

for key, value in sorted(word_frequency.items()):
    print("| {:^2} | {:17} | {:^2} |".format(key, "*" * value, value))

print(separator)