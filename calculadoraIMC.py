from time import sleep

print('=*=' * 11)
print("Calculadora e Analisador de IMC:")
print('=*=' * 11)
sleep(2)
nome = str(input("Digite seu nome: "))
print(f"Prazer em conhece-lo {nome}!")
sleep(1)
peso = float(input("Digite seu peso atual: "))
print("Ótimo, vamos para o próximo...")
sleep(2)
altura = float(input("Digite a sua altura atual em CM Ex(1.70): "))
sleep(1)

imc = peso / (altura * altura)

print("Obrigado pelas informações, vamos ao resultado... \n")
sleep(3)

if imc <= 18.5:
    print(f"Seu IMC é {imc:.2f}, você está abaixo do Peso Ideal")
elif 18.5 <= imc <= 25:
    print(f"Seu IMC é {imc:.2f}, você está no Peso Ideal!")
elif 25 <= imc <= 30:
    print(f"Seu IMC é {imc:.2f} você está na faixa de Sobrepeso!")
elif 30 <= imc <= 40:
    print(f"Seu IMC é {imc:.2f}, você está na faixa de Obesidade!")
else:
    print(f"Seu IMC é {imc:2f}, você se enquadra na faixa de Obesidade Morbida!")
sleep(5)
print(f" \nObrigado por usar a calculadora de ICM {nome}, até breve!")
sleep(2)
print("\nPode Fechar esta aba! :)")
