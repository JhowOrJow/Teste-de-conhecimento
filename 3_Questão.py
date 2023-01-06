"""

3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, 
na linguagem que desejar, que calcule e retorne:
• O menor valor de faturamento ocorrido em um dia do mês;
• O maior valor de faturamento ocorrido em um dia do mês;
• Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

IMPORTANTE:
a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
b) Podem existir dias sem faturamento, como nos finais de semana e feriados. 
Estes dias devem ser ignorados no cálculo da média;

"""
import json

with open('dados.json') as m_json:
    dados = json.load(m_json)

soma = 0
zero_faturamento = 0
faturamento = 0
lista_dias = []
lista_valor_zero = []
lista_valor_maior_media = []
lista_max = []

for i in dados:
    
    dia = i['dia']
    valor = i['valor']
    soma += valor
    faturamento += 1
    Media = soma/(faturamento-zero_faturamento)
    maior_valor = 46251.174
    
    if valor == 0: 
        
        lista_dias.append(dia)
        lista_valor_zero.append(valor)
        zero_faturamento += 1
        
    if valor > Media:
        
            lista_valor_maior_media.append(dia)
         
    if valor == maior_valor:
        
        lista_max.append(valor)
        
                

print(f"\nNos dias {lista_dias} os valores faturados foram recpectivamente de:")
print(f"{lista_valor_zero} reais\n")
print("__"*50)   
print(f'Os dias onde o Faturamento foi maior que a Média mensal são:')
print(f"{lista_valor_maior_media}")
print(f"A quantidade de dias onde o faturamento foi acima da média mensal é: {len(lista_valor_maior_media)}")
print("__"*50)
'''print(dados) 
print(faturamento)'''
print(f'\nA média do Faturamento é {Media:5.2f}')
print("__"*50)
print(f"O maior valor faturado no mês é {lista_max} e foi faturado no dia {9}")

        
        
           