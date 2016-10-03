def Output(Texto):
    print(Texto)
def Tamanho(Texto):
    TamanhoTexto = len(Texto)
    return TamanhoTexto
def Maiusculo(Texto):
    MaiusculoTexto = Texto.upper()
    return MaiusculoTexto
def Minusculo(Texto):
    MinusculoTexto = Texto.lower()
    return MinusculoTexto
def Contador(Letra,Texto):
    aux = 0
    for a in Texto.lower():
        if (Letra.lower == a):
            aux = aux + 1
    if(aux > 0):
        print("Palavra encontrada")
    print("A palavra aparece",aux,"vezes no texto")
        
    
