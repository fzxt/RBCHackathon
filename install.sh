virtualenv env

source env/Scripts/activate

pip install -r ./requirements.txt

cd ./app/public

npm install --verbose

