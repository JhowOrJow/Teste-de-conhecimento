"""
4) Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado:

SP – R$67.836,43
RJ – R$36.678,66
MG – R$29.229,88
ES – R$27.165,48
Outros – R$19.849,53

Escreva um programa na linguagem que desejar onde calcule o percentual de representação que cada 
estado teve dentro do valor total mensal da distribuidora.
"""
sp = 67.83643
rj = 36.67866
mg = 29.22988
es = 27.16548
out = 19.84953
soma_total = float(sp + rj + mg + es + out)
print(f"A soma total calculada é de: {soma_total:5.2f}\n")
print("__"*50)
percentual_sp = ((sp/soma_total)*100)
percentual_rj = ((rj/soma_total)*100)
percentual_mg = ((mg/soma_total)*100)
percentual_es = ((es/soma_total)*100)
percentual_out = ((out/soma_total)*100)

print("\n-----PORCENTAGEM % DE CADA ESTADO-----\n")
print(f'Porcentagem de SP {percentual_sp:5.2f}\n')
print("__"*50)
print(f'Porcentagem de RJ {percentual_rj:5.2f}\n')
print("__"*50)
print(f'Porcentagem de MG {percentual_mg:5.2f}\n')
print("__"*50)
print(f'Porcentagem de ES {percentual_es:5.2f}\n')
print("__"*50)
print(f'Porcentagem de OUT {percentual_out:5.2f}\n')