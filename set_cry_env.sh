printf '\033[32mSetting CRY Environment\033[0m\n\n'

printf "Set cry home directory location : "
read DIR
export CRY_HOME=$DIR
echo "OK!"

sudo chmod 777 *.sh

#ln -s $CRY_HOME/data .
cp ./testOut.cc $CRY_HOME/test
cd $CRY_HOME/test
make testOut
