# standarts-validator
run

## 1. Install virtualenv
pip install virtualenv

## 2. Create and activate virtualenv
virtualenv env
.\env\Scripts\activate   

## 3. Install packages
pip install -r packages

## 4. Execute the rules
py main.py -c configuration.json -o report.json

## 5. Help
py main.py -h

## 6. Create a installer for Windows
pyinstaller --onefile main.py

