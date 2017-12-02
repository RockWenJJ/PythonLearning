# Script Name   : show_file_2.py
# Author        : Wen Junjie
# Created       : 08 Oct 2016
# Last Modified :
# Version       : 1.0
# Modifications :
# Description   : Show all the files (includes files in subfolder) in a path

import os   # import the Module

def show_file_2(path):
    file = os.listdir(path)
    for i in file:
        pathname = os.path.join(path,i)
        if not os.path.isfile(pathname):
            show_file_2(pathname)
        else:
            print(pathname)

if __name__ == "__main__":
    show_file_2("M:\Linkin Park")
    print('This file is modified from tencent-cloud')
