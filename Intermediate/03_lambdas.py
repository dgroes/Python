# Lambda: Pequeña función anónima, definida sin nombre que contiene una sola expresión
# C018: Lambda


def funcion_normal():
    print


sum_two_values = lambda first_value, second_value: first_value + second_value

print(sum_two_values(2, 4))

multiply_values = lambda first_value, second_value: print(first_value * second_value)



multiply_values(3,4)
