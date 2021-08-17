from modules import config
from pathlib import Path
from datetime import datetime
import os
from colorama import Fore

class log:

    def __init__(self):
        self.f = None
    passCount = 0
    failCount = 0
    log_name = None

    def start_log(self, variable = None):
        self.log_name = "./logs/" + config.config.productName + " [" + datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "].csv"
        if not os.access(self.log_name, os.W_OK):
            self.f = open(self.log_name, "a")
            self.f.write("time,command,result,response\n")
            self.f.write("Log started at:" + datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")
        else:
            print("Failed to create log: ," + self.log_name)
            print("Terminating...,")
            exit(1)

    def Write(self, line, status, result):
        now = datetime.now().strftime("%H:%M:%S")
        if status:
            self.f.write("[{}]: ".format(now) + "," + line + ",PASSED:,\"" + result + "\"\n")
        else:
            self.f.write("[{}]: ".format(now) + "," + line + ",FAIL:,\"" + result + "\"\n")

    def ToScreen(self, line, status):
        os.system('clear')
        if status:
            self.passCount += 1
            print("Passed: " + Fore.GREEN + str(self.passCount) + Fore.RESET + "/" + str(self.passCount + self.failCount) + "\n" )
            print(line + Fore.GREEN + " PASSED\n" + Fore.RESET)
        else:
            self.failCount += 1
            print("Passed: " + Fore.GREEN + str(self.passCount) + Fore.RESET + "/" + str(self.passCount + self.failCount) + "\n" )
            print(line + Fore.RED + " FAIL\n" + Fore.RESET)

if __name__ == "modules.logger":
    log = log()