var1 = "This is python data"
find = "is"
splitdata = var1.split(" ")
for i,v in enumerate(splitdata):
    if v == find:
        print('We found the word "',str(v),'" at',str(i),'place of the word')