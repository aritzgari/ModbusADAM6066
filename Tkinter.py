import tkinter as tk
from pymodbus.client import ModbusTcpClient

# Create the main window
window = tk.Tk()
window.title("Escribir al ADAM")

def button_click():
    lista=[]
    lista.append(do5_entry.get())
    lista.append(do4_entry.get())
    lista.append(do3_entry.get())
    lista.append(do2_entry.get())
    lista.append(do1_entry.get())
    lista.append(do0_entry.get())
    
    decimal_number = int("".join(map(str, lista)), 2)
    value_to_write = decimal_number
    
    # Modbus TCP server configuration
    server_ip = '192.168.4.220'  # Replace with your server's IP address
    server_port = 502           # Default Modbus TCP port

    # Create a Modbus TCP client
    client = ModbusTcpClient(server_ip, server_port)

    # Connect to the Modbus server with a timeout
    connection_result = client.connect()

    if connection_result:
        print("Modbus device is reachable.")
        
    # Write to a single holding register at address 301
    write_result = client.write_register(302, value_to_write)
    
    # Check if the write was successful
    if write_result.isError():
        print(f"Write error: {write_result}")
    else:
        print("Write successful.")
        
    # Close the Modbus connection
    client.close()
    
#Label del esclavo
do0_label = tk.Label(window, text="DO0: ")
do0_label.grid(row=0, column=0, padx=10, pady=5)

#Entrada del esclavo
do0_entry = tk.Entry(window)
do0_entry.grid(row=0, column=1, padx=10, pady=5)      
#Label del esclavo
do1_label = tk.Label(window, text="DO1: ")
do1_label.grid(row=1, column=0, padx=10, pady=5)

#Entrada del esclavo
do1_entry = tk.Entry(window)
do1_entry.grid(row=1, column=1, padx=10, pady=5)

#Label del esclavo
do2_label = tk.Label(window, text="DO2: ")
do2_label.grid(row=2, column=0, padx=10, pady=5)

#Entrada del esclavo
do2_entry = tk.Entry(window)
do2_entry.grid(row=2, column=1, padx=10, pady=5)

#Label del esclavo
do3_label = tk.Label(window, text="DO3: ")
do3_label.grid(row=3, column=0, padx=10, pady=5)

#Entrada del esclavo
do3_entry = tk.Entry(window)
do3_entry.grid(row=3, column=1, padx=10, pady=5)

#Label del esclavo
do4_label = tk.Label(window, text="DO4: ")
do4_label.grid(row=4, column=0, padx=10, pady=5)

#Entrada del esclavo
do4_entry = tk.Entry(window)
do4_entry.grid(row=4, column=1, padx=10, pady=5)

#Label del esclavo
do5_label = tk.Label(window, text="DO5: ")
do5_label.grid(row=5, column=0, padx=10, pady=5)

#Entrada del esclavo
do5_entry = tk.Entry(window)
do5_entry.grid(row=5, column=1, padx=10, pady=5)


# Button to trigger an action
button = tk.Button(window, text="Introducir", command=button_click)
button.grid(row=6, column=0, columnspan=2, pady=10)


# Start the tkinter event loop
window.mainloop()