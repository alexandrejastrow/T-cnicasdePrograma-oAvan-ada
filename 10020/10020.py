
class conjuntoLR:

    def __init__(self, l, r):
        self.l = l
        self.r = r


def resolveProblema(problemaAtual: list, M: int) -> None:

    atual = 0
    aux = 0
    index = 1

    # lista onde são salvos os resultados
    segmentos = []

    # enquanto a variavel auxiliar for menor do que o valor de M
    while (aux < M):

        novaLinha = atual
        alvo = 0
        # enquanto o valor do index for menor do que a quantidade de seguimentos de reta
        while(index < len(problemaAtual)):

            # se o ponto l for maior do que o inicio do segimento [atual ... M]
            if problemaAtual[index].l > atual:
                # para o loop
                break
            # se o ponto r desse seguimento for maior do que a novaLinha
            elif problemaAtual[index].r >= novaLinha:
                # nova linha recebe o valor de r desse seguimento
                novaLinha = problemaAtual[index].r
                # alvo recebe o index
                alvo = index

            index += 1
        # se o alvo for 0 nao existe segimento de reta que resolva este problema
        if alvo == 0:
            break
        # o seguimento de reta na lista problemaAtual posição atende aos requisitos do problema, e é adcionado como parte da solução
        segmentos.append(problemaAtual[alvo])
        # atual é atualizado [atual=novaLinha ... M]
        atual = novaLinha
        aux = novaLinha

    # se o aux for maior que M o seguimento [0 ... m] foi descoberto
    if aux >= M:
        # imprime a quantidade de seguimentos usados para resolver o problema
        print(str(len(segmentos)))
        # imprime os seguimentos encontrados
        for elem in segmentos:
            print(elem.l, elem.r)
    else:
        # imprime 0 caso nao haja solução
        print(0)

    return None


def main() -> int:

    qtdProblema = int(input())

    while qtdProblema:

        # so pra pular a linha branco, não usado
        linhaBranco = input()
        # captura a entrada de seguimentos de linhas
        qtdlinhas = int(input())

        problemaAtual = []
        while True:
            entrada = input()
            entrada = entrada.split()

            # finaliza o programa quando recebe 0 0 de entrada
            if entrada == ['0', '0']:
                break

            if(len(entrada) > 0):
                # insere na lista os segimentos l, r
                problemaAtual.append(conjuntoLR(
                    int(entrada[0]), int(entrada[1])))

        # ordena o problema atual pelos valores de [l, r]
        problemaAtual = sorted(problemaAtual, key=lambda c: [c.l, c.r])

        problemaAtual.insert(0, conjuntoLR(
            0, 0))

        # chama função que resolve o problema
        resolveProblema(problemaAtual, qtdlinhas)
        qtdProblema -= 1
        # separa os problemas por 1 linha em branco
        print()


if __name__ == '__main__':
    main()
