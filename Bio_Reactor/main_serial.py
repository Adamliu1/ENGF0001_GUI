import serial

#initial connection
port_COM = "/dev/pts/0"
serial = serial.Serial(port_COM ,9600)

def getdata():
    temp = serial.read(6)
    temp_val = temp.decode('utf-8')
    return temp_val


if __name__ == "__main__":
    while True:
        getdata()

    


