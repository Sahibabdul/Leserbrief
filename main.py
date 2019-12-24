from leserbrief import Leserbrief
import os

text = open("text.txt", "w")
authors = open("authors.txt", "w")
title = open("title.txt", "w")
text.write("")
authors.write("")
title.write("")
text.close()
authors.close()
title.close()

base_url = "https://www.volksblatt.li/Leserbriefe"
amount_of_letters = 647505
list_of_letters=[]
blacklist = open("blacklist.txt","r")
list_black = set(blacklist.read().split())
blacklist.close()
newest_letter_id = list_black[-1]


#--------Creator--------
text = open("text.txt", "a")
blacklist = open("blacklist.txt", "a")
authors = open("authors.txt", "a")
title = open("title.txt", "a")
for i in range(amount_of_letters):
    if str(newest_letter_id-i) not in list_black:
        letter=Leserbrief(newest_letter_id-i)
    else:
        continue
    print(letter.id)
    if letter.get_text()=="Error":
        blacklist.write(letter.id+"\n")
        print("Fail")
    else:
        text.write( letter.id+" --- "+letter.get_text()+"\n")
        authors.write(letter.id+" --- "+ letter.get_creator()+"\n")
        title.write(letter.id+" --- "+ letter.get_title()+"\n")
    
text.close()
blacklist.close()
authors.close()
title.close()
