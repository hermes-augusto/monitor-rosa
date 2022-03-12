for file in /home/falkor/monitor_rosa/files_dbc/*.dbc; do
  ./teste "$file" "/home/falkor/monitor_rosa/files_dbf/${file%%.*}.dbf"
  echo "$file converted to dbf"
done
