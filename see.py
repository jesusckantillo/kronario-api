from config.crud import crud

def generate_combinations(elements, length):
    combinations = []
    backtrack(elements, length, [], combinations)
    return combinations

def backtrack(elements, length, current_combination, combinations):
    if len(current_combination) == length:
        combinations.append(current_combination)
        return

    for i in range(len(elements)):
        new_combination = current_combination + [elements[i]]
        if len(new_combination) <= length:
            backtrack(elements[i+1:], length, new_combination, combinations)

# Ejemplo de uso
info = crud.get_allnrc_bycc(["MAT1111","FIS1023"])
elements = ['A', 'B', 'C', 'D']
length = 2
all_combinations = generate_combinations(info, length)
print(all_combinations)
