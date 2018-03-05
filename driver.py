import dynamixel_functions as dynamixel                     # Uses Dynamixel SDK library

#Name of connected USB device
device_name = "/dev/ttyUSB0".encode('utf-8')

# Control table address
ADDR_TORQUE_ENABLE       = 24                            # Control table address is different in Dynamixel model
ADDR_GOAL_POSITION       = 30
ADDR_PRESENT_POSITION    = 36
ADDR_BAUDRATE            =  4
ADDR_TORQUE              = 14
ADDR_I                   = 27
ADDR_OFFSET              = 20

#Other values
PROTOCOL_VERSION            = 1                             # See which protocol version is used in the Dynamixel
BAUDRATE                    = 1000000                       # Some motors had BAUDRATE = 57600
TORQUE_ENABLE               = 1                             # Value for enabling the torque
TORQUE_DISABLE              = 0                             # Value for disabling the torque
COMM_SUCCESS                = 0                             # Communication Success result value
COMM_TX_FAIL                = -1001                         # Communication Tx Failed
PORT = dynamixel.portHandler(device_name)                   # Initialize PortHandler Structs, set the port path and
                                                            # get methods and members of PortHandlerLinux or PortHandlerWindows


def init():
    dynamixel.packetHandler()                               # Initialize PacketHandler Structs
    if dynamixel.openPort(PORT):                            # Open port
        print("Succeeded to open the port!")
    else:
        print("Failed to open the port!")
        quit()
    if dynamixel.setBaudRate(PORT, BAUDRATE):               # Set port baudrate
        print("Succeeded to set the baudrate!")
    else:
        print("Failed to change the baudrate!")
        quit()

def comm_error():
    dxl_comm_result = dynamixel.getLastTxRxResult(PORT, PROTOCOL_VERSION)
    dxl_error = dynamixel.getLastRxPacketError(PORT, PROTOCOL_VERSION)

    if dxl_comm_result != COMM_SUCCESS:
        print(dynamixel.getTxRxResult(PROTOCOL_VERSION, dxl_comm_result))
    elif dxl_error != 0:
        print(dynamixel.getRxPacketError(PROTOCOL_VERSION, dxl_error))
    else:
        return 0
    return 1


def activate(ID):
    dynamixel.write1ByteTxRx(PORT, PROTOCOL_VERSION, ID+1, ADDR_TORQUE_ENABLE, TORQUE_ENABLE)
    if not comm_error():
        return 1
    return 0

def read_position(ID):
    position = dynamixel.read2ByteTxRx(PORT, PROTOCOL_VERSION, ID+1, ADDR_PRESENT_POSITION)
    if not comm_error():
        return position

def set_goal(ID, goal):
    dynamixel.write2ByteTxRx(PORT, PROTOCOL_VERSION, ID+1, ADDR_GOAL_POSITION, goal)
    if not comm_error():
        return 1
    return 0

def set_I(ID, I):
    dynamixel.write1ByteTxRx(PORT, PROTOCOL_VERSION, ID+1, ADDR_I, I)
    if not comm_error():
        return 1
    return 0

def set_offset(ID, offset):
    dynamixel.write2ByteTxRx(PORT, PROTOCOL_VERSION, ID+1, ADDR_OFFSET, offset)
    if not comm_error():
        return 1
    return 0

def read_offset(ID):
    offset = dynamixel.read2ByteTxRx(PORT, PROTOCOL_VERSION, ID+1, ADDR_OFFSET)
    if not comm_error():
        return offset

def read_max_torque(ID):
    torque = dynamixel.read2ByteTxRx(PORT, PROTOCOL_VERSION, ID+1, ADDR_TORQUE)
    if not comm_error():
        return torque

def change_baudrate(ID, baudrate_level):
    dynamixel.write2ByteTxRx(PORT, PROTOCOL_VERSION, ID+1, ADDR_BAUDRATE, baudrate_level)
    if not comm_error():
        return 1
    return 0

def deactivate(ID):
    dynamixel.write1ByteTxRx(PORT, PROTOCOL_VERSION, ID+1, ADDR_TORQUE_ENABLE, TORQUE_DISABLE)
    if not comm_error():
        return 1
    return 0

def close_port():
    dynamixel.closePort(PORT)




