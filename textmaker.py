import time,os,random

def clear():
    os.system('cls' if os.name=='nt' else 'clear')

def findOccurrences(s, ch):
    return [i for i, letter in enumerate(s) if letter == ch]

jumbler = "α!вΔǤҒʓ&ʏ@cǪƤ9#∂$ɛғ^ƬƧɢ-&н8*ι-(ʝƃƄƅCƇƞƟƠơ5σ<ρ>ƜѴզ4{ƘĴяƨƲЯЄ2{7}тʋ3}ʌ~ω1/6ϰѲИƖĦ@βƆƵ%ƁƂƋƈDƊ=κ+Ѧ˩0ℓ)м?иƳχƉ#ƗKƙƚƛWƝƌƍƎƏƐƑƒƓƔƕIƢƣPƥƦSsƩƪƫTƭƮƯưƱUYƴZƶƷƸ"

sentence = input()
newlines = findOccurrences(sentence,'\n')
clear()
list_sentence = list(sentence)
spaced_sentence = ' '.join(sentence)
count = 0
random_count = random.randint(4,8)
word = []
final = ""
xtimes = 1

# Manipulate render speed and refresh rate here
render_speed = 1             # [1.00 - 5.00]                
refresh_rate = 1              # [0.25 - 5.00]

while(final != spaced_sentence):
    if(count == random_count):
        if(len(sentence) <= 35):
            xtimes = 1
        else:
            xtimes += int(count-count/render_speed) 
        random_count += random.randint(1,3)
        for i in range(0,xtimes):
            temp = random.randint(0,len(list_sentence)-1)
            small_count = 0
            while(temp in word):
                small_count += 1
                temp = random.randint(0,len(list_sentence)-1)
                if(small_count > 100):
                    break
            word.append(temp)
        
    final = ""
    for j in range(0,len(sentence)):
        final += jumbler[random.randint(0,len(jumbler)-1)]
    final = list(final)
    for k in range(0,len(word)):
        final[word[k]] = list_sentence[word[k]]
    for j in range(0,len(newlines)):
        final[newlines[j]] = '\n'
    final = ''.join(final)
    print(final)
    time.sleep(0.075/refresh_rate) 
    clear()
    count += 1
    # print(final,spaced_sentence)
    if(final == sentence):
        break

print(sentence)
