import os

class Post():
    def __init__(self, id, title, creator, text):
        self.id = id
        self.creator = creator
        self.title = title
        self.text = text


if __name__ == "__main__":
    creators={}
    posts=[]
    with open("text.txt","r") as input:
        texts = input.read().split("\n")
        for lines in texts:
            line = lines.split(" --- ")
            posts=Post(line[0], line[1], line[2],line[3])

            if line[2].split()[0] not in creators.keys():
                creators[line[2].split()[0]] = [line[0]]
            else:
                creators[line[2].split()[0]] = creators[line[2].split()[0]].append(line[0])

    print(creators)