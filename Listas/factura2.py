print("¡Bienvenido al Supermercado Verdulero!")
print("======================================")


veg = ["Tomates", "Cebollas", "Pimentones", "Lechugas", "Brócoli", "Zanahorias", "Papas", "Pepinos"]
val = [1000, 1500, 2000, 3000, 5000, 1200, 800, 1800]

# Mostrar catálogo
print("Lista de productos disponibles:")
for i in range(len(veg)):
    print(f"{i+1}. {veg[i]} - {val[i]}$")

print("======================================")

carrito = [0] * len(veg)  # lista inicializada en ceros

# Pedimos compras
continuar = "s"
while continuar.lower() == "s":
    opcion = int(input("Seleccione el número del vegetal que desea comprar: "))
    if 1 <= opcion <= len(veg):
        unidades = int(input(f"¿Cuántos {veg[opcion-1]} llevará? "))
        carrito[opcion-1] += unidades
    else:
        print("Opción inválida, intente de nuevo.")

    continuar = input("¿Desea comprar otro producto? (s/n): ")

# Factura
print("======================================")
print("Factura Electrónica")
print("Supermercado Verdulero")
print("======================================")

resultado = [x * y for x, y in zip(carrito, val)]
for vegetal, unidades, precio, subtotal in zip(veg, carrito, val, resultado):
    if unidades > 0:  # solo muestra los que compró
        print(f"{vegetal}: {unidades} x {precio}$ = {subtotal}$")

total = sum(resultado)
iva = total * 0.19
total_con_iva = total + iva 

print("======================================")
print(f"Subtotal: {total}$")
print(f"IVA (19%): {iva:.2f}$")
print(f"Total a pagar: {total_con_iva:.2f}$")
