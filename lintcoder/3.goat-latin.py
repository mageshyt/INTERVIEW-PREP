import sys
def latinConversion(s):
    """
        this function used to conver the sentence to latin conversion
    """
    n=len(s)
    words=s.split() # get all the words in sentence
    res=[]
    
    for idx,word in enumerate(words):
        goated_word=word
        # if start letter is vowel add 'ma'
        if is_vowel(word[0]):
            goated_word+='ma'
        else:
            # if not vowel add the first letter to end and add 'ma'
            goated_word=word[i:]+word[0]+'ma'
        
        # add 'a'
        goated_word+='a' * (idx+1)
        
        res.append(goated_word)
            
    
    return ' '.join(res)
    

def is_vowel(char):
    """
    this function used to check if the char is vowel or not
    """
    
    return char.lower() in 'aeiou'
    
s = input()    
print(latinConversion(s))
