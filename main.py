from leserbrief import Leserbrief
import os

base_url = "https://www.volksblatt.li/Leserbriefe"
amount_of_letters = 653371
lower_bound = 647504
list_of_letters=[]
with open("text.txt","r") as articles:
    list_articles = articles.read().split("\n")
newest_letter_id = amount_of_letters
for article in reversed(list_articles):
    if " --- " in article:
        newest_letter_id = int(article.split(" --- ")[0])
        break


#--------Creator--------
with open("text.txt","a") as text:
    for i in reversed(range(newest_letter_id)):
        if i < lower_bound:
            exit()
        letter = Leserbrief(i)
        if letter.get_text()=="Error":
            print("Fail " + letter.id)
        else:
            text.write( letter.id+" --- "+letter.get_title() + " --- "+ letter.get_creator()+" --- "+ letter.get_text()+"\n")
            print("Success " + letter.id)
