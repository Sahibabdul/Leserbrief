from multi_rake import Rake
import pandas as pd

df = pd.read_csv("ovezulax_Leserbriefe.csv")
text = list(df["textteil"])

rake = Rake()

with open("keywords.txt", "w", encoding="utf-8") as writer:
    for line in text:
        keywords = rake.apply(line)
        writer.write(str(keywords[:10])+"\n")
with open("keywords.txt", "r", encoding="utf-8") as reader:
    lines = "\n".join(reader.readlines())
    print(rake.apply(lines))