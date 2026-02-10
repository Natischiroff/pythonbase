while True:
    try:
        idade = int(input("Qual a sua idade?"))
        if idade <= 0:
            print("A idade não aceita zero e números negativos")
        else:
            print("Idade Cadastrada: ", idade)
            break
    except ValueError:
        print("Idade inválida! Digite apenas números.")

print("Idade cadastrada:", idade)