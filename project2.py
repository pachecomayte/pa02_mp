# Mayte Pacheco, 05/06/17

def isPangram (sentence):
        alphabet= "abcdefghijklmnopqrstuvwxyz"
        sentence.lower()
        for ch in alphabet:
                if ch not in sentence:
                        return False
                else:
                        return True



def isPalindrome(text):
       word1 = text.lower()
       word2 = word1.replace(" ","").replace(",","").replace(".","").replace("?","").replace("!","").replace("'","").replace(":","").replace(";", "")
       reversetext = word2 [::-1]
       if word2 == reversetext:
              return True
       else:
              return False



def findVowel(text):
    text= list(text)
    vowel=['a','e','i','o']
    cons= ['b','c','d','f','g', 'h','j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's','t', 'v', 'w', 'x', 'z']
    if ('u') in text:
            if ('q') in text and text.index('u') == text.index('q') + 1:
                cons.append('u')
            else:
                vowel.append('u')
    else:
            vowel = vowel
            cons = cons

    if ('y') in text:
            if text.index('y') == 0:
                cons.append('y')
            else:
                vowel.append('y')
    else:
            vowel= vowel
            cons=cons
    for i in text:
            if i in vowel:
                p= text.index(i)
                q= text[p:]+text [:p] + ['ay']
                final = ''.join(q)
                return (final)




def firstVowel (text):
    text=list(text)
    vowel=['a','e','i','o','u']
    if text [0] in vowel:
        new= text +['way']
        newText = ''.join(new)
        return(newText)
    else:
        return(findVowel(text))


def pigWord (text):
    for i in text:
        if text == text.upper():
            low= text.lower()
            a=firstVowel(low)
            return a.upper()
        elif text[0]== text[0].upper():
            low1=text.lower()
            p=firstVowel(low1)
            w=p[0].upper() + p[1:]
            return (w)
        if text== text.lower():
            return (firstVowel(text))
        else:
            return (text)

def pigLatin (text):
    text=text.split(' ')
    nonalpha= ('!,?,:')

    s=''
    for i in text:
        if i.isalpha():
            s+= pigWord(i)
        else:
            s += pigWord(i)
        s += ' '
    s= s[:-1]
    return s
