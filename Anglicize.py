# ### 1. Conditionals

def convert_time(a):
    if len(a) ==1:
        return a[0]
    elif len(a) ==2:
        return a[1]+(a[0]*60)
    elif len(a) ==3:
        return a[2]+(a[1]*60)+(a[0]*60*60)
    elif len(a) ==4:
        return a[3]+(a[2]*60)+(a[1]*60*60)+(a[0]*60*60*24)


# ### 2. Testing

def last_name_first(n):
    
    end_first = n.find(' ')
    first = n[:end_first]
    last  = n[end_first+1:].strip()
    return last+', '+first


# ### 3. Control Flow

def sortnum(a):
    b=[]
    if (a[0] < a[1]):
        if (a[0] < a[2]):
            if (a[1] < a[2]):
                b.extend([a[0],a[1],a[2]])
            else:
                b.extend([a[0],a[2],a[1]])
        else:
            b.extend([a[2],a[0],a[1]])
    else:
        if (a[1] < a[2]):
            if (a[0] < a[2]):
                b.extend([a[1],a[0],a[2]])
            else:
                b.extend([a[1],a[2],a[0]])
        else:
            b.extend([a[2],a[1],a[0]])
    return b


# ### 4. Challenge

def anglicize1to19(n):
    if n == 1:
        return "one"
    elif n == 2:
        return "two"
    elif n == 3:
        return "three"
    elif n == 4:
        return "four"
    elif n == 5:
        return "five"
    elif n == 5:
        return "five"
    elif n == 6:
        return "six"
    elif n == 7:
        return "seven"
    elif n == 8:
        return "eight"
    elif n == 9:
        return "nine"
    elif n == 10:
        return "ten"
    elif n == 11:
        return "eleven"
    elif n == 12:
        return "twelve"
    elif n == 13:
        return "thirteen"
    elif n == 14:
        return "fourteen"
    elif n == 15:
        return "fifteen"
    elif n == 16:
        return "sixteen"
    elif n == 17:
        return "seventeen"
    elif n == 18:
        return "eighteen"
    return "ninteen"

def tens(n):
    if n == 20:
        return "twenty"
    elif n == 30:
        return "thirty"
    elif n == 40:
        return "fourty"
    elif n == 50:
        return "fifty"
    elif n == 60:
        return "sixty"
    elif n == 70:
        return "seventy"
    elif n == 80:
        return "eighty"
    return "ninety"

def anglicize20to99(n):
    return  tens((n//10)*10) + " " + anglicize1to19(n%10)

def anglicize100to999(n):   
    hundreds = n % 100     
    suffix = ''
    if hundreds == 0:
        suffix = ''
    elif hundreds < 20:
        suffix = " " + anglicize1to19(hundreds)
    elif hundreds == 20 or hundreds == 30 or hundreds == 40 or hundreds == 50 or hundreds == 60 or hundreds == 70 or hundreds == 80 or hundreds == 90 :
        suffix = " " + tens(hundreds)
    else:
        suffix = " " +anglicize20to99(hundreds)
    return anglicize1to19(n//100) + ' hundred' + suffix


def anglicize(n):
    if n==0:
        return 'zero'
    elif 0<n<20:
        return anglicize1to19(n)
    elif n == 20 or n == 30 or n == 40 or n == 50 or n == 60 or n == 70 or n == 80 or n == 90:
        return tens(n)
    elif 20<n<100:
        return anglicize20to99(n)
    elif 100<n<1000:
        return anglicize100to999(n)
