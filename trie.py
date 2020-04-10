headmain={}

def add(word):
    head=headmain
    for ch in word:
        if ch not in head:
            head[ch]={}
        head=head[ch]
    head['*']=True

def search(word):
    cur=headmain

    for ch in word:
        if ch not in cur:
            return False
        cur=cur[ch]
    if '*' in cur:
        return True
    else:
        return False

add("hello")
add('hell')
add('hey')
print(headmain)
{'h': {'e': {'l': {'l': {'o': {'*': True}, '*': True}}, 'y': {'*': True}}}}