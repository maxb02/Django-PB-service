#рус текст не принимается

def coder(text):
    numcode=[]
    a=range(65,91)
    b=range(91,123)
    charcode=[]
    c=''
    for i in text:
        if ord(i) in a:
            if ord(i)> 89:
                numcode.append(ord(i)-24)
            else:
                numcode.append(ord(i)+2)
        elif ord(i) in b:
            if ord(i)>120:
                numcode.append(ord(i) - 24)
            else:
                numcode.append(ord(i) + 2)
        else:
            numcode.append(ord(i))
    for i in numcode:
        charcode.append(chr(i))

    return c.join(charcode)

print (coder('HR-interview aAzZ'))

