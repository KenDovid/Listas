# ---------------------------------------------
# DEMOSTRACIÓN DE LISTAS EN PYTHON
# ---------------------------------------------

frutas = ["Manzana", "Banano", "Cereza", "Naranja", "Pera", "Kiwi"]
print("Lista inicial:", frutas)

# Acceso
print("Índice 0:", frutas[0])
print("Índice 2:", frutas[2])
print("Índice -1:", frutas[-1])
print("Índice -2:", frutas[-2])
print("Rango [1:3]:", frutas[1:3])
print("Rango [:4]:", frutas[:4])
print("Rango [2:]:", frutas[2:])
print("Slicing [:]:", frutas[:])
print("Saltos [::2]:", frutas[::2])
print("Invertida [::-1]:", frutas[::-1])

# Append
frutas.append("Mango")
print("Append:", frutas)

# Insert
frutas.insert(1, "Fresa")
print("Insert:", frutas)

# Extend
frutas.extend(["Uva", "Sandía"])
print("Extend:", frutas)

# Index
print("Index 'Cereza':", frutas.index("Cereza"))

# Remove
frutas.remove("Fresa")
print("Remove:", frutas)

# Pop
print("Pop(2):", frutas.pop(2))
print("Lista:", frutas)

# Clear
frutas.clear()
print("Clear:", frutas)

# Métodos extra
numeros = [5, 3, 8, 3, 2, 8, 1]
print("\nLista números:", numeros)
print("Count(3):", numeros.count(3))
numeros.sort()
print("Sort:", numeros)
numeros.reverse()
print("Reverse:", numeros)
print("Copy:", numeros.copy())
