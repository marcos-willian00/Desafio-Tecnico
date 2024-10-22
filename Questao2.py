def verificar_letra_a(string):
    quantidade = string.lower().count('a')

    if quantidade > 0:
        print(f"A letra 'a' aparece {quantidade} vezes na string.")
    else:
        print("A letra 'a' não aparece na string.")

string = input("Informe uma string: ")

verificar_letra_a(string)
