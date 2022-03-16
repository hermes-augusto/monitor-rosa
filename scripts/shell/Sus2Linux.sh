#Primeiro parametro é o diretorio de origem exemplo: /dissemin/publicos/SIASUS/200801_/Dados/
#Segundo é o nome do arquivo ou arquivos com *
NOMESHELL=$(basename $0)
echo ">>>"
echo ">>> Iniciando $NOMESHELL..."
echo ">>> Checks iniciais de ambiente..."
echo ">>> Parametros de processamento..."
vrc=0
if [ ! "$1" ]
then
  echo ">>> Parametro 1: Diretorio nao informado!"
  vrc=20
fi

if [ ! "$2" ]
then
  echo ">>> Parametro 2: Nome do arquivo nao informado!"
  vrc=23
fi

if [ ${vrc} -eq "0" ]
then
   echo ">>> Parametros de processamento OK!"
else
   echo ">>>"
   echo ">>>---------------- Parametros Obrigatorios -----------------------"
   echo ">>> \$1 = Diretorio onde buscar                                    "
   echo ">>> \$2 = Arquivo para pegar                                       "
   echo ">>> Exit Code=$vrc"
   exit $vrc
fi
DIR_FILES_DBC="/home/falkor/monitor_rosa/files/dbc"
DIR_ORIGEM=$1
ARQ_ORIGEM=$2
wget -P $DIR_FILES_DBC --user=Anonymous password= ftp://ftp.datasus.gov.br/${DIR_ORIGEM}/${ARQ_ORIGEM}
