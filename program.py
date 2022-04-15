from datetime import datetime

# Escribe los logs en un archivo
def log(msg):
    with open("log.txt", 'a+') as file:
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        file.write(f"{current_time} {msg}\n")
        
# Verifica si cumple el largo máximo permitido
def is_large(inp, msg=""):
    if len(inp) > 255:
        print(f"Entrada {msg} excede el largo máximo permitido (255 caracteres)")
        log(f"Entrada {msg} excede el largo máximo permitido (255 caracteres)")
        exit()

# Verifica si los caracteres utilizados son ascii    
def is_ascii(inp, msg=""):
    if not inp.isascii():
        print(f"Entrada {msg} no permitida")
        log(f"Entrada {msg} no permitida")
        exit()

# Compara las secuencias para ver si son iguales 
def compare_seq(seq_a, seq_b):
    is_equal = True
    if len(seq_a) != len(seq_b):
        is_equal = False
    else:
        while seq_a:
            if seq_a.pop() != seq_b.pop():
                is_equal = False
                break
                
    return is_equal

# Obtiene la entrada del usuario     
def get_input():
    input_a = input("Ingrese la secuencia 1: ")
    input_b = input("Ingrese la secuencia 2: ")

    is_large(input_a, "A")
    is_large(input_b, "B")

    is_ascii(input_a, "A")
    is_ascii(input_b, "B")
    
    return input_a, input_b

# Almacena las secuencias en una pila   
def to_stack(input_a, input_b):
    seq_a = []
    for s in input_a:
        seq_a.append(s)

    seq_b = []
    for s in input_b:
        seq_b.append(s)
        
    return seq_a, seq_b

if __name__ == "__main__":
    input_a, input_b = get_input()
    seq_a, seq_b = to_stack(input_a, input_b)
    is_equal = compare_seq(seq_a, seq_b)
    
    if is_equal:
        log(f"{input_a}, {input_b}, Iguales")
        print("Iguales")
    else:
        log(f"{input_a}, {input_b}, No Iguales")
        print("No Iguales")