precio_unitario = float(input("Ingrese el precio del producto: "))
cantidad = int(input("Ingrese la cantidad que desea comprar: "))

subtotal = precio_unitario * cantidad
iva = subtotal * 0.16
total = subtotal + iva

print("Subtotal: $", round(subtotal, 2))
print("IVA (16%): $", round(iva, 2))
print("Total a pagar: $", round(total, 2))