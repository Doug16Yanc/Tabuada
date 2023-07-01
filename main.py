def main():

    print("Bem-vindo(a) ao nosso sistema da tabuada de multiplicação de números:")

    valor = True

    while(valor):

        opcao = int(input("Digite 0 para tabuada ou -1 para encerrar o programa."))


        if (opcao == 0):

            numero = int(input("Digite um número menor entre 1 e 9 (inclusive) para que eu mostre a tabuada:"))

            for i in range(1, 11):
                produto = numero*i

                print(f"{numero} X {i} = {produto}")

        elif (opcao == -1):
            break;

if __name__:
    main()