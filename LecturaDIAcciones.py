from pymodbus.client import ModbusTcpClient

def leerestadoDI():
    # Modbus TCP server configuration
    lista =[]
    server_ip = '192.168.4.220'  # Replace with your server's IP address
    server_port = 502           # Default Modbus TCP port
    
    # Create a Modbus TCP client
    client = ModbusTcpClient(server_ip, server_port)

    # Connect to the Modbus server with a timeout
    # connection_result = client.connect()

    # Read device information
    try:
        response=client.read_holding_registers(300,1)
        #print(response.registers[0]) da un número entero con el que indica los estados de las entradas
        binary = format(response.registers[0], '0{}b'.format(6)) #Formatear lo leido con modbus a un binario y añadir 0 hasta tener 5 digitos
        
        #Leer cada digito de la variable y añadirla a una lista    
        for digit in binary:
            lista.append(int(digit))
        lista = list(reversed(lista))
        
    except Exception as e:
        print(f"Error leyendo ADAM: {e}")
    # Close the Modbus connection
    client.close()
    
    return lista
        
def activarluz():
    server_ip = '192.168.4.220'  # Replace with your server's IP address
    server_port = 502           # Default Modbus TCP port
    luzactivada=1
    # Create a Modbus TCP client
    client = ModbusTcpClient(server_ip, server_port)

    # Connect to the Modbus server with a timeout
    connection_result = client.connect()

    if connection_result:
        # print("Modbus device is reachable.")
        # Value to write to a single holding register
        value_to_write = 1

        # Write to a single holding register at address 301
        write_result = client.write_register(302, value_to_write)
        
        # Check if the write was successful
        """ if write_result.isError():
            print(f"Write error: {write_result}")
        else:
            print("Write successful.")
        
    else:
        print("Modbus device is not reachable.") """
    # Close the Modbus connection
    client.close()
    return luzactivada

def desactivarluz():
    server_ip = '192.168.4.220'  # Replace with your server's IP address
    server_port = 502           # Default Modbus TCP port

    # Create a Modbus TCP client
    client = ModbusTcpClient(server_ip, server_port)

    # Connect to the Modbus server with a timeout
    connection_result = client.connect()

    if connection_result:
        #print("Modbus device is reachable.")
        # Value to write to a single holding register
        value_to_write = 0

        # Write to a single holding register at address 301
        write_result = client.write_register(302, value_to_write)
        
        # Check if the write was successful
        """ if write_result.isError():
            print(f"Write error: {write_result}")
        else:
            print("Write successful.") """
        
    #else:
        #print("Modbus device is not reachable.")
        
    # Close the Modbus connection
    client.close()

estadoluz=0
while True:
    listaa=leerestadoDI()    
    for i in range(len(listaa)):
        if listaa[0]==1 and estadoluz==0:
            estadoluz=activarluz()
            print("Activar")
        elif listaa[0]==0 and estadoluz==1:
            print("Desactivar")
            desactivarluz()
            estadoluz=0


