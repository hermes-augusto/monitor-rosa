import csv
import sys
from datetime import datetime

from dbfread import DBF

def dbf_to_csv(dbf_table_pth): 
    
    file_name=dbf_table_pth
    dbf_table_pth = "/home/falkor/monitor_rosa/files/dbf/"+file_name
    csv_fn = "/home/falkor/monitor_rosa/files/csv/"+file_name[:-4]+".csv" 
    table = DBF(dbf_table_pth, encoding="Latin-1")
    #print("Inciando processamento: ",datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
    with open(csv_fn, 'w', newline = '',encoding="utf8") as f:
        writer = csv.writer(f)
        writer.writerow(table.field_names)
        for record in table: 
            writer.writerow(list(record.values()))
    #print("Fim do processamento: ",datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
    return csv_fn

if __name__ == "__main__":
    print("Inciando processamento: ",datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
    name_file = sys.argv[1]
    dbf_to_csv(name_file)
    print("Fim do processamento: ",datetime.now().strftime("%d/%m/%Y %H:%M:%S"))

