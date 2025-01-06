#Attenuator interface

import USB_RUDAT

# Initialize the device
U1 = USB_RUDAT.USBDAT()

# Connect to the device
if not U1.Connect():
    print("Failed to connect to the device! Please check the connection and try again.")
    exit()

print("Device connected successfully!")
print("Device Model:", U1.Send_SCPI(":MN?"))
print("Serial Number:", U1.ReadSN())

def set_attenuation(channel, value):
    """Set the attenuation value for a specific channel."""
    if 1 <= channel <= 4:
        cmd = f":CHAN:{channel}:SETATT:{value}"
        U1.Send_SCPI(cmd)
        print(f"Channel {channel} attenuation set to {value} dB.")
    else:
        print("Invalid channel. Please select a channel between 1 and 4.")

def set_attenuation_sequential():
    """Set attenuation for all channels sequentially."""
    for channel in range(1, 5):
        value = float(input(f"Enter attenuation value for Channel {channel} (in dB): "))
        set_attenuation(channel, value)
    print("All channels have been configured sequentially.")

def query_attenuation(channel=None):
    """Query the attenuation value for a specific channel or all channels."""
    if channel:
        if 1 <= channel <= 4:
            cmd = f":CHAN:{channel}:ATT?"
            response = U1.Send_SCPI(cmd)
            print(f"Channel {channel} attenuation: {response} dB.")
        else:
            print("Invalid channel. Please select a channel between 1 and 4.")
    else:
        cmd = ":ATT?"
        response = U1.Send_SCPI(cmd)
        print(f"All channel attenuations: {response}")

def menu():
    """Display the menu and handle user input."""
    while True:
        print("\n--- Mini-Circuits Attenuator Control ---")
        print("1. Set attenuation for a specific channel")
        print("2. Set attenuation for all channels sequentially")
        print("3. Query attenuation for a specific channel")
        print("4. Query attenuation for all channels")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            channel = int(input("Enter channel number (1-4): "))
            value = float(input("Enter attenuation value (in dB): "))
            set_attenuation(channel, value)
        elif choice == "2":
            set_attenuation_sequential()
        elif choice == "3":
            channel = int(input("Enter channel number (1-4): "))
            query_attenuation(channel)
        elif choice == "4":
            query_attenuation()
        elif choice == "5":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the menu for user interaction
menu()

# Disconnect the device when done
U1.Disconnect()
print("Device disconnected.")
