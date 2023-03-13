import hashlib
import csv

def hash_password_hack(input_file_name, output_file_name):
  with open(input_file_name) as f:
            reader=csv.reader(f)
            a=dict()
            hash_d=dict()
            
            
            for row in reader:
             name=row[0]
             text=row[1]
             a[name]=text
                
            for i in range(1000 , 10000):
               hash_jadid = hashlib.sha256(str(i).encode())
               hash_jadid = hash_jadid.hexdigest()
               hash_d[hash_jadid] = i
               
            c=dict()
            for keyss, a_item in a.items():
              name_new=keyss
              for hash_item in hash_d.keys():
                  if hash_item==a_item:                  
                    c[name_new]=hash_d.get(hash_item)
 
    
  with open(output_file_name, 'w', newline='') as fout:
        writer=csv.writer(fout)
        for key, value in c.items():
              writer.writerow((key,value))
                          
  fout.close() 
