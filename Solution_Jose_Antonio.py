# ADVENT OF CODE 2022 DAY 6
# JOSE ANTONIO LOPES PAIVA JUNIOR

# A parte 1 do exercício usa uma sequência de 4 caracteres únicos para um start-of-packet, e a parte 2 usa uma sequência de 14 caracteres únicos
# Para obter o resultado da parte 2 basta mudar a variável
NUM_SEQUENCE_PART_ONE = 4
NUM_SEQUENCE_PART_TWO = 14

def find_start_of_packet(message):
    # Percorre a mensagem tendo i como index
    for i in range(len(message)):
        # Caso a mensagem chegue nos últimos 4 (ou 14) caracteres, ela para de percorrer, pois nesse caso não poderá mais ser um start-of-packet
        if i < (len(message) - (NUM_SEQUENCE_PART_ONE - 1)):
            # o set() é uma coleção que retorna dados exclusivos (que não se repetem)
            # caso o tamanho do set retornado seja igual a 4 (ou 14) (ou seja, os 4 (ou 14) elementos são exclusivos) então significa que aqueles quatro elementos são únicos e não tem caracteres que se repetem
            if(len(set(message[i:i+NUM_SEQUENCE_PART_ONE])) == len(message[i:i+NUM_SEQUENCE_PART_ONE])):
                # mostra o índice do último elemento de um start-of-packet (marker)
                print(f'o indice é: {i + NUM_SEQUENCE_PART_ONE}')
                break

# Recebe uma mensagem como input
print('insira a mensagem:\n')
input_message = input()

find_start_of_packet(input_message)