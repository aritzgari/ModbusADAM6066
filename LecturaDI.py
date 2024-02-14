from pymodbus.client import ModbusTcpClient

# Modbus TCP server configuration
server_ip = '192.168.4.220'  # Replace with your server's IP address
server_port = 502           # Default Modbus TCP port
lista =[]
# Create a Modbus TCP client
client = ModbusTcpClient(server_ip, server_port)

# Connect to the Modbus server with a timeout
connection_result = client.connect()

# Read device information
try:
    response=client.read_holding_registers(300,1)
    #print(response.registers[0]) da un número entero con el que indica los estados de las entradas
    binary = format(response.registers[0], '0{}b'.format(6)) #Formatear lo leido con modbus a un binario y añadir 0 hasta tener 5 digitos
    
    #Leer cada digito de la variable y añadirla a una lista    
    for digit in binary:
        lista.append(int(digit))
    """  print(lista)
    print(lista[0])
    print(lista[1])
    print(lista[2])
    print(lista[3])
    print(lista[4]) """
    
except Exception as e:
    print(f"Error leyendo ADAM: {e}")
    
for i in range(len(lista)):
    if lista[i] == 1:
        print(f"DI{i}: 1")
    else:
        print(f"DI{i}: 0")


# Close the Modbus connection
client.close()