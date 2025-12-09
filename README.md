1. Yêu cầu hệ thống

Python 3.10+

pip và virtualenv

Hệ điều hành: Windows / macOS / Linux

Đã cài đặt các SDK/phần mềm phụ thuộc nếu cần:

SQL Server Native Client (nếu dùng pyodbc)

Oracle Instant Client (nếu dùng oracledb)

Qt Designer (kèm theo PySide6)

2. Cấu trúc thư mục dự án (tham khảo)
Project/
│── Client/
│   └── Python_Desktop_Collect_Data/
│       ├── main.py
│       ├── main.spec
│       ├── ui/
│       │   ├── my_form_ui.py
│       │   └── my_form.py
│       └── infrastucture
│── encode.py
│── README.md
└── .venv/

3. Create Virtual Environment
Create venv
python -m venv .venv

Activate venv

Windows

.\.venv\Scripts\activate

macOS / Linux

source .venv/bin/activate

4. Install Database Connector Packages
SQL Server
pip install pyodbc

Oracle
pip install oracledb

PostgreSQL
pip install psycopg2

5. Install Excel Export Packages
pip install pandas openpyxl

6. Install Packaging Tools
pip install PyInstaller
pip install --upgrade PyInstaller pyinstaller-hooks-contrib

7. Generate Encryption Key & Encrypted Config

Run the script:

python encode.py

This will generate:

secret.key
config.json.enc

8. Install PyArmor for Source Code Protection
pip install pyarmor

Encrypt source files:
pyarmor gen --recursive .\Client\Python_Desktop_Collect_Data\

9. Package Application with PyInstaller
pyinstaller --distpath <your path>\OutputFolder\ <your path>\main.spec

Output will be located at:

<your path>\OutputFolder\<app_name>\

10. Design UI with Qt Designer

Launch Qt Designer from the virtual environment:

pyside6-designer

11. Convert .ui File to .py File
pyside6-uic <path>/my_form.ui -o <path>/my_form.py

12. Run Application After Packaging

Windows

<output_folder>\Python_Desktop_Collect_Data.exe

macOS

./Python_Desktop_Collect_Data.app

Linux

./Python_Desktop_Collect_Data

13. Screen shot
    
<img width="516" height="308" alt="image" src="https://github.com/user-attachments/assets/c1edb79e-337f-4401-8060-4e1c14190e1d" />
<img width="1267" height="987" alt="image" src="https://github.com/user-attachments/assets/ee69e47d-6c5f-4532-bc7b-f8a8932e1312" />


