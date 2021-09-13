# função que converte valor do consumo em KWH
def calcConsumo(preco: int) -> int:

    consumo = 0

    consumo += min(max(0, preco/2), 100)
    preco -= 2*100

    consumo += min(max(0, preco/3), 9900)
    preco -= 3*9900

    consumo += min(max(0, preco/5), 990000)
    preco -= 5*990000

    consumo += max(0, preco/7)

    return int(consumo)

# função que converte KWH em preço


def calcPreco(Kwh: int) -> int:

    preco = 0
    preco += min(max(0, Kwh*2), 2*100)
    Kwh -= 100

    preco += min(max(0, Kwh*3), 3*9900)
    Kwh -= 9900

    preco += min(max(0, Kwh*5), 5*990000)
    Kwh -= 990000

    preco += max(0, Kwh*7)

    return int(preco)


def main() -> int:

    while True:
        # captura a entrada de dados
        entrada = input()

        # finaliza o programa quando recebe 0 0 de entrada
        if entrada == '0 0':
            break

        # sepra os 2 valores da linha
        entrada = entrada.split()

        # converte para inteiro
        consumoTotal = int(entrada[0])
        diffConsumo = int(entrada[1])

        totalKWH = calcConsumo(consumoTotal)

        meuConsumo = 0
        consumoVisinho = 0

        init = 1
        fim = totalKWH

        # loop que busca pelo resultado, usando a estrategia dividir para conquistar
        while(init <= fim):

            # uso similar do quicksort, pego o meio da "lista" e vai dividindo ate achar o resultado
            pivo = (init + fim)//2

            consumoVisinho = calcPreco(pivo)
            meuConsumo = calcPreco(totalKWH - pivo)

            # verifico se a diferença do meu consumo com do meu visinho é menor que a diferença exigida
            if (consumoVisinho-meuConsumo) <= diffConsumo:
                # sendo menor o inicio recebe meu pivo
                init = pivo
            elif (consumoVisinho-meuConsumo) > diffConsumo:
                # sea diferença for grande o final se torna o pivo
                fim = pivo

            if (consumoVisinho-meuConsumo) == diffConsumo:
                print(meuConsumo)
                break


if __name__ == '__main__':
    main()
