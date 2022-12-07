try:
    numero = int(input("Digite o numero"))
    print(numero)

    10/0
except ZeroDivisionError:
    print("Divisao por zero não é possivel")
except ValueError:
    print("digite um valor valido")
except:
    print("Erro inesperado")
finally:
    print("executa sempre")