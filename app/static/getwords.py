""" with open("app/static/seven_letter_words.txt",'r') as reader:
    words = set()
    lines = reader.readlines()
    for line in lines:
        words.add(line.strip())
    print(str(words))

with open("app/static/seven_letter_words.py", 'w') as writer:
    writer.write("seven_letter_words = " + str(words)) """

from seven_letter_words import seven_letter_words

print(seven_letter_words)