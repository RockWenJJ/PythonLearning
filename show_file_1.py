# Script Name   : show_file_1.py
# Author        : Wen Junjie
# Created       : 08 Oct 2016
# Last Modified :
# Version       : 1.0
# Modifications :
# Description   : Show all the files (includes files in subfolder) in a path

import os   # import the Module

def showFileProperties(path):
    filename = os.listdir(path)
    for s_filename in filename:
        fi = os.path.splitext(s_filename)
        if fi[0][-1] == '\\':   # check if the last character is '\'
            if fi[1] == '':     # check if it is a file or a folder
                showFileProperties(path+s_filename)
            else:
                print(path+s_filename)
        else:
            if fi[1] == '':
                showFileProperties(path+'\\'+s_filename)
            else:
                print(path+'\\'+s_filename)

if __name__ == "__main__":
    showFileProperties("M:\Linkin Park")
