import os
from multi_rake import Rake
import csv

class Letter:
    def __init__(self, author, ID, text):
        self.author = author
        self.ID = [ID]
        self.text = [text]
        self.keywords = ""

    def getID(self):
        return self.ID

    def getAuthor(self):
        return self.author
    
    def getText(self):
        return " ".join(self.text)
    
    def appendText(self, text, id):
        self.text.append(text)
        self.ID.append(id)

    def setKeywords(self, x):
        self.keywords = x

    def getKeywords(self):
        return self.keywords

    def __str__(self):
        return str(self.author) + str(self.text) + str(self.keywords)


letters = {}
authors = []

with open("ovezulax_Leserbriefe030622.csv", "r", encoding="utf-8") as reader:
    csv_reader = csv.reader(reader)
    for row in csv_reader:
        auth = row[2].split(",")[0].replace("*", "Star")
        while auth.startswith(" "):
            auth = auth [1:]
        for writ in authors:
            if auth.startswith(writ) and len(auth) > 5 and writ != "":
                auth = writ
                break
        if auth in authors:
            letters[auth].appendText(row[4], row[0])
        else:   
            authors.append(auth)
            letters[auth] = Letter(auth, row[0], row[4])



rake = Rake()

counter = 0
for letter in letters.values():
    counter += 1
    buffer = rake.apply(letter.getText())
    out = []
    for item in buffer:
        out.append(item[0])
    letter.setKeywords(out)


for key in letters.keys():
    print(str(letters[key].getAuthor()))
    if len(str(letters[key].getAuthor())) == 0:
        with open("keywords/" + "Letter " + " s/" + str(letters[key].getAuthor().replace("/", "")) + ".txt", "w", encoding="utf-8") as writer:
            letter = letters[key]
            writer.write("Author: " + str(letter.getAuthor()) + " | IDs: " + str(letter.getID()) +  " | keywords: " + str(letter.getKeywords()) + "\n")

    else:    
        with open("keywords/"+ "Letter " + str(letters[key].getAuthor().replace("/", ""))[0].lower() +" s/"+str(letters[key].getAuthor().replace("/", ""))+".txt", "w", encoding="utf-8") as writer:
            letter = letters[key]
            writer.write("Author: " + str(letter.getAuthor()) + " | IDs: " + str(letter.getID()) +  " | keywords: " + str(letter.getKeywords()) + "\n")

with open("keywords.txt", "w", encoding="utf-8") as writer:
    for letter in letters.values():
        writer.write("Author: " + str(letter.getAuthor()) + " | IDs: " + str(letter.getID()) +  " | keywords: " + str(letter.getKeywords()[:20]) + "\n")