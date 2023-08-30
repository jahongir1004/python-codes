import random as r
words=["hello",
       "adequate",
       "adequately",
       "certainty",
       "cartoon",
       "movie"]
def shuffle():
    shuffle=[]
    word_lets="" 
    word=r.choice(words) 
    word_let=[] 
    
    for w in word:
        word_let.append(w)
    while word_let:
        a=r.choice(word_let)
        word_lets+=a
        word_let.remove(a)
    shuffle.append(word)
    shuffle.append(word_lets)    
    return shuffle
def play():
    s=shuffle()
    print(f"Computer generated a word!>>> {str(s[1])}")
    t=True
    while t:
        a=input("Find it>>>")
        if a==s[0]:
            
            t=False
        else:
            print("No")
            continue
    return True    
print(play())