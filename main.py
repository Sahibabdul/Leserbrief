from leserbrief import Leserbrief
import os
import logging

#Logging Config. 
logging.basicConfig(filename='debug.log', format='%(levelname)s | %(asctime)s:%(message)s',level=logging.DEBUG)

#Analyze Config
#Base URL atm it only works for this website but the Code could be adapted to other sites
base_url = "https://www.volksblatt.li/Leserbriefe"
#Bounds for Letters to analyze
amount_of_letters = 654932
lower_bound = 647504
logging.info("Upper bound:" +str(amount_of_letters)+" Lower bound:"+str(lower_bound))
list_of_letters=[]
#Looking at all letters already looked at
with open("text.txt","r") as articles:
    list_articles = articles.read().split("\n")
newest_letter_id = amount_of_letters
for article in reversed(list_articles):
    if " --- " in article:
        newest_letter_id = int(article.split(" --- ")[0])
        break
logging.info("Newest Letter id: "+str(newest_letter_id))

#--------Creator--------
#Actually Getting the letters from the site
#Writing it to the output file text.txt
with open("text.txt","a") as text:
    #Going from upperbound to Lower Bound
    for i in reversed(range(newest_letter_id)):
        if i < lower_bound:
            logging.debug("Exited with: "+str(i))
            exit()
        letter = Leserbrief(i)
        if letter.get_text()=="Error":
            logging.debug("Letter not available at: "+str(letter.id)+" | did not get any text")
        else:
            text.write( letter.id+" --- "+letter.get_title() + " --- "+ letter.get_creator()+" --- "+ letter.get_text()+"\n")
            logging.info("")
            print("Done with: "+str(letter.id))
