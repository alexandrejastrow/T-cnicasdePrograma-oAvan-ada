
memorizacao = {}
size = 0


def divideCoins(arrayDeMoedas: list, soma: int, index=0) -> int:
    '''
        Função recebe uma lista de inteiros, cada inteiro representa uma moeda,
        Recebe um inteiro de nome soma, que representa a metade das somas das moedas, e um valor de index que inicializa em 0 por padrao.

    '''

    global size
    global memorizacao

    # verifica se a soma ou index chegaram na condição de parada
    if soma <= 0 or index >= size:
        return 0

    # Apesar de ter essa parte de memorização ela não está funcionando como desejado.
    if (soma, index) in memorizacao:
        return memorizacao[(soma, index)]

    # Se a posição atual do vetor for maior que a soma, pula para próxima parte do problema
    if arrayDeMoedas[index] > soma:
        return divideCoins(arrayDeMoedas, soma, index+1)

    else:
        # É feita uma verificação recursiva, onde inclui este item do vetor na conta.
        usaEste = arrayDeMoedas[index] + \
            divideCoins(arrayDeMoedas, soma - arrayDeMoedas[index], index+1)

        # É feita uma verificação recursiva, onde não inclui este item do vetor na conta.
        naoUsaEste = divideCoins(arrayDeMoedas, soma, index+1)

        # Verifica qual é o maior valor, pois ele é o que está mais perto da variável soma.
        result = max(usaEste, naoUsaEste)

        # Insere este resultado na memorização
        memorizacao[(soma, index)] = result

        return result


def moedasStrToInt(moedas: list) -> list and int:
    '''
        Função recebe uma lista de strings que são convertidos para valores inteiros e inseridos em uma lista auxiliar, essa nova lista é retornada, junto com a soma dos inteiros.
    '''
    total = 0
    aux = []
    for i in range(len(moedas)):

        aux.append(int(moedas[i]))
        total += int(moedas[i])

    return (aux, total)


def main() -> int:
    '''
        captura as informações necessárias para resolução do problema.
    '''
    global size
    global memorizacao

    numeroDeProblemas = int(input())

    while(numeroDeProblemas):

        qtdMoedas = input()
        moedas = input()

        arrayDeMoedas, total = moedasStrToInt(moedas.split())
        # A memorização é reiniciada, pois caso contrário há divergência de resultado em alguns valores.

        # comentando essa linha a memorização fica aplicada para todo o problema, porem alguns resultados divergem
        memorizacao = {}

        size = int(qtdMoedas)

        result = divideCoins(arrayDeMoedas, total//2)

        # Imprime a diferença do total menos o dobro do resultado encontrado
        print(total - 2*result)
        numeroDeProblemas -= 1
    return 0


if __name__ == '__main__':
    main()
