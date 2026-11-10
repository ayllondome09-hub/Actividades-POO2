notas=[10,8,9,5]
print(notas[1])
notas.append(20)
print(max(notas))
notas.insert(1,10)
print (len(notas))
print(notas[-1])
print(sum(notas))
print(notas[0])
print(notas[-2])
print(notas[2])
print(min(notas))
notas.remove(9)
notas=sorted(notas)
print(notas[2:])
print(notas[:2])

meses=["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"]
print(meses[0])
print(meses[-1])
##meses=["marzo"]=junio

estudiantes={
    "cedula":"123456789",
    "nombre":"Juan",
    "correo":"juan@ejemplo.com",
    "celular":"1234567890",
    "notas":[10,9,5,4]

}
print(estudiantes.get("nombre"))
print(estudiantes.keys)

conjunto_a={1,1,5,4,6,8}
conjunto_b={1,9,6,5,4}
print(conjunto_a & conjunto_b)
print(conjunto_a | conjunto_b)

