1
opcion = 100

print("***Empanadas inteligentes***")
print("1. Agregar clientes:")
print("2. mostrar clientes")
print("3. Buscar cliente por cedula: ")

print("0. sali")

#Diccionario
cliente = {}

#lista 
clientes=[]

while(opcion !=0):

    #pedimos la opcion deseada
    opcion = int(input("Digite la opcion preferida: "))

    #caminos del MENU
    if(opcion ==1):
        cliente['cedula'] =input("Digite su cedula: ")
        cliente['nombre'] =input("Digite su nombre: ")
        clientes.append(cliente)
        print(cliente)
    elif(opcion ==0):
        break
    elif(opcion ==2):
        print(clientes)
    elif(opcion ==3):
        cedulaABuscar =input("Digite la cedula: ")
        for cliente in clientes:
            if(cliente['cedula']==cedulaABuscar):
                print(f"Cliente encontrado: {cliente['cedula']}")
                break
            else:
                print("Usuario no encontrado")
                break


    else:
        print("Digite una opcion valida")
    
else:
    print("Adios")