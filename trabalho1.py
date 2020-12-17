import csv
import locale

# O(n²)
def selectionSort(lista):
    for i in range(1, len(lista)):
        for j in range(0 , i):
            if(lista[i] < lista[j]):
                aux = lista[j]
                lista[j] = lista[i]
                lista[i] = aux

# O(n log n)
def shellSort(lista):
    dist = len(lista) // 2
    while(dist > 0):
        i = dist
        while(i < len(lista)):
            temp = lista[i]
            j = i - dist
            while(j>= 0 and lista[j] > temp):
                lista[j+dist] = lista[j]
                j -= dist
                lista[j+dist] = temp
            i += 1
        dist = dist // 2

# O(n)
def countingSort(arr, exp1):
    n = len(arr)
    output = [0] * (n)
    count = [0] * (10)

    for i in range(0, n):
        index = (arr[i]/exp1)
        count[int((index)%10)] += 1

    for i in range(1,10):
        count[i] += count[i-1]

    i = n-1
    while i>=0:
        index = (arr[i]/exp1)
        output[ count[ int((index)%10) ] - 1] = arr[i]
        count[int((index)%10)] -= 1
        i -= 1

    i = 0
    for i in range(0,len(arr)):
        arr[i] = output[i]

def radixSort(arr):
    max1 = max(arr)

    exp = 1
    while max1/exp > 0:
        countingSort(arr,exp)
        exp *= 10

def totalRespiradores(lista, op):
    if(op == 1):
        print("\n========================================")
        print(f"São Paulo recebeu conforme essa distribuição: {lista}")
    elif(op == 2):
        print("\n========================================")
        print(f"Rio de Janeiro recebeu conforme essa distribuição: {lista}")
    elif(op == 3):
        print("\n========================================")
        print(f"Minas Gerais recebeu conforme essa distribuição: {lista}")
    elif(op == 4):
        print("\n========================================")
        print(f"Espírito Santo recebeu conforme essa distribuição: {lista}")
    elif(op == 5):
        print("\n========================================")
        print(f"O Sudeste recebeu conforme essa distribuição: {lista}")
    print("========================================\n")

def gastoTotal(lista, op):
    soma = 0
    for i in lista:
        soma += float(i)

    if(op == 1):
        print("\n========================================")
        print(f"São Paulo gastou: {locale.currency(soma, grouping=True)}")
    elif(op == 2):
        print("\n========================================")
        print(f"Rio de Janeiro gastou: {locale.currency(soma, grouping=True)}")
    elif(op == 3):
        print("\n========================================")
        print(f"Minas Gerais gastou: {locale.currency(soma, grouping=True)}")
    elif(op == 4):
        print("\n========================================")
        print(f"Espírito Santo gastou: {locale.currency(soma, grouping=True)}")
    elif(op == 5):
        print("\n========================================")
        print(f"O Sudeste gastou: {locale.currency(soma, grouping=True)}")
    print("========================================\n")

def tipoDestino(lista, op):
    uti=transporte=transporteUSA=0

    for i in lista:
        if(i.lower().rstrip() == "uti"):
            uti += 1
        elif(i.lower().rstrip() == "transporte"):
            transporte += 1
        elif(i.lower().rstrip() == "transporte usa"):
            transporteUSA += 1

    if(op == 1):
        print("\n========================================")
        print(f"São Paulo destinou {transporte} respiradores para transporte, {uti} para UTI e {transporteUSA} de transporte USA")
    elif(op == 2):
        print("\n========================================")
        print(f"Rio de Janeiro destinou {transporte} respiradores para transporte, {uti} para UTI e {transporteUSA} de transporte USA")
    elif(op == 3):
        print("\n========================================")
        print(f"Minas Gerais destinou {transporte} respiradores para transporte, {uti} para UTI e {transporteUSA} de transporte USA")
    elif(op == 4):
        print("\n========================================")
        print(f"Espírito Santo destinou {transporte} respiradores para transporte, {uti} para UTI e {transporteUSA} de transporte USA")
    elif(op == 5):
        print("\n========================================")
        print(f"O Sudeste destinou {transporte} respiradores para transporte, {uti} para UTI e {transporteUSA} de transporte USA")
    print("========================================\n")

if __name__ == "__main__":

    lista = []

    arquivo = open('distribuicao_respiradores.csv')
    linhas = csv.reader(arquivo)

    locale.setlocale(locale.LC_ALL, '')

    print("Análise sobre a distribuição de respiradores durante a Covid-19 no Sudeste brasileiro no período de abril a novembro\n")
    print("Para analisar o número de respiradores por Estado recebidos cronologicamente, digite 1")
    print("Para analisar a quantidade total de respiradores recebidos por estado, digite 2")
    print("Para analisar qual o gasto total, digite 3")
    print("Para analisar o tipo de destino para cada Estado, digite 4")

    n = int(input("Digite a opção: "))

    while(n <= 0 or n > 4):
        print("\nOpção inválida. Digite uma das opções disponíveis\n")
        n = int(input("Digite a opção: "))

    if(n == 1):
        print("\nQual Estado deseja analisar? \n (1) - São Paulo \n (2) - Rio de Janeiro \n (3) - Minas Gerais \n (4) - Espírito Santo \n (5) - Todos\n")
        op = int(input("Digite a opção: "))

        while(op <= 0 or op > 5):
            print("\nOpção inválida. Digite uma das opções disponíveis\n")
            op = int(input("Digite a opção: "))

        if(op == 1):
            for i in linhas:
                if(i[0].lower().rstrip() == "são paulo"):
                    lista.append(i[1])

        elif(op == 2):
            for i in linhas:
                if(i[0].lower().rstrip() == "rio de janeiro"):
                    lista.append(i[1])

        elif(op == 3):
            for i in linhas:
                if(i[0].lower().rstrip() == "minas gerais"):
                    lista.append(i[1])

        elif(op == 4):
            for i in linhas:
                if(i[0].lower().rstrip() == "espirito santo"):
                    lista.append(i[1])

        elif(op == 5):
            for i in linhas:
                lista.append(i[1])

        totalRespiradores(lista, op)

    elif(n == 2):

        sp=rj=mg=es=0

        print("\nQual Estado deseja analisar? \n (1) - São Paulo \n (2) - Rio de Janeiro \n (3) - Minas Gerais \n (4) - Espírito Santo \n (5) - Todos\n")
        op = int(input("Digite a opção: "))

        while(op <= 0 or op > 5):
            print("Opção inválida. Digite uma das opções disponíveis")
            op = int(input("Digite a opção: "))

        if(op == 1):
            for i in linhas:
                if(i[0].lower().rstrip() == "são paulo"):
                    lista.append(int(i[1]))

        elif(op == 2):
            for i in linhas:
                if(i[0].lower().rstrip() == "rio de janeiro"):
                    lista.append(int(i[1]))

        elif(op == 3):
            for i in linhas:
                if(i[0].lower().rstrip() == "minas gerais"):
                    lista.append(int(i[1]))

        elif(op == 4):
            for i in linhas:
                if(i[0].lower().rstrip() == "espirito santo"):
                    lista.append(int(i[1]))

        elif(op == 5):
            for i in linhas:
                if(i[0].lower().rstrip() == "são paulo"):
                    sp += 1
                elif(i[0].lower().rstrip() == "rio de janeiro"):
                    rj += 1
                elif(i[0].lower().rstrip() == "minas gerais"):
                    mg += 1
                elif(i[0].lower().rstrip() == "espirito santo"):
                    es += 1
                lista.append(int(i[1]))

        print("\nQual algoritmo deseja utilizar? \n (1) - Selection Sort \n (2) - Shell Sort \n (3) - Radix Sort\n")
        k = int(input("Digite a opção: "))

        while(k <= 0 or k > 3):
            print("Opção inválida. Digite uma das opções disponíveis")
            k = int(input("Digite a opção: "))

        if(k == 1):
            selectionSort(lista)

        elif(k == 2):
            shellSort(lista)

        elif(k == 3):
            radixSort(lista)

        soma = 0
        for i in lista:
            soma += int(i)
        if(op != 5):
            print("\n========================================")
            print("A ordem crescente de entregas foi: " + str(lista))
            print(f"O número total de respiradores recebidos foi {soma}")
            print(f"O maior número de respiradores recebidos de uma única vez foi {lista[len(lista)-1]}")
            print(f"O menor número de respiradores recebidos de uma única vez foi {lista[0]}")
            print(f"As entregas ocorreram no decorrer de {len(lista)} dias")
            print("========================================\n")
        else:
            print("\n========================================")
            print("A ordem crescente de entregas foi: " + str(lista))
            print(f"O número total de respiradores recebidos foi {soma}, sendo {sp} para São Paulo, {rj} para o Rio de Janeiro, {mg} para Minas Gerais e {es} para Espírito Santo")
            print(f"O maior número de respiradores recebidos de uma única vez foi {lista[len(lista)-1]}")
            print(f"O menor número de respiradores recebidos de uma única vez foi {lista[0]}")
            print(f"O estado que mais recebeu respiradores foi Minas Gerais, com {mg} unidades")
            print("========================================\n")
    elif(n == 3):

        print("\nQual Estado deseja analisar? \n (1) - São Paulo \n (2) - Rio de Janeiro \n (3) - Minas Gerais \n (4) - Espírito Santo \n (5) - Todos\n")
        op = int(input("Digite a opção: "))

        while(op <= 0 or op > 5):
            print("Opção inválida. Digite uma das opções disponíveis")
            op = int(input("Digite a opção: "))

        if(op == 1):
            for i in linhas:
                if(i[0].lower().rstrip() == "são paulo"):
                    lista.append(float(i[2]))
        elif(op == 2):
            for i in linhas:
                if(i[0].lower().rstrip() == "rio de janeiro"):
                    lista.append(float(i[2]))
        elif(op == 3):
            for i in linhas:
                if(i[0].lower().rstrip() == "minas gerais"):
                    lista.append(float(i[2]))
        elif(op == 4):
            for i in linhas:
                if(i[0].lower().rstrip() == "espirito santo"):
                    lista.append(float(i[2]))
        elif(op == 5):
            for i in linhas:
                lista.append(float(i[2]))

        gastoTotal(lista, op)

    elif(n == 4):

        print("\nQual Estado deseja analisar? \n (1) - São Paulo \n (2) - Rio de Janeiro \n (3) - Minas Gerais \n (4) - Espírito Santo \n (5) - Todos\n")
        op = int(input("Digite a opção: "))

        while(op <= 0 or op > 5):
            print("Opção inválida. Digite uma das opções disponíveis")
            op = int(input("Digite a opção: "))

        if(op == 1):
            for i in linhas:
                if(i[0].lower().rstrip() == "são paulo"):
                    lista.append(i[3])
        elif(op == 2):
            for i in linhas:
                if(i[0].lower().rstrip() == "rio de janeiro"):
                    lista.append(i[3])
        elif(op == 3):
            for i in linhas:
                if(i[0].lower().rstrip() == "minas gerais"):
                    lista.append(i[3])
        elif(op == 4):
            for i in linhas:
                if(i[0].lower().rstrip() == "espirito santo"):
                    lista.append(i[3])
        elif(op == 5):
            for i in linhas:
                lista.append(i[3])

        tipoDestino(lista, op)

    arquivo.close()
