sent = input("enter a sentence ")
po = sent
count  = 0
if "a" in po:
    count += 1

while(po != ""):
    po = input("enter a line ")
    for i in po:
        if i == "a":
            count += 1
    sent = sent +" "+ po
print(sent)
res = len(sent.split())
print("the number of words in sentences are", res)
print("the number of words that contain a are ", count)