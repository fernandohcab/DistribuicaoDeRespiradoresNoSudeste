import csv

# O(n²)
def selectionSort(lista):
    for i in range(1, len(lista)):
        for j in range(0 , i):
            if lista[i] < lista[j]:
                aux = lista[j]
                lista[j] = lista[i]
                lista[i] = aux

    print(len(lista))

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
    print(len(lista))

# O(n)
def bucket_sort(lista):

    tam = max(lista)//len(lista)

    temp = []
    resultado = []

    for i in range(0, len(lista)):
        temp.append([])

    for i in range(0, len(lista)):
        j = lista[i]//tam
        if j != len(lista):
            temp[j].append(lista[i])
        else:
            temp[len(lista) - 1].append(lista[i])

    selectionSort(temp)

    for i in range(0, len(lista)):
        resultado += temp[i]

    print(len(resultado))


if __name__ == "__main__":

    SP = []
    RJ = []
    MG = []
    ES = []
    lista = []

    arquivo = open('distribuicao_respiradores.csv')
    linhas = csv.reader(arquivo)
    for i in linhas:
        if(i[0].lower().rstrip() == "rio de janeiro"):
            RJ.append(i)
        elif(i[0].lower().rstrip() == "são paulo"):
            SP.append(i)
        elif(i[0].lower().rstrip() == "minas gerais"):
            MG.append(i)
        elif(i[0].lower().rstrip() == "espirito santo"):
            ES.append(i)

    print("Análise sobre a distribuição de respiradores durante a Covid-19 no Sudeste brasileiro\n")
    print("Para analisar a data de entregas para cada Estado, digite 1")
    print("Para analisar a quantidade de respiradores recebidos, digite 2")
    print("Para analisar o custo de cada entrega de respiradores, digite 3")
    print("Para analisar o número de respiradores por Estado, digite 4")
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
                lista = SP
            elif(op == 2):
                lista = RJ
            elif(op == 3):
                lista = MG
            elif(op == 4):
                lista = ES
            elif(op == 5):
                lista = SP + RJ + MG + ES

            print("Qual algoritmo deseja utilizar? \n (1) - Selection Sort \n (2) - Shell Sort \n (3) - Bucket Sort")
            k = int(input())
            while(k <= 0 or k > 3):
                print("Opção inválida. Digite uma das opções disponíveis")
                k = int(input())

            if(k == 1):
                selectionSort(lista)
                break
            elif(k == 2):
                shellSort(lista)
                break
            elif(k == 3):
                bucket_sort(lista)
                break

        elif(n == 2):
            print("Qual Estado deseja analisa? \n (1) - São Paulo \n (2) - Rio de Janeiro \n (3) - Minas Gerais \n (4) - Espírito Santo \n (5) - Todos")
            op = int(input())
            while(op <= 0 or op > 5):
                print("Opção inválida. Digite uma das opções disponíveis")
                op = int(input())
            if(op == 1):
                lista = SP
            elif(op == 2):
                lista = RJ
            elif(op == 3):
                lista = MG
            elif(op == 4):
                lista = ES
            elif(op == 5):
                lista = SP + RJ + MG + ES

            print("Qual algoritmo deseja utilizar? \n (1) - Selection Sort \n (2) - Shell Sort \n (3) - Bucket Sort")
            k = int(input())

            while(k <= 0 or k > 3):
                print("Opção inválida. Digite uma das opções disponíveis")
                k = int(input())
            if(k == 1):
                selectionSort(lista)
                break
            elif(k == 2):
                shellSort(lista)
                break
            elif(k == 3):
                bucket_sort(lista)
                break

        elif(n == 3):
            print("Qual Estado deseja analisa? \n (1) - São Paulo \n (2) - Rio de Janeiro \n (3) - Minas Gerais \n (4) - Espírito Santo \n (5) - Todos")
            op = int(input())
            while(op <= 0 or op > 5):
                print("Opção inválida. Digite uma das opções disponíveis")
                op = int(input())
            if(op == 1):
                lista = SP
            elif(op == 2):
                lista = RJ
            elif(op == 3):
                lista = MG
            elif(op == 4):
                lista = ES
            elif(op == 5):
                lista = SP + RJ + MG + ES

            print("Qual algoritmo deseja utilizar? \n (1) - Selection Sort \n (2) - Shell Sort \n (3) - Bucket Sort")
            k = int(input())

            while(k <= 0 or k > 3):
                print("Opção inválida. Digite uma das opções disponíveis")
                k = int(input())
            if(k == 1):
                selectionSort(lista)
                break
            elif(k == 2):
                shellSort(lista)
                break
            elif(k == 3):
                bucket_sort(lista)
                break

        elif(n == 4):
            print("Qual Estado deseja analisa? \n (1) - São Paulo \n (2) - Rio de Janeiro \n (3) - Minas Gerais \n (4) - Espírito Santo \n (5) - Todos")
            op = int(input())
            while(op <= 0 or op > 5):
                print("Opção inválida. Digite uma das opções disponíveis")
                op = int(input())
            if(op == 1):
                lista = SP
            elif(op == 2):
                lista = RJ
            elif(op == 3):
                lista = MG
            elif(op == 4):
                lista = ES
            elif(op == 5):
                lista = SP + RJ + MG + ES

            print("Qual algoritmo deseja utilizar? \n (1) - Selection Sort \n (2) - Shell Sort \n (3) - Bucket Sort")
            k = int(input())

            while(k <= 0 or k > 3):
                print("Opção inválida. Digite uma das opções disponíveis")
                k = int(input())
            if(k == 1):
                selectionSort(lista)
                break
            elif(k == 2):
                shellSort(lista)
                break
            elif(k == 3):
                bucket_sort(lista)
                break
        else:
            print("Opção inválida. Digite uma das opções disponíveis")
    arquivo.close()
#    print(SP)
