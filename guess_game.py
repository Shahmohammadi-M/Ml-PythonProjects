import random
had_bala=99
had_payeen=1
hads=random.randint(had_payeen, had_bala)
print(hads)


javab=input('Enter k or b or d:' )
while javab!='d':
     if javab=='k':
         had_bala=hads-1
     elif javab=='b':
         had_payeen=hads+1
     hads=random.randint(had_payeen,had_bala)
     print(hads)
     javab=input('Enter k or b or d:' )
    
print('you won the game')
    

    