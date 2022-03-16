echo "Conversao do dir files/dbf"
echo "Iniciando..." `date +"%T.%3N"`
for file in /home/falkor/monitor_rosa/files/dbf/*.dbf; do
  file_name_dbf=`basename $file`

  python3 /home/falkor/monitor_rosa/scripts/python/dbf2cvs.py "$file_name_dbf"

  echo "$file converted to csv"
done
echo "Fim..." `date +"%T.%3N"`