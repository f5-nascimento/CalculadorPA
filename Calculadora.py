#O PROGRAMA CONSISTE EM UM CALCULADOR DE PROGRESSÕES ARITMÉTICAS UTIZANDO PYTHON
#O PROGRAMA EXIGE TESTES


carga = int(input("DIGITE 0 PARA CARREGAR CALCULADORA "))

while carga == 0:
    seletor = input("SEJA BEM VINDO AO CALULADOR DE PROGRESSÕES ARITMÉTICAS" + "\n" +
                    " " + "\n" +
                    "Digite 1 para calcular AN " + "\n" +
                    "Digite 2 para calcular AM:" + "\n" +
                    "Digite 3 para calcular N:" + "\n" +
                    "Digite 4 para calcular M:" + "\n" +
                    "Digite 5 para calcular R:" + "\n" +
                    "Digite 6 para calcular SOMA: " + "\n" +
                    "-> ")
    print(" ")

    #ENCONTRAR O ENÉSIMO TERMO DE UMA PA
    if seletor == "1":
        am = int(input("Digite o valor de AM: "))
        m  = int(input("Digite a posição que AM ocupa: "))
        n  = int(input("Digite a posição que AN ocupa: "))
        r  = float(input("Digite a razão da PA: "))
        an = am + (n-m) * r


        print(an)

    # ENCONTRAR O PRIMEIRO TERMO CONHECIDO DE UMA PA
    elif seletor == "2":
        an = int(input("Digite o valor de AN: "))
        n = int(input("Digite a posição que AN ocupa: "))
        m  = int(input("Digite a posição que AM ocupa: "))
        r = float(input("Digite a razão da PA: "))
        am = an - (m-n) * r

        print(am)

    # ENCONTRAR A QUANTIDADE DE ELEMENTOS DE UMA PA
    elif seletor == "3":
        am = int(input("Digite o valor de AM: "))
        m  = int(input("Digite a posição que AM ocupa: "))
        an = int(input("Digite o valor de AN: "))
        r = float(input("Digite a razão da PA: "))
        n = (an - am + m*r)/ (m*r)

        print(n)


    # ENCONTRAR A POSIÇÃO DO PRIMEIRO ELEMENTO CONHECIDO DE UMA PA
    elif seletor == "4":
        am = int(input("Digite o valor de AM: "))
        an = int(input("Digite o valor de AN: "))
        n  = int(input("Digite a posição que AN ocupa: "))
        r = float(input("Digite a razão da PA: "))
        m = (am - an + n * r) / r



        print(m)

    # ENCONTRAR A RAZÃO DE UMA PA
    elif seletor == "5":
        am = int(input("Digite o valor de AM: "))
        m  = int(input("Digite a posição que AM ocupa: "))
        an = int(input("Digite o valor de AN: "))
        n  = int(input("Digite a posição que AN ocupa: "))
        r = (an - am)/ (n-m)

        print(r)

    # ENCONTRAR A SOMA DE TODOS OS TERMOS DE UMA PA
    elif seletor == "6":
        am = int(input("Digite o primeiro termo de AM: "))
        an = int(input("Digite o último termo da PA "))
        n = int(input("Digite a quantidade de termos da PA: "))
        soma = (am + an) * (n / 2)

        print(soma)

    else:
        print("Você digitou uma opção inválida, calculadora encerrada")
        exit()

    print("")
    carga = int(input("DIGITE 0 CASO DESEJE REALIZAR UM NOVO CÁLCULO "))

else:
    exit()
