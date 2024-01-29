from pymodbus.client import ModbusTcpClient

# Modbus TCP server configuration
server_ip = '192.168.4.220'  # Replace with your server's IP address
server_port = 502           # Default Modbus TCP port

# Create a Modbus TCP client
client = ModbusTcpClient(server_ip, server_port)

    # Connect to the Modbus server with a timeout
connection_result = client.connect()

if connection_result:
    print("Modbus device is reachable.")
else:
    print("Modbus device is not reachable.")

# Close the Modbus connection
client.close()