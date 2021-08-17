from modules import config
from modules import logger
import paramiko
import os
import serial

class Connection:

    def ssh(self, ip, port, username, password):
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
            ssh.connect(hostname=ip, port=port,username=username, password=password, timeout=5)
        except paramiko.AuthenticationException:
            print("SSH Authentication Error")
            logger.log.Write("SSH Authentication Error", 0, "")
            exit(1)
        except:
            print("Connection failed")
            logger.log.Write("Connection failed", 0, "")
            exit(1)

        print("Successful connection to: " + ip)
        return ssh


    def Serial(self, port, baudrate):
        ser = serial.Serial()
        ser.port = port
        ser.baudrate = baudrate

        if os.geteuid() != 0:
            logger.Write("insufficient permissions (You need run script as root!)", 0, "")
            print("insufficient permissions (You need run script as root!)")
            exit(1)
        try:
            ser.open()
            print("Connected: " + ser.port)
            return ser
        except:
            print("Serial Connection error")
            logger.log.Write("Connection error", 0, "")
            return None


if __name__ == "modules.connect":
    Connection = Connection()