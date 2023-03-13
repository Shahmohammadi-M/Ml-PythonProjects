import csv
import statistics

def calculate_averages(input_file_name, output_file_name):
    with open(input_file_name) as f:
              reader=csv.reader(f)
              a=dict()
              n=[]
            
              for row in reader:
                  these_grades=[]
                  name=row[0]
                  n.append(name)
            
                  for grade in row[1:]:
                      if grade!='':
                          these_grades.append(float(grade))
                          ave=float(statistics.mean(these_grades))
                        
                          a[name]=ave
                     
    with open(output_file_name, 'w', newline='') as fout:
        writer=csv.writer(fout)
        for key, value in a.items():
              writer.writerow((key,value))
                          
    fout.close()


def calculate_sorted_averages(input_file_name, output_file_name):
    with open(input_file_name) as f:
            reader=csv.reader(f)
            a={}
            n=[]
            
          
            for row in reader:
                these_grades=[]
                
                name=row[0]
                n.append(name)
            
                for grade in row[1:]:
                    
                    if grade!='':
                        these_grades.append(float(grade))
                        ave=statistics.mean(these_grades)
                        a[name]=ave 

            sorted_nums=sorted(a.values())
            sorted_nums_uniq=sorted(set(a.values()))
            keys_tmp=list(a.keys())
            list_asli= list(a.values())
            keys_sorted=[]
            for s_numb in sorted_nums_uniq:
                c=0
                indx=[]
                for num in list_asli:
                    c=c+1
                    if s_numb==num:
                        indx.append(c)
                keys_sorted_tmp=[]
                for ind in range(0,len(indx)):
                    keys_sorted_tmp.append(keys_tmp[indx[ind]-1])
                sorted_list=sorted(keys_sorted_tmp)
                for item_in_list in sorted_list:
                    keys_sorted.append(item_in_list)
                
            
            
            tmp_data2=dict()
            n=[]       
            c=-1
            for row in keys_sorted:
                c=c+1
                name=row
                tmp_data2[name]=sorted_nums[c]                         
               
    with open(output_file_name, 'w', newline='') as fout:
                  writer=csv.writer(fout)
                  for key, value in tmp_data2.items():
                      writer.writerow((key,value))                          
    fout.close()


def calculate_three_best(input_file_name, output_file_name):
    with open(input_file_name) as f:
            reader=csv.reader(f)
            a={}
            n=[]
            count=0
            
            for row in reader:
                these_grades=[]
                name=row[0]
                n.append(name)
            
                for grade in row[1:]:
                    if grade!='':
                        these_grades.append(int(grade))
                        ave=statistics.mean(these_grades)
                        a[name]=ave 
                                
            sorted_nums=sorted(a.values())
            sorted_nums_uniq=sorted(set(a.values()))
            keys_tmp=list(a.keys())
            list_asli= list(a.values())
            keys_sorted=[]
            for s_numb in sorted_nums_uniq:
                c=0
                indx=[]
                for num in list_asli:
                    c=c+1
                    if s_numb==num:
                        indx.append(c)
                keys_sorted_tmp=[]
                for ind in range(0,len(indx)):
                    keys_sorted_tmp.append(keys_tmp[indx[ind]-1])
                sorted_list=sorted(keys_sorted_tmp)
                for item_in_list in sorted_list:
                    keys_sorted.append(item_in_list)
                
            
            
            tmp_data2=dict()
            n=[]       
            c=-1
            for row in keys_sorted:
                c=c+1
                name=row
                tmp_data2[name]=sorted_nums[c]   
                        
    with open(output_file_name,'w', newline='') as fout:
        writer=csv.writer(fout)
        for name,ave in sorted(tmp_data2.items(),key=lambda x:x[1] ,reverse=True):
            count=count+1
            if count<=3:
                writer.writerow((name,ave))
    fout.close()

def calculate_three_worst(input_file_name, output_file_name):
    with open(input_file_name) as f:
            reader=csv.reader(f)
            a={}
            n=[]
            count=0
            for row in reader:
                these_grades=[]
                name=row[0]
                n.append(name)
            
                for grade in row[1:]:
                    if grade!='':
                        these_grades.append(int(grade))
                        ave=statistics.mean(these_grades)
                        a[name]=ave 
    with open(output_file_name,'w', newline='') as fout:
        writer=csv.writer(fout)
        for name,ave in sorted(a.items(), key=lambda x:x[1] ):
            count=count+1
            if count<=3:
                writer.writerow([(ave)])
    fout.close() 
           
def calculate_average_of_averages(input_file_name, output_file_name):
    with open(input_file_name) as f:
            reader=csv.reader(f)
            a=dict()
            n=[]
            miangin=[]
            
            for row in reader:
                these_grades=[]
                name=row[0]
                n.append(name)
            
                for grade in row[1:]:
                    if grade!='':
                        these_grades.append(int(grade))
                        ave=statistics.mean(these_grades)
                        a[name]=ave
                     
    with open(output_file_name, 'w', newline='') as fout:
      writer=csv.writer(fout)
      for i in a:
            miangin.append(a.get(i))
      writer.writerow([statistics.mean((miangin))])
                          
    fout.close()
                      

