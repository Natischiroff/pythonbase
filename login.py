while True:
    try:
        nome = input("Digite seu nome de usuário: ").strip()
        senha = input("Digite sua senha:").strip()

        if nome == "":
            print("O nome não pode ser vazio.")
        else:
            if len(senha) >= 6:
                break
            else:
                print("A senha deve ter 6 caracteres.")
    except ValueError:
        print("Entrada inválida. Tente novamente.")

print("Nota registrada!", nome)
print("Bem-vindo, " + nome)