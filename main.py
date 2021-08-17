#!/usr/modules/env python3

import modules.logger as logger
from modules import config
from modules import test
import sys
import os

def main():
    os.system('clear')
    if not len(sys.argv) == 3 or not sys.argv[1] == "-D":
        print("Usage: sudo python3 -D {device model}")
        exit(1)
    
    productName = sys.argv[2]
    config.config.productName = sys.argv[2]
    product = config.config.getProductInfo(productName)
    if product == None:
        print("Product not found")
        exit(1)
    logger.log.start_log()
    test.RunTest.Start(product)

    print('Detailed information: ' + logger.log.log_name)
    

if __name__ == "__main__":
    main()

