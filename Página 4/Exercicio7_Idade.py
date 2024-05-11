#Vamos calcular a idade de uma pessoa

print("Vamos ler a sua idade em anos, meses e dias e apresentar quantos dias de vida você tem")

anos = int(input("Digite qual a sua idade em anos: "))
meses = int(input("Digite quantos meses passaram desde o seu último aniversário: "))
dias = int(input("Digite quantos dias passaram desde o seu último mesversário: "))

idade = (anos * 365 + meses * 30 + dias)

print("O total de dias de vida que você tem é: ", idade)