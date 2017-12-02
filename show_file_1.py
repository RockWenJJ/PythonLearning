# Script Name   : show_file_1.py
# Author        : Wen Junjie
# Created       : 08 Oct 2016
# Last Modified : 08 Oct 2016
# Version       : 1.1
# Modifications : change the name of the function
# Description   : Show all the files (includes files in subfolder) in a path

import os   # import the Module

def show_file_1(path):
    filename = os.listdir(path)
    for s_filename in filename:
        fi = os.path.splitext(s_filename)
        if fi[0][-1] == '\\':   # check if the last character is '\'
            if fi[1] == '':     # check if it is a file or a folder
                show_file_1(path+s_filename)
            else:
                print(path+s_filename)
        else:
            if fi[1] == '':
                showFileProperties(path+'\\'+s_filename)
            else:
                print(path+'\\'+s_filename)

if __name__ == "__main__":
    show_file_1("M:\Linkin Park")
    print('This is for Git Learning!')
