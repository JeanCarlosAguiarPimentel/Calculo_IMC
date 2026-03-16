nome_1="Jean Carlos"
altura_1 = 1.63
peso_1 = 52.60
IMC_1 = peso_1 / (altura_1 * altura_1)

nome_2 ="Isabella Vitória"
altura_2 = 1.64
peso_2 = 73
IMC_2 = peso_2 / (altura_2 * altura_2)

linha_1 = f'{nome_1} tem {altura_1:.2f} de altura'
linha_2 = f'pesa {peso_1:.2f} e seu IMC é de'
linha_3 = f'{IMC_1:.2f}'
#Dados de outro usuario
linha_5 = f'{nome_2} tem {altura_2:.2f} de altura'
linha_6 = f'pesa {peso_2:.2f} e seu IMC é de'
linha_7 = f'{IMC_2:.2f}'


print("\n", linha_1)
print(linha_2)
print(linha_3)

IMC = IMC_1

if IMC <= 18.5:
    print('abaixo do peso')
elif 18.5 < IMC <= 24.9:
    print('peso normal')
elif 25.0 < IMC <= 29.9:
    print('sobrepeso')
elif 30.0 < IMC <= 39.9:
    print('obesidade (grau 1 ou 2)')
else:
    print('obesidade grave (grau 3)')


print("\n" ,linha_5)
print(linha_6)
print(linha_7)


IMC = IMC_2

if IMC <= 18.5:
    print('abaixo do peso')
elif 18.5 < IMC <= 24.9:
    print('peso normal')
elif 25.0 < IMC <= 29.9:
    print('sobrepeso')
elif 30.0 < IMC <= 39.9:
    print('obesidade (grau 1 ou 2)')
else:
    print('obesidade grave (grau 3)')

#adicionei a questão de informar qual o nivel da saude da pessoa 
#baseada pelo calculo de imc de acordo com pesquisas veridicas na google
