import json
import os

from cryptography.fernet import Fernet


class LoadConfig:
    def __init__(self, config_file="config.json.enc"):
        self.base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
        self.config_path = os.path.join(self.base_dir, config_file)
        # Đọc key từ file
        with open(self.base_dir + "\\secret.key", "rb") as f:
            key = f.read()

        cipher = Fernet(key)

        # Giải mã file config.enc
        with open(self.config_path, "rb") as f:
            encrypted_data = f.read()

        decrypted_data = cipher.decrypt(encrypted_data)
        self.config = json.loads(decrypted_data.decode("utf-8"))

        # # Đọc file config
        # with open(self.config_path, "r", encoding="utf-8") as f:
        #     self.config = json.load(f)

    def get_section(self, section_name):
        """Lấy một phần cấu hình theo tên"""
        return self.config.get(section_name, {})

    def get_value(self, section_name, key, default=None):
        """Lấy giá trị cụ thể trong một section"""
        return self.config.get(section_name, {}).get(key, default)
