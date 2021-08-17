import paramiko
from modules import config
import time

class Send:

    # def __del__(self):
    #     ssh.close()

    def Serial(cmd_line, ser):
        cmd_B = bytes(cmd_line, 'utf-8')
        out = ''
        ser.write(cmd_B + b"\r\n")
        time.sleep(1)
        while ser.inWaiting() > 0:
            out += ser.read(1).decode("utf-8")
        return out

    def SSH(cmd_line, channel):
        if cmd_line[-4:][0] == "\\":
            channel.send(cmd_line[:-4] + '\n')
            channel.send("\032".encode("utf8"))
            time.sleep(2)
        else:
            channel.send(cmd_line + '\n')

        while not channel.recv_ready():
            time.sleep(1)
        out = channel.recv(9999)
        return out.decode("utf8")

    def SSH_Bytes(line, channel):
        channel.send(line.encode("utf8"))
