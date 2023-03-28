import csv

year=2022

mapping_table={}
f1=open("../"+str(year)+"_sgis_attributes_table.csv",'r',encoding='utf-8-sig')
reader=csv.reader(f1)
for line in reader:
	mapping_table[line[2]]=line[0]
f1.close()

f2=open("../"+str(year)+"_06_mois_cjs_merge.csv",'r',encoding='utf-8-sig')
f3=open("../"+str(year)+"_06_pop.csv",'w',encoding='utf-8',newline='')
reader=csv.reader(f2)
writer=csv.writer(f3)

firstline=True
for line in reader:
	if firstline:
		firstline=False
		templine=["SGIS코드"]
		templine+=line
		writer.writerow(templine)
	else:
		if line[0] in mapping_table:
			templine=[mapping_table[line[0]]]
		else:
			templine=['']

		templine+=line
		writer.writerow(templine)

f2.close()
f3.close()