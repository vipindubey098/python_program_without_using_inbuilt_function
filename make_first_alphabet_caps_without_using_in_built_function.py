def firstCap(str_data):
    res = ""
    for char in str_data:
        if ord(char) >= 65 and ord(char) <=122:
            # Refer this link: https://www.smashingmagazine.com/2012/06/all-about-unicode-utf8-character-sets/
            # Finding the first alphabet
            if str_data.index(char) == 0:
                if ord(char) >= 65 and ord(char) <=90:
                    res += char
                    # print("i am on first Caps letter")
                elif ord(char) >= 97 and ord(char) <=122:
                    res += chr(ord(char)-32)
                    # print("i am on first small letter")
            else:
                if ord(char) >= 65 and ord(char) <=90:
                    res += chr(ord(char)+32)
                    # print("i am on second Caps letter")
                elif ord(char) >= 97 and ord(char) <=122:
                    # res += chr(ord(char)-32)
                    res += char
                    # print("i am on second small letter")
        else:
            print("alphabets only")
    return res

def FirstLetters(sentence):
    res = []
    letters = ""
    words = sentence.split()
    lengthwords = len(words)
    for index, value in enumerate(words):
        print(value)
        res += firstCap(value)+" "
    return(res)
print(FirstLetters('ThIs iS HeLLo'))
