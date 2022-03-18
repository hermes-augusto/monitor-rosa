echo "Conversao do dir files/dbc"
echo "Iniciando..." `date +"%T.%3N"`
for file in /home/falkor/monitor_rosa/files/dbc_copy/*.dbc; do
  file_name_dbf=`basename $file`

  /home/falkor/monitor_rosa/scripts/c/executavel/dbc2dbf.exe "$file" "/home/falkor/monitor_rosa/files/dbf_copy/${file_name_dbf%%.*}.dbf"

  echo "$file converted to dbf"
done
echo "Fim..." `date +"%T.%3N"`