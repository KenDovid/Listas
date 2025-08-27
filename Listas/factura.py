print("¡Vegetales a la venta!")
veg = ["Tomates", "Cebollas", "Pimentones", "Lechugas", "Brocolí"]
val = [1000, 1500, 2000, 3000, 5000] 
print(veg)
print(val)

cantidad = []


for vegetal in veg:
    cantLlevar = int(input(f"¿Cuántos {vegetal} llevará? "))
    cantidad.append(cantLlevar)

print("================================================")
print("Factura Electrónica")
print("Supermercado verdurero")
print("================================================")

resultado = [x * y for x, y in zip(cantidad, val)]
for vegetal, cant, precio, subtotal in zip(veg, cantidad, val, resultado):
    print(f"{vegetal}: {cant} x {precio}$ = {subtotal}")

total = sum(resultado)
iva = total * 0.19
total_con_iva = total + iva 

print("================================================")
print(f"Subtotal: {total}$")
print(f"IVA (19%): {iva:2f}$")
print(f"Total a pagar: {total_con_iva:2f}$")