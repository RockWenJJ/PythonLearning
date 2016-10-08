# Script Name   : show_file_3.py
# Author        : Wen Junjie
# Created       : 08 Oct 2016
# Last Modified :
# Version       : 1.0
# Modifications :
# Description   : Show all the files (includes files in subfolder) in a path, using method os.walk()

import os   # import the Module

def show_file_3(path):
    for root,dirs,files in os.walk(path):
        for filepath in files:
            print(os.path.join(root,filepath))


if __name__ == "__main__":
    show_file_3("M:")
