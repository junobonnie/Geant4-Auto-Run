printf '\033[32mSetting CRY Environment\033[0m\n\n'

printf "Set cry test directory location : "
read DIR
export CRY_TEST_DIR=$DIR
echo "OK!"

sudo chmod 777 *.sh

ln -s $CRY_TEST_DIR/data .
