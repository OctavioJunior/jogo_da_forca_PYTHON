import os
import random

nome = input("Digite se nome: ")
print(f"Olá {nome}, vamos começar o jogo!!!")
input("\nPressione ENTER para começar o jogo!")
os.system("cls")

listaDePalavras = ["gato", "cachorro",
                   "elefante", "cobre", "tartaruga", "coelho"]
palavraSelecionada = random.choice(listaDePalavras).upper()
tamanhoPalavra = len(palavraSelecionada)
palavraCodificada = ["_"]*tamanhoPalavra
quantidadeErros = 0

while "_" in palavraCodificada and quantidadeErros < 6:
  print(f"\nSua palavra tem {tamanhoPalavra} letras e é um animal.")
  print(f"Erros: {quantidadeErros} de 6.")
  for letra in palavraCodificada:
      print(letra, end=" ")  # ____
  print()

  letraEscolhida = input("Digite uma letra: ").upper()
  acertou = False
  for i in range(len(palavraSelecionada)):
    if letraEscolhida == palavraSelecionada[i]:
      palavraCodificada[i] = letraEscolhida
      acertou = True

  if acertou == True:
    print("Parabéns, você acertou!")
  else:
    print("Errou a letra, tente novamente")
    quantidadeErros = quantidadeErros + 1
  os.system("cls")

if quantidadeErros == 6:
  print("Você perdeu o jogo!")
else:
  print("Parabéns, você ganhou o jogo!")

print(f"A palavra era: {palavraSelecionada}")