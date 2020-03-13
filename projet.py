alphabet=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

import random
lettre = random.choice(alphabet)

#print(lettre)

score = 0

reponse = input('la lettre est '+lettre)
reponse = reponse.capitalize()

if reponse[0] == lettre:
    print("c'est bon")
    score =+ 1
else:
    print("c'est faux")
print(score)