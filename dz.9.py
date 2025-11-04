# 1
class Atbash:
    alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"

    def __init__(self):
        lowercase_code = {x: y for x, y in zip(self.alphabet, self.alphabet[::-1])}
        uppercase_code = {x.upper(): y.upper() for x, y in zip(self.alphabet, self.alphabet[::-1])}
        self._encode = lowercase_code
        self._encode.update(uppercase_code)

    def encode(self, text):
        return ''.join([self._encode.get(char, char) for char in text])


cipher1 = Atbash()
line = input()
while line != '.':
    print(cipher1.encode(line))
    line = input()




# 2
class Caesar:
    alphabet = "яюэьыъщшчцхфутсрпонмлкйизжёедгвба"

    def __init__(self, key):
        self._encode = dict()
        for i in range(len(self.alphabet)):
            letter = self.alphabet[i]
            encoded = self.alphabet[(i + key) % len(self.alphabet)]
            self._encode[letter] = encoded
            self._encode[letter.upper()] = encoded.upper()
        self._decode = dict()
        for i in range(len(self.alphabet)):
            letter = self.alphabet[i]
            encoded = self.alphabet[(i - key) % len(self.alphabet)]
            self._decode[letter] = encoded
            self._decode[letter.upper()] = encoded.upper() # TODO

    def encode(self, text):
        return ''.join([self._encode.get(char, char) for char in text])

    def decode(self, line):
        return ''.join([self._decode.get(char, char) for char in line])


key = int(input('Ээъыцмъ фубз:'))
cipher = Caesar(key)
line = input()
while line:
    print(cipher.decode(line))
    line = input()




# 3.1
abc = [3,21,9,19,13,2,33,25,20,4,23,11,10,12,5,1,14,8,7,6,15,31,24,28,22,26,29,32,17,18,30,27,16]
s = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
d = []
for i in range(33):
    d.append((abc[i], s[i]))
d = sorted(d)
print(d)
import random

class Monoalphabet:
    alphabet = [i for i in 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя']  # TODO

    def __init__(self, keytable):
        lowercase_code = {x: y for x, y in zip(self.alphabet, keytable)}
        uppercase_code = {x.upper(): y.upper() for x, y in zip(self.alphabet, keytable)}
        self._encode = lowercase_code
        self._encode.update(uppercase_code)
        self._decode = {}  # TODO

    def encode(self, text):
        return ''.join([self._encode.get(char, char) for char in text])

    def decode(self, line):
        s = ''
        r = ''
        y = []
        d1 = []
        for i in line:
            if i != " ":
                s+=i
        for i in 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя':
            k = s.count(i)/len(s)
            d1.append((k,i))
        d1 = sorted(d1, reverse=True)
        print(d1)
        print(d1[11],d[11])
        for i in line:
            i = i.lower()
            for j in range(33):
                if d1[j][1] == i:
                    r += d[j][1]
                    break
            if i == " ":
                r+=i
        return r
key = Monoalphabet.alphabet[:]
random.shuffle(key)
cipher = Monoalphabet(key)
line = "Егпж Огнщющжэ (ацягэяпэогбюцы йэсщюз) Мэяхющыегс ажцмцянщюгщс егпжцо ажцшбцы йэсщюз иояищбши сюцрцэяпэогбюзщ егпжз. Эьт Эях-Чгюмг о шоцгв жэьцбэв ацчэйэя, лбц цьзлюзщ сцюцэяпэогбюзщ егпжз мцоцяхюц-бэчг ажцшбц ацммэфбши лэшбцбюцст чжгабцэюэягйт г ащжозс ажщмяцнгя гшацяхйцоэбх сюцрцэяпэогбюзщ егпжз. О Щожцащ бэчгщ егпжз ьзяг оащжозщ цагшэюз о 1467 рцмт гбэяхиюшчгс эжвгбщчбцжцс Ящцю Ьэббгшбэ Эяхьщжбг. О XVI ощчщ ющсщёчгы эььэб Гцрэюю Бжгбщсгы о шоцщы чюгрщ “Шбщюцржэпги” ажщмшбэогя швщст ацягэяпэогбюцрц егпжцоэюги о огмщ бэьягёз. Ьцящщ шяцнюзы оэжгэюб ш гшацяхйцоэюгщс шсщеэююзв эяпэогбцо ьзя цагшэю о 1563 рцмт Мнэсьэббгшбэ мщяяэ Ацжбэ о щрц чюгрщ “Ажц шчжзбтф йюэлгсцшбх цбмщяхюзв ьтчо”. Ацшящмюгс шяцоцс о жэйогбгг ацягэяпэогбюзв егпжцо сцнюц шлгбэбх жцбцжюзщ сэегюз, ажгсщжцс чцбцжцы сцнюц шлгбэбх ющсщёчтф сэегют Enigma, жэйжэьцбэююэи о 1917 р. Штбх ацягэяпэогбюзв егпжцо йэчяфлщюэ о сюцрцчжэбюцс ажгсщющюгг жэйяглюзв егпжцо ажцшбцы йэсщюз ч цажщмщящююцст лгшят ьтчо егпжтщсцрц бщчшбэ. Бц щшбх ч чэнмцы ьтчощ ац цбмщяхюцшбг ажгсщюищбши цмгю гй егпжцо ажцшбцы йэсщюз.Егпж Огнщющжэ шцшбцгб гй ацшящмцоэбщяхюцшбг ющшчцяхчгв егпжцо Ёщйэжи ш жэйяглюзсг йюэлщюгисг шмогрэ. Мяи йэегпжцозоэюги сцнщб гшацяхйцоэбхши бэьягёэ эяпэогбцо, юэйзоэщсэи чоэмжэб (бэьягёэ) Огнщющжэ. Ажгсщюгбщяхюц ч жтшшчцст эяпэогбт бэьягёэ Огнщющжэ шцшбэояищбши гй шбжцч ац 33 шгсоцяцо, ажглдс чэнмэи шящмтфъэи шбжцчэ шмогрэщбши юэ ющшчцяхчц ацйгёгы. Бэчгс цьжэйцс, о бэьягёщ ацятлэщбши 33 жэйяглюзв егпжцо Ёщйэжи. Юэ жэйюзв кбэаэв чцмгжцочг егпж Огнщющжэ гшацяхйтщб жэйяглюзщ эяпэогбз гй кбцы бэьягёз. Юэ чэнмцс кбэащ егпжцоэюги гшацяхйтфбши жэйяглюзщ эяпэогбз, озьгжэщсзщ о йэогшгсцшбг цб шгсоцяэ чяфлщоцрц шяцоэ. Юэажгсщж, щшяг чяфлщоцщ шяцоц “ШЭБ”, бц ащжоэи ьтчоэ цбчжзбцрц бщчшбэ егпжтщбши ш гшацяхйцоэюгщс эяпэогбэ “Ш’, обцжэи “Э”, бжщбхи “Б”, лщбоджбэи шюцоэ “Ш” г бэч мэящщ.Ажцржэссэ егпжцоэюги егпжцс Огнщющжэ: Ацшящмюгы жэймщя жэьцбз йэегпжцоэю егпжцс Огнщющжэ ш ющгйощшбюзс чцмцозс шяцоцс. Ацмшчэйчэ мяи шэсзв шбцычгв чжгабцэюэягбгчцо: мягюэ чцмцоцрц шяцоэ 8."

while line:
    print(cipher.decode(line))
    line = input()



# 3.2
import random


class Monoalphabet:
    alphabet = [i for i in 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя']  # TODO

    def __init__(self, keytable):
        lowercase_code = {x: y for x, y in zip(self.alphabet, keytable)}
        uppercase_code = {x.upper(): y.upper() for x, y in zip(self.alphabet, keytable)}
        self._encode = lowercase_code
        self._encode.update(uppercase_code)
        self._decode = {}  # TODO

    def encode(self, text):
        return ''.join([self._encode.get(char, char) for char in text])

    def decode(self, line):
        a = "егпжонщюэбэчмячыцилдшарсйзвьёктфхw"
        b = "шифрвженатакдльйоячёспгмзыxбцэуюьw"
        r = ''
        for i in line:
            for j in range(len(a)):
                if i.lower() == a[j]:
                    r+=b[j]
                    break
            if i.lower() not in a:
                r+=i
        return r
key = Monoalphabet.alphabet[:]
random.shuffle(key)
cipher = Monoalphabet(key)
line = "Мэяхющыегс ажцмцянщюгщс егпжцо ажцшбцы йэсщюз иояищбши сюцрцэяпэогбюзщ егпжз. Эьт Эях-Чгюмг о шоцгв жэьцбэв ацчэйэя, лбц цьзлюзщ сцюцэяпэогбюзщ егпжз мцоцяхюц-бэчг ажцшбц ацммэфбши лэшбцбюцст чжгабцэюэягйт г ащжозс ажщмяцнгя гшацяхйцоэбх сюцрцэяпэогбюзщ егпжз. О Щожцащ бэчгщ егпжз ьзяг оащжозщ цагшэюз о 1467 рцмт гбэяхиюшчгс эжвгбщчбцжцс Ящцю Ьэббгшбэ Эяхьщжбг. О XVI ощчщ ющсщёчгы эььэб Гцрэюю Бжгбщсгы о шоцщы чюгрщ “Шбщюцржэпги” ажщмшбэогя швщст ацягэяпэогбюцрц егпжцоэюги о огмщ бэьягёз. Ьцящщ шяцнюзы оэжгэюб ш гшацяхйцоэюгщс шсщеэююзв эяпэогбцо ьзя цагшэю о 1563 рцмт Мнэсьэббгшбэ мщяяэ Ацжбэ о щрц чюгрщ “Ажц шчжзбтф йюэлгсцшбх цбмщяхюзв ьтчо”. Ацшящмюгс шяцоцс о жэйогбгг ацягэяпэогбюзв егпжцо сцнюц шлгбэбх жцбцжюзщ сэегюз, ажгсщжцс чцбцжцы сцнюц шлгбэбх ющсщёчтф сэегют Enigma, жэйжэьцбэююэи о 1917 р. Штбх ацягэяпэогбюзв егпжцо йэчяфлщюэ о сюцрцчжэбюцс ажгсщющюгг жэйяглюзв егпжцо ажцшбцы йэсщюз ч цажщмщящююцст лгшят ьтчо егпжтщсцрц бщчшбэ. Бц щшбх ч чэнмцы ьтчощ ац цбмщяхюцшбг ажгсщюищбши цмгю гй егпжцо ажцшбцы йэсщюз.Егпж Огнщющжэ шцшбцгб гй ацшящмцоэбщяхюцшбг ющшчцяхчгв егпжцо Ёщйэжи ш жэйяглюзсг йюэлщюгисг шмогрэ. Мяи йэегпжцозоэюги сцнщб гшацяхйцоэбхши бэьягёэ эяпэогбцо, юэйзоэщсэи чоэмжэб (бэьягёэ) Огнщющжэ. Ажгсщюгбщяхюц ч жтшшчцст эяпэогбт бэьягёэ Огнщющжэ шцшбэояищбши гй шбжцч ац 33 шгсоцяцо, ажглдс чэнмэи шящмтфъэи шбжцчэ шмогрэщбши юэ ющшчцяхчц ацйгёгы. Бэчгс цьжэйцс, о бэьягёщ ацятлэщбши 33 жэйяглюзв егпжцо Ёщйэжи. Юэ жэйюзв кбэаэв чцмгжцочг егпж Огнщющжэ гшацяхйтщб жэйяглюзщ эяпэогбз гй кбцы бэьягёз. Юэ чэнмцс кбэащ егпжцоэюги гшацяхйтфбши жэйяглюзщ эяпэогбз, озьгжэщсзщ о йэогшгсцшбг цб шгсоцяэ чяфлщоцрц шяцоэ. Юэажгсщж, щшяг чяфлщоцщ шяцоц “ШЭБ”, бц ащжоэи ьтчоэ цбчжзбцрц бщчшбэ егпжтщбши ш гшацяхйцоэюгщс эяпэогбэ “Ш’, обцжэи “Э”, бжщбхи “Б”, лщбоджбэи шюцоэ “Ш” г бэч мэящщ."
while line:
    print(cipher.decode(line))
    line = input()



# 4
class Vigenere:
    alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"

    def __init__(self, keyword):
        self.alphaindex = {ch: index for index, ch in enumerate(self.alphabet)}
        self.key = [self.alphaindex[letter] for letter in keyword.lower()]

    def caesar(self, letter, shift, encode=True):
        if letter in self.alphaindex:  # строчная буква
            if encode:
                index = (self.alphaindex[letter] + shift) % len(self.alphabet)
            else:
                index = (self.alphaindex[letter] - shift) % len(self.alphabet)
            cipherletter = self.alphabet[index]
        elif letter.lower() in self.alphaindex:  # прописная буква
            cipherletter = self.caesar(letter.lower(), shift, encode).upper()
        else:
            cipherletter = letter
        return cipherletter

    def encode(self, line):
        ciphertext = []
        for i, letter in enumerate(line):
            shift = self.key[i % len(self.key)]
            cipherletter = self.caesar(letter, shift, encode=True)
            ciphertext.append(cipherletter)
        return ''.join(ciphertext)

    def decode(self, line):
        plaintext = []
        k = 0
        for i, letter in enumerate(line):
            if letter not in "абвгдеёжзийклмнопрстуфхцчшщъыьэюя":
                plaintext.append(letter)
            else:
                shift = self.key[k % len(self.key)]
                cipherletter = self.caesar(letter, shift, encode=False)
                plaintext.append(cipherletter)
                k += 1
        return ''.join(plaintext)


keyword = "мфти"
cipher = Vigenere(keyword)
decoded = cipher.decode("йвылщф ыцящгнюзрвхщдз щгхья дбахжтыи дгч эщтфхьтяхт дфыыачпг вчшэтфбффсявблы мыээф -- эчщдожящгцат ячрщюе еэжщм саспбн. ёшщянъжн хсжбмыц ксбебкмвыз, хёвчшръчоффбхйдз о бтбхвтю йжбт ющгсх, эдшыаоратеъл шб ъхй вчэ.")

print(f"Расшифрованный: {decoded}")
