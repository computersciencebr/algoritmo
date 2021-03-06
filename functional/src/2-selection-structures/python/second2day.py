## Selection Structures 

###  Verificar valor 
Faça um programa que peça um valor e mostre na tela se o valor é positivo ou negativo.
#### Solução

### Número primo
Faça um programa que exiba verdadeiro se o número for primo (falso caso contrário)

### Tipo de triângulo
Pedir os valores dos catetos e hipotenusa, por intermédio deles informar se o triângulo é equilátero; isóscele; escaleno 
#### Solução
> [Pascal](https://github.com/computersciencebr/algoritmo/tree/master/src/2-selection-structures/pascal/triangulo.pas)

### Energia elétrica
Calcule o valor da fatura do cliente, por intermédio do consumo em Kw/H e a categoria de consumo, sendo:
* residencial =  consumo em KwH * 0.6);
* comercio = consumo em KwH * 0.48);
* industria = consumo em KwH * 1.29);
#### Solução
> [Pascal](https://github.com/computersciencebr/algoritmo/tree/master/src/2-selection-structures/pascal/energia-eletrica.pas)

###  Votar
Perguntar a idade do usuário e verificar se ele pode votar, de acordo com seguinte regra:  
* idade>=16 não pode votar
* idade>=18 obrigado a votar 
* idade>=65 pode votar
#### Solução
> [Pascal](https://github.com/computersciencebr/algoritmo/tree/master/src/2-selection-structures/pascal/votar.pas)

### Mini Calculadora
> [Pascal](https://github.com/computersciencebr/algoritmo/tree/master/src/2-selection-structures/pascal/minicalculadora.pas)

### Cálculo de churrasco
#### Solução
> [Pascal](https://github.com/computersciencebr/algoritmo/tree/master/src/2-selection-structures/pascal/churrasco.pas)

### Cálculo de peso ideal
Leia altura, sexo e peso de uma pessoa, construa um algoritmo que calcule seu peso ideal.  
Informe se o peso da pessoa está dentro, acima ou abaixo do peso 
(Considere a margem de erro de 1 Kg para mais ou para menos como estando no peso ideal). 
Utilizando as seguintes fórmulas:
* Para homens: peso - (72.7*h) - 58
* Para mulheres: peso - (62.1*h) - 44.7
#### Solução
> [Julia](https://github.com/computersciencebr/algoritmo/tree/master/src/2-selection-structures/julia/peso-ideal.jl)

### Reajuste salarial
#### Solução
> [Pascal](https://github.com/computersciencebr/algoritmo/tree/master/src/2-selection-structures/pascal/reajuste-salarial.pas)

### Salário de Professor
#### Solução
> [Pascal](https://github.com/computersciencebr/algoritmo/tree/master/src/2-selection-structures/pascal/salario-prof.pas)

### Comissão de vendas
Dado o salário fixo, o valor das vendas efetuadas pelo vendedor de uma empresa e sabendo-se que ele recebe uma comissão de 3% sobre o total das vendas até R$ 1.500,00 e 5% sobre o que ultrapassar este valor, calcular e escrever o seu salário total.
#### Solução em:
 > [Julia](https://github.com/computersciencebr/algoritmo/tree/master/src/2-selection-structures/julia/comissao-venda.jl)  

### Gasto em lavanderia
Prepare um algoritmo para informar o total gasto em uma lavanderia. 
O algoritmo inicialmente deverá perguntar o total de camisas, o total de calças e o total de meias e informar o total gasto, levando em conta a seguinte tabela de preços:

* 02.00 = Meias 
* 05.00 = Camisas 
* 10.00 = Calças 

Depois de informar o total gasto, o algoritmo deverá perguntar ao usuário se o mesmo deseja fazer um novo cálculo de gasto, caso a resposta seja positiva, o algoritmo deverá retornar ao seu início, caso contrário deverá ser finalizado
#### Solução em:

### Loja de tintas
O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
* Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3
situações:
* comprar apenas latas de 18 litros;
* comprar apenas galões de 3,6 litros;
* comprar latas e galões, a combinação de melhor resultado.
#### Solução em:

 ### Notas para representar um valor
Escrever um algoritmo que leia um valor e calcule qual o menor número possível de notas e
moedas de 100, 50, 20, 10, 5, 2 e 1 em que o valor lido pode ser decomposto. 
Escrever o valor lido e a relação de notas necessárias.
#### Solução em:


# -*- coding: utf-8 -*-"

'''
Desafio do vídeo "Entrada de Dados": Reescreva o programa conta
Segundos para imprimir também a quantidade de dias,
ou seja, faça um programa em Python que dada a quantidade de segundos,
o programa "quebra" esse valor em dias, horas, minutos e segundos.
A saída deve estar no formato: a dias, b horas, c minutos e d segundos.

Abaixo um exemplo de como deve ser a entrada e saída de dados do programa:

Exemplo:

Entrada de Dados:
Por favor, entre com o número de segundos que deseja converter: 178615

Saída de Dados:
2 dias, 1 horas, 36 minutos e 55 segundos.
'''

second = float(input('Por favor, entre com o número de segundos que deseja converter:'))

day = second//86400

if (day - second/86400) != 0 :

    hour = day - second/86400

    if hour < 0 :
        hour = -1 * hour

    hour = hour * 24
    hour = hour//1

    if (hour- (day - second/86400)*24) != 0 :

        if ((day - second/86400)*24) < 0 :
            minute = (hour + (day - second/86400)*24)
        else:
            minute = (hour - (day - second/86400)*24)

        if minute < 0 :
            minute = (-1 * minute) *60

        temp = minute
        minute = minute//1

        temp = minute - temp

        if temp < 0 :
            temp = -1 * temp

        if temp != 0 :
            temp = (temp * 60)//1

print(int(day),"dias,",int(hour),"horas,",int(minute),"minutos e",int(temp),"segundos.")
