# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 16:59:50 2019

@author: 813908
"""

from os import listdir
from os.path import isfile, join, exists

mypath = 'C:/Users/813908/Music/'

onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

onlyfiles = [x for x in onlyfiles if not x.endswith('.ini')]


directory_to_extract_to = 'C/Users/813908/Music/'

import zipfile

for file in onlyfiles:
    
    path_to_zip_file = mypath + file
    
    directory_to_extract_to = mypath + file[:-3]
    
    with zipfile.ZipFile(path_to_zip_file, 'r') as zip_ref:
        zip_ref.extractall(directory_to_extract_to)


from shuil import move, copy2

for i in onlyfiles:
    
    final_folder = mypath + i[:-3]
    
    if not exists(final_folder):
        move(join(final_folder, i), final_folder)
    else:
        copy2(join(final_folder, i), final_folder)