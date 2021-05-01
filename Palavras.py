#open the file csv
arq = open('baseleitura.csv', 'r')
#open text and read lines
text = arq.readlines()
#Store the variable cont
cont = 0
#Store the list record
newText = []
#iterarion the contents in the file
for i,j in enumerate(text[:-1]) :
    #compare the elements in the next 
    if j != text[i+1]:
        #if they are different 
        #i count and Store record
        cont +=1
        newText.append(j)
       
# After scanning the elements I print the total count
# and the registered words total
print('Word count: ',cont)
for l in newText:
    print('All records: ', l )
#close the file csv
arq.close()