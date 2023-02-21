def replace(source, find, replacing):
    result = ''
    i, j = 0, 0
    while i < len(source) - len(find):
        print(len(source)-len(find))
        # print(len(find))
        # print(source[i:i+len(find)])
        # print(i+len(find))
        # print(i)
        # print(i+len(find))
        if source[i:i+len(find)] == find:
            # print(j)
            # print(i)
            # print(source[j:i])
            
            print(source[j:i])
            print(replacing)
            result += source[j:i] + replacing
            print(result)
            i += len(find)
            j = i
        else:
            i += 1
    print(source[j:])
    result += source[j:]
    print(result)
    return result
    
# print(replace('To be or not to be, this is the question!', 'question', 'code'))
print(replace("Don't play without your friends", "with", "by"))

# def replace(s, s1, s2):
#     tokens = s2.split()
#     if s in tokens:
#         tokens[tokens.index(s)] = s1
#     return ' '.join(tokens)
# print(replace("with", "by" , "Don't play with out your friends"))
    
