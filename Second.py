# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

def inputNumbers(numbers):
    xyz = ["X", "Y", "Z"]
    list = []
    for i in range(numbers):
        a.append(input(f"Введите значение {xyz[i]}: "))
    return list


def checkPredicate(numbers):
    left = not (numbers[0] or numbers[1] or numbers[2])
    right = not numbers[0] and not numbers[1] and not numbers[2]
    result = left == right
    return result


statement = inputNumbers(3)

if checkPredicate(statement) == True:
    print(f"Утверждение истинно")
else:
    print(f"Утверждение ложно")