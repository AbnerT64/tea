# Tendencias e Innovacion en Tecnologia Agricola (TEA)

horas = input("horas trabajadas? ") 
valorporhora = input("valor por hora? ") 

#se utiliza la conversion de tipo a int
# sino se hace la coversion exiatira error porque trata de multiplicar strings
total=int(horas)*float(valorporhora) 
print("usted ha recibido: ") 
print(total) 