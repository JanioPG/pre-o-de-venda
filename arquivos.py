from data import data_da_consulta
from interface import parar_exibir, limpar_tela, linha

name_file = 'precos-produtos.txt'


def editar_arquivo_texto(lista):
    """
    -> Insere os dados do produto no arquivo de texto
    Args:
        list: lista contendo informações do produto em seus elementos.
    """
    with open(name_file, 'at+') as produtos:
        produtos.seek(0)    # retorna o ponteiro de leitura do txt p/ o início
        num_id = len(produtos.readlines()) + 1
        produtos.write(str(num_id) + ';')
        for item in (lista):
            produtos.write(str(item) + ';')
        data_hora = data_da_consulta()
        produtos.write(data_hora + '\n')
        limpar_tela()
    ler_arquivo(cod=lista[1], operação=True)


def ler_arquivo(cod='', operação=False):
    """-> Faz a leitura do arquivo de texto e apresenta ao usuário os produtos

    Args:
        cod (str, optional): Código do produto. Defaults to ''.

    Returns:
        str: Retorna dados do produto se este for encontrado, se não, retorna 'produto não encontrado'. Ou, ainda, informa erro na base de dados.
    """
    try:
        with open(name_file, 'r') as produtos:
            lines = produtos.readlines()
            if len(lines) == 0:
                return print('Nenhum produto foi cadastrado')

            if operação == True:
                lista = []
                for i, item in enumerate(lines):
                    item = item.replace('\n', '')
                    info = item.split(';')
                    if info[2] == cod:
                        lista.append(lines[i])
                if len(lista) == 0:
                    print('Produto não encontrado. Tente ver a lista completa')
                else:
                    exibir_informação(lista)
            else:
                exibir_informação(lines)
    except (FileNotFoundError, IndexError):
        print('''\033[31mERROR:
        Possíveis causas e ações:
        Base de dados não existe.
        Verifique a integridade da base de dados, o arquivo pode ter sido alterado inadequadamente.\033[m''')
    finally:
        parar_exibir()


def exibir_informação(lista):
    """
    -> Exibe um ou mais produtos da lista
    """
    print(f'\033[1;32m{"id":<4}{"Nome do Produto":<20}{"Cód.":<10}{"Lote":<10}{"Custo":<10}{"Margem de Lucro (%)":<25}{"Preço de venda":<12}{"Data da Consulta":>20} \033[m')
    linha()
    for item in lista:
        item = item.replace('\n', '')
        info = item.split(';')
        print(f'{info[0]:<4}{info[1]:<20}{info[2]:<10}{info[3]:<10}R$ {info[4]:<10}{info[5]:^25}\033[1;31mR$ {info[6]:<12}\033[m{info[7]:<20}')
        linha()


def registrar_produto():
    """
    -> Salva os dados do produto, incluindo seu preço de venda
    """
    dados = [str(input('Nome do produto: ')),
    str(input('Código do produto: ')),
    str(input('Lote: ')),
    float(input('Custo do produto: R$')),
    float(input('Margem de lucro [%]: '))
    ]
    preco = round((dados[3] / (1 - (dados[4]/100))), 2)
    dados.append(preco)
    editar_arquivo_texto(dados)
