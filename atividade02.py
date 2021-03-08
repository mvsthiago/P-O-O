'''Fazer uma sequencia de impressão onde sejam mostras as representações  decimal, octal, hexadecimal dos valores inteiros de 0 a 225 (que são os valores que um byte pode representar).
Verificar o contéudo dos especificadores de representação no contexto do comando print.
Cria para cada representação uma função especifica (printDecimal, printOctal, printHexadecimal, printBinario).
Incluir no código uma funcionalidade imprimirTabela() que executar um laço para imprimir cada linha
do relatório.
Layout da saída:
Decimal  Octal  Hexadecimal    Binario
------------- --------- --------------------- -----------------
  999      XXXX       XXXX          99999999'''
def printDecimal(n):
    print(n,'\t\t', end='')

def printBinario(n):
    print(bin(n), '\t', end='')

def printOctal(n):
    print(oct(n), '\t', end='')

def printHexadecimal(n):
    print(hex(n), '\t', '\n')

def imprimirTabela():
    n =0
    while n <256:
        printDecimal(n)
        printBinario(n)
        printOctal(n)
        printHexadecimal(n)
        n += 1


print("decimal binario octa hexa")
imprimirTabela()