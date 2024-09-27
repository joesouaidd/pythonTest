Input= "wrw blf hvv ozhg mrtsg'h vkrhlwv?"
Output= ""


for i in Input:
    if i != " ":
        number = ord(i)-ord('a')
        Output +=  chr(ord('z') - number)

    else:
        Output += " "

print(Output)