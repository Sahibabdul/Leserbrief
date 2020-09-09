from leserbrief import Leserbrief

from urllib.request import urlopen
from html.parser import HTMLParser
from urllib import parse
from bs4 import BeautifulSoup
import logging
import os
import logging

#Logging Config. 
logging.basicConfig(filename='debug.log', format='%(levelname)s | %(asctime)s:%(message)s',level=logging.DEBUG)

#Analyze Config
#Base URL atm it only works for this website but the Code could be adapted to other sites
base_url = "https://www.volksblatt.li/Leserbriefe"

starting_page = urlopen(base_url)
response = urlopen(base_url)
if 'text/html' in response.getheader('Content-Type'):
    html_bytes = response.read()
    html_string = html_bytes.decode("utf-8")
soup = BeautifulSoup(html_string, features="html.parser")
base_id = str(soup.find({"id": "body_repLeserbriefe_aLink_0"}))

#Bounds for Letters to analyze
amount_of_letters = 663621
lower_bound = 654932
print("starting now")
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
Print("done")
