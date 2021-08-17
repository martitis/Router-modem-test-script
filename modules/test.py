import serial
from modules import config
from modules import logger
# from colorama import Fore
from modules import sendCommands
from modules import connect

class RunTest:
    protocol = None

    def Start(self, product):
        conType = config.config.get_con_type(product)
        if conType == None:
            exit()

        if conType == "serial":
            device, baudrate = config.config.get_serial(product)
            serialCon = connect.Connection.Serial(device, baudrate)
            if serialCon == None:
                exit()
            self.runSerial(serialCon, product)

        elif conType == "ssh":
            ip, port, user, pw = config.config.get_ssh(product)
            sshCon = connect.Connection.ssh(ip, port, user, pw)
            self.runSSH(sshCon, product)
            
        else:
            print("Protocol not found")
            exit(5)
        


    def DeterminateProtocol(self, pName):

        for product in config.config.__config__['product']:
            if product['name'] == pName:
                if product['config']['type'] == "serial":
                    return "serial"
                    
                elif product['config']['type'] == "ssh":
                    return "ssh"

                else:
                    logger.Write("Error: Unknown connection protocol: " + product['config']['type'])
                    return None

    def runSerial(self, ser, prod):
        for product in prod['cmd_list']:
            try:
                result = sendCommands.Send.Serial(product['cmd'] + " " + product['args'], ser)
            except:
                logger.log.ToScreen("Error occured while sending serial command", 0)
                logger.log.Write("Error occured while sending serial command")
                exit(1)
            logger.log.Write(product['cmd'], (product['result'] in result),result)
            logger.log.ToScreen(product['cmd'], (product['result'] in result))


    def runSSH(self, ssh, prod):
        channel = ssh.invoke_shell()
        sendCommands.Send.SSH("/etc/init.d/gsmd stop", channel)
        sendCommands.Send.SSH("socat /dev/tty,raw,echo=0,escape=0x03 /dev/ttyUSB3,raw,setsid,sane,echo=0,nonblock ; stty sane", channel)
        for product in prod['cmd_list']:
            result = sendCommands.Send.SSH(product['cmd'] + product['args'], channel)
            logger.log.Write(product['cmd'], (product['result'] in result),result)
            logger.log.ToScreen(product['cmd'], (product['result'] in result))
            
        channel.send("\003".encode("utf8")) # ctrl-c
        sendCommands.Send.SSH("/etc/init.d/gsmd start", channel)
        channel.close()
        ssh.close()



if __name__ == "modules.test":
    RunTest = RunTest()