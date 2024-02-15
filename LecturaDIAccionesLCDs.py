from pymodbus.client import ModbusTcpClient
import minimalmodbus
import serial

# Flag para lanzar las funciones cuando hay que lanzarlas
estadoluz=0

#Leer estado de las entradas digitales del ADAM
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

#Función especifica que coje las dos variables de direccion y valor.
def escrituraenesclavo(direccion, valor):
    estado=1
    port = 'COM7'  # Change this to the appropriate COM port on your system
    baudratevar = 9600
        
    # Configure the Modbus RTU instrument
    ser = serial.Serial(port, baudrate=baudratevar, bytesize=8, parity='N', stopbits=1, timeout=1)
    instrument = minimalmodbus.Instrument(ser, direccion, mode='rtu', close_port_after_each_call=True)

    # Write to a holding register
    register_address = 7 # Change this to the register address you want to write to // el 7 es para enviarle un número
    try:
        # Write to the register
        instrument.write_register(register_address, valor)
            
        # Print the result
        print(f"Value {valor} written to register {register_address}")

    except Exception as e:
        print(f"Error writing to Modbus register: {e}")

    finally:
        # Close the serial port
        ser.close()
    return estado

#
def escribirzero(direccion):
    estado=0
    # Configure the serial port
    port = 'COM7'  # Change this to the appropriate COM port on your system
    baudratevar = 9600
    ser = serial.Serial(port, baudrate=baudratevar, bytesize=8, parity='N', stopbits=1, timeout=1) 
    
    # Configure the Modbus RTU instrument
    instrument = minimalmodbus.Instrument(ser, direccion, mode='rtu', close_port_after_each_call=True)

    # Write to a holding register
    value_to_write = 48 # Change this to the value you want to write

    try:
        # Write to the register
        instrument.write_register(0, value_to_write, functioncode=6)
        instrument.write_register(1, value_to_write, functioncode=6)

    except Exception as e:
        print(f"Error writing to Modbus register: {e}")

    finally:
        # Close the serial port
        ser.close()
        return estado


while True:
    
    listaa=leerestadoDI()
    
    if listaa[0]==1 and estadoluz==0:
        print("Activar")
        estadoluz=escrituraenesclavo(3,3)
        
        
    elif listaa[0]==0 and estadoluz==1:
        print("Desactivar")
        estadoluz=escribirzero(3)
        


