# !/bin/bash Run your code in bash terminal
# Used to help users run all the steps to access program

# check if python is installed(for higher marks)

python3 -m venv TODO-venv
# check if venv already exists(for higher marks)
source TODO-venv/bin/activate
pip3 install -r requirements.txt
clear
python3 main.py