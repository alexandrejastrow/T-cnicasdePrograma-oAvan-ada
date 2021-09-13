
class Elephant:

    def __init__(self, KG, QI, pos):
        self.KG = KG
        self.QI = QI
        self.pos = pos


memo = [None]*1000
lstElephants = []


def calc(index: int) -> int:
    '''
        Verifica a quantidade de ocorrências onde o pesos estejam aumentando, mas o QI esteja diminuindo para a posição index doa lista de elefantes.
    '''
    global memo
    global lstElephants
    # se ja tiver memorizado retorna
    if memo[index] != None:
        return memo[index]

    memo[index] = 1

    for i in range(index+1, len(lstElephants)):
        # se o peso no index for < do que o peso em i e a inteligência em index for maior do que a de i
        if lstElephants[index].KG < lstElephants[i].KG and lstElephants[index].QI > lstElephants[i].QI:
            # este é um caso em queo peso aumenta mais a inteligencia diminui
            memo[index] = max(memo[index], 1 + calc(i))

    # retorna a quantidade de ocorrências onde o peso aumenta mais a inteligencia diminui.
    return memo[index]


def loc(index: int, pos: int) -> None:
    """
        Esta função recebe um index, e uma posição

        index: é a posição da lista de elefantes que tem a resposta correta
        pos: é a posição da lista de momorização que é decrementada
    """
    global lstElephants
    global memo

    print(lstElephants[index].pos)
    for i in range(index+1, len(lstElephants)):
        if memo[i] == pos:

            return loc(i, pos - 1)


def main() -> int:

    global lstElephants
    count = 1

    while True:
        try:
            entrada = input().split()
            # cria uma lista com os dados de elefantes, e um contador
            lstElephants.append(
                Elephant(int(entrada[0]), int(entrada[1]), count))

            count += 1
        except:
            break
    # é feita a ordenação dos elefantes por [ kilo, inteligência]
    lstElephants = sorted(lstElephants, key=lambda l: [l.KG, l.QI])

    qtd = 0
    # procura
    for i in range(len(lstElephants)):
        qtd = max(qtd, calc(i))

    print(qtd)
    # faz a busca pela resposta certa
    for i in range(len(lstElephants)):
        if(memo[i] == qtd):
            loc(i, qtd-1)
            break
    return 0


if __name__ == '__main__':
    main()
