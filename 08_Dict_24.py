x = {'2':'a','22':'b','222':'c','3':'d','33':'e','333':'f','4':'g','44':'h',\
     '444':'i','5':'j','55':'k','555':'l','6':'m','66':'n','666':'o','7':'p',\
     '77':'q','777':'r','7777':'s','8':'t','88':'u','888':'v','9':'w','99':'x',\
     '999':'y','9999':'z','0':' '}
y = {}
for key in x : y[x[key]] = key
def text2keys(text) :
    t = text.lower()
    x = ""
    z = ""
    for e in t :
        if e in 'abcdefghijklmnopqrstuvwxyz ' : x += e
    for e in x : z += y[e]+" "
    return z.strip()
def keys2text(keys):
    z = ""
    k = keys.split()
    for i in range(len(k)) : z += x[k[i]]
    return z
print(text2keys("I am busy."))
print(keys2text("444 0 2 6 0 22 88 7777 999"))