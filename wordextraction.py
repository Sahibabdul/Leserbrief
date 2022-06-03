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

with open("ovezulax_Leserbriefe.csv", "r", encoding="utf-8") as reader:
    csv_reader = csv.reader(reader)
    for row in csv_reader:
        if row[2].split(",")[0].replace(" ", "") in authors:
            letters[row[2].split(",")[0].replace(" ", "")].appendText(row[4], row[0])
        else:   
            authors.append(row[2].split(",")[0].replace(" ", ""))
            letters[row[2].split(",")[0].replace(" ", "")] = Letter(row[2].split(",")[0].replace(" ", ""), row[0], row[4])

rake = Rake()

counter = 0
for letter in letters.values():
    print(str(counter))
    counter += 1
    buffer = rake.apply(letter.getText())
    out = []
    for item in buffer:
        out.append(item[0])
    letter.setKeywords(out)


for key in letters.keys():
    with open("keywords/"+str(letters[key].getAuthor().replace("/", ""))+".txt", "w", encoding="utf-8") as writer:
        letter = letters[key]
        writer.write("Author: " + str(letter.getAuthor()) + " | IDs: " + str(letter.getID()) +  " | keywords: " + str(letter.getKeywords()) + "\n")