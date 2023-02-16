import os
from collections import Counter
import socket  

def list_files_in_path(path):
    write_to_file('/home/output/result.txt', 'Q4.a) Text files at location /home/data '+str(os.listdir(path))+'\n\n')

def count_number_words(path,file1,file2):
    num_words_file1 = num_words_file2 = 0
    with open(path+file1,'r') as file:
        data = file.read()
        lines = data.split()
        num_words_file1 += len(lines)
    
    with open(path+file2,'r') as file:
        data = file.read()
        lines = data.split()
        num_words_file2 += len(lines)
    
    write_to_file('/home/output/result.txt', 'Q4.b) Number of words in IF.txt: '+str(num_words_file1)+'\n\n')
    write_to_file('/home/output/result.txt', 'Q4.b) Number of words in Limerick.txt: '+ str(num_words_file2)+'\n\n')
    write_to_file('/home/output/result.txt', 'Q4.c) Total number of words in both the files: '+str(num_words_file1+num_words_file2)+'\n\n')

def top_3_frequent_words(path,file1):
    with open(path+'/'+file1, 'r') as file:
        data = file.read()
        lines = data.split()
        word_counts = Counter(lines)
        top_3 = word_counts.most_common(3)
        txt = 'Q4.d) The top 3 words with maximum number of counts in IF.txt are: "'+top_3[0][0]+'", "'+top_3[1][0]+'", and "'+top_3[2][0]+'".'+'\n And their counts are '+str(top_3[0][1])+', '+str(top_3[1][1])+' and '+str(top_3[2][1])+' respectively\n\n'
        write_to_file('/home/output/result.txt', txt)

def get_ip_address():
    hostname=socket.gethostname()   
    IPAddr=socket.gethostbyname(hostname)    
    write_to_file('/home/output/result.txt', "Q4.e) The IP Address is: "+str(IPAddr))

def write_to_file(path, text):
    with open(path, 'a') as file:
        file.write(text)

def clear_file(path):
    isExist = os.path.exists(path)
    if not isExist:
       os.makedirs(path)

    with open(os.path.join(path, 'result.txt'), 'w') as file:
        file.write('')

def read_file(path):
    with open(path, 'r') as f:
        print(f.read())
        


clear_file('/home/output/')
given_path = '/home/data/'
list_files_in_path(given_path)
count_number_words(given_path, 'IF.txt','Limerick.txt')
top_3_frequent_words(given_path,'IF.txt')
get_ip_address()
read_file('/home/output/result.txt')
