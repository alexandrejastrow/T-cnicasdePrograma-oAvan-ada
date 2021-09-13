class Work:
    def __init__(self, nome, valorA, valorB, custo):
        self.nome = nome
        self.valorA = valorA
        self.valorB = valorB
        self.custo = custo


memo = {}
trabalhos = []


def calculaCusto(n: int, m: int, a: int, b: int, index: int) -> None:
    '''
        Função que calcula o custo da agencia resolver o problema (cargaTrabalhoInicial, cargaTrabalhoAlvo, valorA, valorB)
    '''

    global memo
    global trabalhos

    # verifica se trabalho similar ja foi feito anteriormente
    if(n, m, a, b) in memo:
        trabalhos[index].custo = memo[(n, m, a, b)]
        return

    while True:
        # se a carga de trabalho inicial for igual ao alvo, para o loop
        if n == m:
            break
        aux = n//2

        # se o valor de B for menor do que valor de A * (valor atual de n),  e (valor atual de n // 2) for maior do que o valor alvo
        if trabalhos[index].valorB < (n-aux) * trabalhos[index].valorA and aux >= m:

            n = aux
            # O custo é incrementado com o valor de B
            trabalhos[index].custo += trabalhos[index].valorB
        else:
            n -= 1
            # caso contrario o custo é incrementado com o valor de A
            trabalhos[index].custo += trabalhos[index].valorA

    # salva o problema com entrada (n,m) na memoria
    memo[(n, m, a, b)] = trabalhos[index].custo
    return


def main() -> int:

    numeroDeProblemas = int(input())
    case = 1

    global trabalhos
    while(numeroDeProblemas):

        trabalhos = []
        entrada = input()
        entrada = entrada.split()

        cargaTrabalhoInicial = int(entrada[0])
        cargaTrabalhoAlvo = int(entrada[1])
        qrdAgencias = int(entrada[2])

        for i in range(qrdAgencias):
            ag = input()

            ag = ag.split(":")
            nome = ag[0]
            values = ag[1].split(",")
            a = int(values[0])
            b = int(values[1])
            # cria cada agencia e insere na lista
            trabalhos.append(Work(nome, a, b, 0))

            # calcula custo para a agencia de indice i
            calculaCusto(cargaTrabalhoInicial, cargaTrabalhoAlvo, a, b, i)

        # ordena para este caso, pelo custo e pelo nome da agencia
        trabalhos = sorted(trabalhos, key=lambda l: [l.custo, l.nome])

        # impime os resultados
        print("Case", case)
        for i in range(qrdAgencias):
            print(trabalhos[i].nome, trabalhos[i].custo)

        case += 1
        numeroDeProblemas -= 1

    return 0


if __name__ == '__main__':
    main()
