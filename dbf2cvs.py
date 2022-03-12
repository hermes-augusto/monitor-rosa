import csv
from dbfread import DBF
def dbf_to_csv(dbf_table_pth): #Input a dbf, output a csv, same name, same path, except extension
    csv_fn = dbf_table_pth[:-4]+ ".csv" #Set the csv file name
    table = DBF(dbf_table_pth,encoding="Latin-1")# table variable is a DBF object
    with open(csv_fn, 'w', newline = '',encoding="utf8") as f:# create a csv file, fill it with dbf content
        writer = csv.writer(f)
        writer.writerow(table.field_names)# write the column name
        for record in table: # write the rows
            writer.writerow(list(record.values()))
    return csv_fn # return the csv name

dbf_to_csv("output_v2.dbf")

#Leitura basica o csv para ver como esta
file = open('output_v2.csv', encoding='utf-8', errors='replace', newline='')

csvreader = csv.reader(file)
header = []
header = next(csvreader)

rows = []
for row in csvreader:
        rows.append(row)

print(rows)
#exemplo abaixo de uma linha
#['201510', 'PG', '230440', '2561492', '2315201273869', '201510',0301120056', '40.0', '230440', '05', '30', 'M', '07272636000212', '07272636000131', '\x83\x84\x83{{\x7f{{|\x83\x83\x80\x7f\x80|', '4', '46', 'F', '01', '230440', '010', '60812450', '0', '1', '20151010', '20151231', '05', '1', '21', '0', '0', '1', '0', '0', '', 'M230440001', '01', '0000000000000', '2561492', '20151010', '20151010', '0000', '0000', '0000', '', '', '0407010173', '20141016', '2314103849794', '', '', '', '', '', '', '', '', '', '', '', '', '12', '2', '', '', 'N', '', '', '', '', '', '', '0', '0', '1', '0', '1']
