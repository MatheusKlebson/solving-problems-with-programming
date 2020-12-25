'''Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
Calcule e mostre o total do seu salário no referido mês.'''
ganho_hora = float(input("Quanto você ganha por hora?R$"))
horas_trabalhadas = float(input("Quantas horas trabalhadas no mês? "))
salario = ganho_hora * horas_trabalhadas
print(f"Salário no fim do mÊs:R${salario}")