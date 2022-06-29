message = 'Ta _7N6DDDhlg:W3D_H3C31N__0D3ef sHR053F38N43D0F i33___NA'

LengthMessage = len(message)+1

NewMessage = ''
Line = 0
AB = True
lenNewMessage = len(NewMessage)
for pos, i in enumerate(message):

    if lenNewMessage == 0:
        NewMessage += Line*'-'
    
    lenNewMessage = len(NewMessage)- Line*LengthMessage

    if Line == 0 or Line == 3:
        progress = '-'*(5)  
    else:    
        if AB:
            progress = '-'*(5-Line*2)   
        else:
            progress = '-'*(Line*2-1)

    if lenNewMessage + len(progress)+1 < LengthMessage:
        NewMessage += i+progress
        AB = not AB
    elif lenNewMessage + len(progress) +1 == LengthMessage:
        print(pos)
        NewMessage += i+progress+ '\n'
        Line += 1
        AB = True
        lenNewMessage = len(NewMessage) - (Line*LengthMessage+1)
    elif lenNewMessage < LengthMessage:
        NewMessage += i+'-'*(LengthMessage-lenNewMessage-1) + '\n'
        Line += 1
        AB = True
        lenNewMessage = len(NewMessage) - (Line*LengthMessage+1)
    else:
        print('error')

print(NewMessage)
