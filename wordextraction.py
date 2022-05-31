from multi_rake import Rake
import pandas as pd

df = pd.read_csv("ovezulax_Leserbriefe.csv")
text = list(df["textteil"])
ids = list(df["id"])

rake = Rake()

with open("keywords.txt", "w", encoding="utf-8") as writer:
    for line in range(len(text)):
        keywords = rake.apply(text[line])
        writer.write("ID: " + str(ids[line]) + " | "+ str(keywords[:10])+"\n")