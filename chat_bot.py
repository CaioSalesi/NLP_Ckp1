while True:
    frase = input("Digite uma frase: ").lower()
    frase = frase.split()
    pontuacaoPos = 0
    pontuacaoNeg = 0
    pontuacaoNeu = 0

    #import das listas
    with open("positivas.txt", "r", encoding="utf-8") as arquivo:
        positivas = arquivo.readlines()
    positivas = [x[:-1] for x in positivas]
    with open("negativas.txt", "r", encoding="utf-8") as arquivo:
        negativas = arquivo.readlines()
    negativas = [x[:-1] for x in negativas]
    for i in frase:
        palavraAnterior = frase[frase.index(i)-1]
        
        if i in positivas: #verificador de positivas
            if palavraAnterior == 'não':
                pontuacaoNeg +=1
            else:
                pontuacaoPos += 1
                
        elif i in negativas: #verificador de negativas
            if palavraAnterior == 'não':
                pontuacaoNeu +=1
            else:
                pontuacaoNeg += 1
        else:
            pontuacaoNeu += 1
            
    #print("Positivas:", pontuacaoPos)
    #print("Negativas:", pontuacaoNeg)
    #print("Neutras: ", pontuacaoNeu)

    if pontuacaoPos > pontuacaoNeg:
        print("A sua frase é positiva")
    elif pontuacaoNeg > pontuacaoPos:
        print("A sua frase e negativa")
    else:
        print("Não sabemos, perdão")

    continuar = input("Se deseja sair digite '0': ")
    if continuar == '0':
        break
