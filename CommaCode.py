def list_to_string(list):
    if len(list) == 1:
        return list[0]
    return "{}, and {}".format(", ".join(list[:-1]), list[-1])

spam = ["apples", "bananas", "tofu", "cats"]
print(list_to_string(spam))


#def getList(list):
#    value = ''
#    for i in range(len(list)):
#        if i == len(list) - 1: # the last index in the list
#            value += 'and '+list[i]
###    return value
#
#spam = ['apples', 'bananas', 'tofu', 'cats']

#print(getList(spam))
