# Trecho de código fornecido na questão:
int INDICE = 12, SOMA = 0, K = 1;

while K < INDICE {
    K = K + 1;
    SOMA = SOMA + K;
}
print(SOMA);

# Volta 1: K = 2, SOMA = 2
# Volta 2: K = 3, SOMA = 5
# Volta 3: K = 4, SOMA = 9
# Volta 4: K = 5, SOMA = 14
# Volta 5: K = 6, SOMA = 20
# Volta 6: K = 7, SOMA = 27
# Volta 7: K = 8, SOMA = 35
# Volta 8: K = 9, SOMA = 44
# Volta 9: K = 10, SOMA = 54
# Volta 10: K = 11, SOMA = 65
# VOlta 11: K = 12, SOMA = 77

# Ao final do loop de 11 voltas, o valor de SOMA será 77.
