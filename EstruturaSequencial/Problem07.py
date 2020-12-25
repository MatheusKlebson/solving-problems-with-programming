'''Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.
'''
'''Para fazer o cálculo da área do quadrado é necessário realizar o produto entre dois lados.
 Como o quadrado tem lados iguais, basta pegar a medida de um dos lados e elevar ao quadrado.
 Para a realização usamos a fórmula da área A = b. h, assim um de seus lados será a base (b) e o outro a altura (h).'''
lado_quadrado = float(input("Lado do quadrado: "))
calculo_area = lado_quadrado**2 
print(f"Area do quadrado mede: {calculo_area}")
print(f"O dobro da area mede: {calculo_area*2}")

'''PROBLEMA ABANDONADO'''