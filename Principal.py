import StringUtil

Texto = input("Digite o texto: ")

#Imprimir tamanho
StringUtil.Output(Texto)
StringUtil.Output(StringUtil.Tamanho(Texto))

#Imprimir Maiusculo
StringUtil.Output(StringUtil.Maiusculo(Texto))

#Imprimir Minusculo
StringUtil.Output(StringUtil.Minusculo(Texto))

Letra = input("Digite uma letra: ")
StringUtil.Contador(Letra,Texto)
