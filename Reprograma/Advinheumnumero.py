#Advinhe um número
#Neste programa, você precisa definir um número entre 1 e 100 e pedir para o usuário tentar acertar. 
#Você vai dizer se a pessoa acertou, chutou muito alto ou chutou muito baixo. Diga qual o numero
 
numero = int(input("Boa tarde! Nosso sistema definiu um número, entre 0 e 100 e, por gentileza, solicito que tente acertar qual é o mesmo:"))
''' O número definido foi 50'''
if numero == 50:
    print("Parábens, você acertou!")
elif numero >= 0 and numero < 50:
    print("Quaaase! Você chutou baixo, o número correto é 50 :)")
elif numero > 50 and numero < 100:
    print("Eitaaa! Quase, você chutou alto. O número correto é 50 :)")
else:
    print("Por favor, digite um número entre 0 e 100.")
