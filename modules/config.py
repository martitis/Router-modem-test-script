import json
from os import close
import serial
import paramiko
import modules.logger as logger


class config:

    __config_file_name__ = "config.json"

    __config__ = None

    productName = None

    def __init__(self):
        try:
            tmpConf = open(self.get_config_file_name())
            tmpString = tmpConf.read().replace('\n', '')
            self.__config__ = json.loads(tmpString)
            tmpConf.close()
        except:
            print("Error opening config file")
            logger.log.Write("Error opening config file")
            exit()

    def getProductInfo(self, productName):
        product = None
        for line in self.__config__['product']:
            if line['name'] == productName:
                return line

        return product

    def get_con_type(self, product):
        if product['config']['type'] == "serial":
            return "serial"
                    
        elif product['config']['type'] == "ssh":
            return "ssh"

        else:
            return None

    def get_ssh(self, product):
        return product['config']['ip'], product['config']['port'], product['config']['username'], product['config']['password']

    def get_serial(self, product):
        return  product['config']['device'], product['config']['baudrate']


    def get_config_file_name(self):
        return self.__config_file_name__


if __name__ == "modules.config":
    config = config()