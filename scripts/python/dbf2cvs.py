import csv
import sys
from datetime import datetime

from dbfread import DBF
def dbf_to_csv(dbf_table_pth): #Input a dbf, output a csv, same name, same path, except extension
    
    file_name=dbf_table_pth
    dbf_table_pth = "/home/falkor/monitor_rosa/files/dbf_copy/ABOCE1502.dbf"
    csv_fn = "/home/falkor/monitor_rosa/files/csv/"+file_name[:-4]+".csv" #Set the csv file name
    table = DBF(dbf_table_pth, encoding="Latin-1")# table variable is a DBF object
    with open(csv_fn, 'w', newline = '',encoding="utf8") as f:# create a csv file, fill it with dbf content
        writer = csv.writer(f)
        writer.writerow(table.field_names)# write the column name
        for record in table: # write the rows
            writer.writerow(list(record.values()))
    return csv_fn # return the csv name

if __name__ == "__main__":
    #print("Inciando processamento: ",datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
    name_file = sys.argv[1]
    dbf_to_csv(name_file)
    #print("Fim do processamento: ",datetime.now().strftime("%d/%m/%Y %H:%M:%S"))

