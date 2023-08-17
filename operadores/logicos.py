a = True
b = False

resultado_and = a and b  # True si ambos a y b son True, de lo contrario False
resultado_or = a or b    # True si al menos uno de a o b es True, de lo contrario False
resultado_not_a = not a  # True si a es False, de lo contrario False
resultado_not_b = not b  # True si b es False, de lo contrario False

print("AND lógico:", resultado_and)
print("OR lógico:", resultado_or)
print("NOT lógico para a:", resultado_not_a)
print("NOT lógico para b:", resultado_not_b)


a = True
b = False

resultado_and = a & b     # AND lógico: True si ambos a y b son True, de lo contrario False
resultado_or = a | b      # OR lógico: True si al menos uno de a o b es True, de lo contrario False
resultado_not_a = ~a      # NOT lógico para a: True si a es False, de lo contrario False
resultado_not_b = ~b      # NOT lógico para b: True si b es False, de lo contrario False

print("AND lógico:", resultado_and)
print("OR lógico:", resultado_or)
print("NOT lógico para a:", resultado_not_a)
print("NOT lógico para b:", resultado_not_b)

