#Cài gói(kết nối csdl với sql server) trong môi trường ảo
Bash: <PROJECT PATH> pip install pyodbc

#Cài gói(kết nối csdl với oracle) trong môi trường ảo
Bash: <PROJECT PATH> pip install oracledb

#Cài gói(kết nối csdl với postgresql) trong môi trường ảo
Bash: <PROJECT PATH> pip install psycopg2

#Cài gói để xuất excel
Bash: <PROJECT PATH> pip install pandas openpyxl

#Cài gói để đóng gói phần mềm cho Windows, MacOS, Linux
Bash: <PROJECT PATH> pip install PyInstaller
Bash: <PROJECT PATH> pip install --upgrade PyInstaller pyinstaller-hooks-contrib

#Chạy file encode.py để tạo ra secrect.key và tạo config.json.enc

#Cài gói pyarmor để tăng bảo mật code.
Bash: <PROJECT PATH> pip install pyarmor

#Sử dụng pyarmor
Bash: pyarmor gen --recursive .\Client\AdapterApp\

#Đóng gói bằng cách chạy main.spec
Bash: pyinstaller --distpath D:\OutputFolder\  .\Client\AdapterApp\main.spec
#Sử dụng Qt Designer để kéo thả UI designer như winform. Từ đường dẫn thư mục .venv\Scripts hãy chạy dòng lệnh: 
Bash: <PROJECT PATH>pyside6-designer

#Sau khi đã thiết kế UI trên Qt Designer(.ui) thì trích xuất qua code Python(.py): 
Bash: <PROJECT PATH>pyside6-uic <ĐƯỜNG DẪN LƯU FILE .ui>my_form.ui -o <ĐƯỜNG DẪN LƯU FILE .py>my_form.py

