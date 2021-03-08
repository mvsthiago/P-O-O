def imprimirNotaFiscal(codigo, Nome, CPF, produtos):
    codigo = str(codigo)
    cont = '1'
    print('---------------------------------------------------------------------------------------------------------------')
    print('NOTA FISCAL                                                                                          01/08/2020')
    print('Cliente: %s Nome: %s' % (codigo, Nome))
    print('CPF/CNPJ: %s' % (CPF))
    print('---------------------------------------------------------------------------------------------------------------')
    print('ITENS')
    print('---------------------------------------------------------------------------------------------------------------')
    print('Seq   Descrição                                                    QTD       Valor Unit            Preço')
    print('----   --------------------------------------------------------   -----     ------------     ------------------')
    for key, value in produtos.items():
        if key == 'Valor' + cont:
            valor = value
            pass

        if key == 'Descricao'+cont:
            descricao = value
            pass
        if key == 'Quantidade' + cont:
            quantidade = value
            preco = float(quantidade)*float(valor)
            preco = str(preco)
            print('00%s    %s                                                  %s             %s                  %s' % (
                cont, descricao, quantidade, valor, preco))
            print('')
            cont = int(cont) + 1
            cont = str(cont)
            pass

    print('---------------------------------------------------------------------------------------------------------------')
    print('Valor Total: 185.00')


def setValoresNota(Nome, CPF, codigo, Valor, Descricao):

    pass


produtos = {}
cont = '2'
codigo = str(input('Digite o código do cliente:'))
Nome = input('Digite o nome do cliente:')
CPF = input('Digite o cpf do cliente:')
Descricao = input('Digite a descrição do produto:')
Valor = input('Digite o valor do produto:')
Quantidade = input('Digite a quantidade do produto:')

produtos['Valor1'] = Valor
produtos['Descricao1'] = Descricao
produtos['Quantidade1'] = Quantidade

flag = input('Deseja inserir outro produto?(Digite S/N)')



while(flag == 'S' or flag == 's'):
    Descricao = input('Digite a descricao de outro produto:')
    Valor = input('Digite o valor do produto:')
    Quantidade = input('Digite a quantidade do produto:')

    produtos['Valor'+cont] = Valor
    produtos['Descricao'+cont] = Descricao
    produtos['Quantidade'+cont] = Quantidade

    flag = input('Deseja inserir outro produto?(Digite S/N)')
    cont = int(cont) + 1
    cont = str(cont)
    if (flag != 'n' or flag != 'N'):
        print('Por favor digite novamente')
        flag = 's'


print(produtos)

# setValoresNota(Nome,CPF,codigo,Valor,Descricao)
imprimirNotaFiscal(codigo, Nome, CPF, produtos)