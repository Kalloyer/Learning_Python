try:
    a = int(input("Numerador: "))
    b = int(input("Denominador: "))
    r = a / b
except (ValueError, TypeError):
    print("Tivemos um problema com os tipos de dados digitados")
except ZeroDivisionError:
    print("Não é possível dividir o número por zero")
except KeyboardInterrupt:
    print("O usuário não informou os dados")
else:
    print(f"O resultado é {r}")       
finally:
    print("Volte sempre, muito obrigado!")
