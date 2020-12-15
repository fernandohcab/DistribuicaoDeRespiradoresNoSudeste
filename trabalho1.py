import csv

# O(n²)
def selectionSort(lista, linhas):
    for i in range(1, len(lista)):
        for j in range(0 , i):
            if(lista[i] < lista[j]):
                aux = lista[j]
                lista[j] = lista[i]
                lista[i] = aux

    print(lista)

# O(n log n)
def shellSort(lista, linhas):
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
    print(lista)

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

def radixSort(arr, linhas):
    max1 = max(arr)

    exp = 1
    while max1/exp > 0:
        countingSort(arr,exp)
        exp *= 10

    print(arr)

if __name__ == "__main__":

    SP = []
    RJ = []
    MG = []
    ES = []
    lista = []

    arquivo = open('distribuicao_respiradores.csv')
    linhas = csv.reader(arquivo)

    print("Análise sobre a distribuição de respiradores durante a Covid-19 no Sudeste brasileiro\n")
    print("Para analisar o número de respiradores por Estado, digite 1")
    print("Para analisar a quantidade de respiradores recebidos, digite 2")
    print("Para analisar o custo de cada entrega de respiradores, digite 3")
    print("Para analisar a data de entregas para cada Estado, digite 4")

    print("Para sair, aperte 0")
    n = 1
    while(n != 0):
        n = int(input())

        if(n == 0):
            break;

        elif(n == 1):

            print("Qual Estado deseja analisa? \n (1) - São Paulo \n (2) - Rio de Janeiro \n (3) - Minas Gerais \n (4) - Espírito Santo \n (5) - Todos")
            op = int(input())
            while(op <= 0 or op > 5):
                print("Opção inválida. Digite uma das opções disponíveis")
                op = int(input())
            if(op == 1):
                for i in linhas:
                    if(i[0].lower().rstrip() == "são paulo"):
                        lista.append(i[0])

            elif(op == 2):
                for i in linhas:
                    if(i[0].lower().rstrip() == "rio de janeiro"):
                        lista.append(i[0])
            elif(op == 3):
                for i in linhas:
                    if(i[0].lower().rstrip() == "minas gerais"):
                        lista.append(i[0])
            elif(op == 4):
                for i in linhas:
                    if(i[0].lower().rstrip() == "espirito santo"):
                        lista.append(i[0])
            elif(op == 5):
                for i in linhas:
                    lista.append(i[0])

            print("Qual algoritmo deseja utilizar? \n (1) - Selection Sort \n (2) - Shell Sort \n (3) - Radix Sort")
            k = int(input())
            while(k <= 0 or k > 3):
                print("Opção inválida. Digite uma das opções disponíveis")
                k = int(input())

            if(k == 1):
                selectionSort(lista, linhas)
                break
            elif(k == 2):
                shellSort(lista, linhas)
                break
            elif(k == 3):
                radixSort(lista, linhas)
                break

        elif(n == 2):
            print("Qual Estado deseja analisa? \n (1) - São Paulo \n (2) - Rio de Janeiro \n (3) - Minas Gerais \n (4) - Espírito Santo \n (5) - Todos")
            op = int(input())
            while(op <= 0 or op > 5):
                print("Opção inválida. Digite uma das opções disponíveis")
                op = int(input())
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
                    lista.append(int(i[1]))

            print("Qual algoritmo deseja utilizar? \n (1) - Selection Sort \n (2) - Shell Sort \n (3) - Radix Sort")
            k = int(input())

            while(k <= 0 or k > 3):
                print("Opção inválida. Digite uma das opções disponíveis")
                k = int(input())
            if(k == 1):
                selectionSort(lista, linhas)
                break
            elif(k == 2):
                shellSort(lista, linhas)
                break
            elif(k == 3):
                radixSort(lista, linhas)
                break

        elif(n == 3):
            print("Qual Estado deseja analisa? \n (1) - São Paulo \n (2) - Rio de Janeiro \n (3) - Minas Gerais \n (4) - Espírito Santo \n (5) - Todos")
            op = int(input())
            while(op <= 0 or op > 5):
                print("Opção inválida. Digite uma das opções disponíveis")
                op = int(input())
            if(op == 1):
                for i in linhas:
                    if(i[0].lower().rstrip() == "são paulo"):
                        lista.append(int(i[2]))
            elif(op == 2):
                for i in linhas:
                    if(i[0].lower().rstrip() == "rio de janeiro"):
                        lista.append(int(i[2]))
            elif(op == 3):
                for i in linhas:
                    if(i[0].lower().rstrip() == "minas gerais"):
                        lista.append(int(i[2]))
            elif(op == 4):
                for i in linhas:
                    if(i[0].lower().rstrip() == "espirito santo"):
                        lista.append(int(i[2]))
            elif(op == 5):
                for i in linhas:
                    lista.append(int(i[2]))

            print("Qual algoritmo deseja utilizar? \n (1) - Selection Sort \n (2) - Shell Sort \n (3) - Radix Sort")
            k = int(input())

            while(k <= 0 or k > 3):
                print("Opção inválida. Digite uma das opções disponíveis")
                k = int(input())
            if(k == 1):
                selectionSort(lista, linhas)
                break
            elif(k == 2):
                shellSort(lista, linhas)
                break
            elif(k == 3):
                radixSort(lista, linhas)
                break

        elif(n == 4):
            print("Qual Estado deseja analisa? \n (1) - São Paulo \n (2) - Rio de Janeiro \n (3) - Minas Gerais \n (4) - Espírito Santo \n (5) - Todos")
            op = int(input())
            while(op <= 0 or op > 5):
                print("Opção inválida. Digite uma das opções disponíveis")
                op = int(input())
        if(op == 1):
            for i in linhas:
                if(i[0].lower().rstrip() == "são paulo"):
                    lista.append(int(i[3]))
        elif(op == 2):
            for i in linhas:
                if(i[0].lower().rstrip() == "rio de janeiro"):
                    lista.append(int(i[3]))
        elif(op == 3):
            for i in linhas:
                if(i[0].lower().rstrip() == "minas gerais"):
                    lista.append(int(i[3]))
        elif(op == 4):
            for i in linhas:
                if(i[0].lower().rstrip() == "espirito santo"):
                    lista.append(int(i[3]))
        elif(op == 5):
            for i in linhas:
                lista.append(int(i[3]))

        print("Qual algoritmo deseja utilizar? \n (1) - Selection Sort \n (2) - Shell Sort \n (3) - Radix Sort")
        k = int(input())

        while(k <= 0 or k > 3):
            print("Opção inválida. Digite uma das opções disponíveis")
            k = int(input())
        if(k == 1):
            selectionSort(lista, linhas)
            break
        elif(k == 2):
            shellSort(lista, linhas)
            break
        elif(k == 3):
            radixSort(lista, linhas)
            break
        else:
            print("Opção inválida. Digite uma das opções disponíveis")

    arquivo.close()
#    print(SP)
