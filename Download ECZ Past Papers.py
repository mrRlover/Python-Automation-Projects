# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 12:22:38 2020

@author: Mwangele
"""

import requests
from bs4 import BeautifulSoup
import os
import urllib 

archive_url = 'https://zedpastpapers.com/downloads/grade12/index.html'

def get_links():
    r = requests.get(archive_url)

    soup = BeautifulSoup(r.content, 'html5lib')
    
    links = soup.findAll('a')
    
    pdf_links = [link['href'] for link in links if "export" in link['href']]

    return pdf_links

def get_file_links():
    r = requests.get(archive_url)

    soup = BeautifulSoup(r.content, 'html5lib')
    
    links = soup.findAll('a')
    
    file_links = []
    
    for link in links:           
        for nam in filenames:                
            if link.text.strip()==nam:
                file_links.append(link['href'])
                
    return file_links

def download_past_papers(pdf_links):
    for link in pdf_links:
        file_name = link.split('/')[-1]
        
        print("Downloading file:%s"%file_name)
        
        r = requests.get(link)
            
        with open(file_name, 'wb') as f:
            for chunk in r.iter_content(chunk_size = 32768):
                if chunk:
                    f.write(chunk)
        print("%s downloaded!\n"%file_name)

    print('All past papers downloaded!')

pdf_links = get_links()

filepath = 'C:/Users/Mwang/OneDrive/Documents/ECZ/Past Papers/'

os.chdir(filepath)

url = 'https://zedpastpapers.com/downloads/grade12/index.html'
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html)

# kill all script and style elements
for script in soup(["script", "style"]):
    script.extract()    # rip it out

# get text
text = soup.get_text()

# break into lines and remove leading and trailing space on each
lines = (line.strip() for line in text.splitlines())
# break multi-headlines into a line each
chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
# drop blank lines
text = '\n'.join(chunk for chunk in chunks if chunk)

zed_papers =  text.split('\n')

options = ['Mathematics Paper', 'English Paper', 'Science Paper', 'Biology Paper', 'Chemistry Paper', 
           'Computer Studies Paper', 'Physics Paper']

def Filter(string, substr): 
    return [str for str in string if
             any(sub in str for sub in substr)] 
    
filenames = Filter(zed_papers, options)

final_file_links = get_file_links()

# for a in soup.select(','.join('a:contains("{}")'.format(i) for i in filenames)):
#    print(a['href'])

folders = [name + 's' for name in options]

# for folder in folders:
#     if not os.path.isdir(os.path.join(filepath, folder)):
#         os.mkdir(os.path.join(filepath, folder))

final_file_links = [w.replace(' ', '') for w in final_file_links]

i = 0

for link in final_file_links:
    filename = filenames[i] + 'pdf'
    if options[0] in filename:
        os.chdir(os.path.join(filepath, folders[0]))
        if not os.path.isfile(filename):
            urllib.request.urlretrieve(link, filename)
    elif options[1] in filename:
        os.chdir(os.path.join(filepath, folders[1]))
        if not os.path.isfile(filename):
            urllib.request.urlretrieve(link, filename)
    elif options[2] in filename:
        os.chdir(os.path.join(filepath, folders[2]))
        if not os.path.isfile(filename):
            urllib.request.urlretrieve(link, filename)
    elif options[3] in filename:
        os.chdir(os.path.join(filepath, folders[3]))
        if not os.path.isfile(filename):
            urllib.request.urlretrieve(link, filename)
    elif options[4] in filename:
        os.chdir(os.path.join(filepath, folders[4]))
        if not os.path.isfile(filename):
            urllib.request.urlretrieve(link, filename)
    elif options[5] in filename:
        os.chdir(os.path.join(filepath, folders[5]))
        if not os.path.isfile(filename):
            urllib.request.urlretrieve(link, filename)
    else:
        os.chdir(os.path.join(filepath, folders[6]))
        if not os.path.isfile(filename):
            urllib.request.urlretrieve(link, filename)
    
    i = i + 1
    
    if i < len(filenames):
        print("%s downloaded!\n"%filename)
    
    if i == len(filenames):
        print('All past papers downloaded!') 
       
os.getcwd()





