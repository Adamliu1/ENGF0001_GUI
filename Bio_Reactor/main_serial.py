import serial

#initial connection
port_COM = "/dev/pts/2"
serial = serial.Serial(port_COM ,9600)

def getdata():
    print(serial.read())



if __name__ == "__main__":
    getdata()




