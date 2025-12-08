import json
import os


class LoadJson:
    def __init__(self, config_file="sample_queries.json", level_up: str = ".."):

        self.base_dir = os.path.abspath(
            os.path.join(os.path.dirname(__file__), level_up)
        )

        self.config_path = os.path.join(self.base_dir, config_file)
        self.sample_queries = []  # khởi tạo list

        # Nếu file chưa tồn tại thì tạo mới
        if not os.path.exists(self.config_path):
            # Nếu là sample_queries.json thì tạo file rỗng
            if config_file == "sample_queries.json":
                with open(self.config_path, "w", encoding="utf-8") as f:
                    f.write("")  # hoặc ghi một JSON mặc định

        if config_file == "sample_queries.json":
            with open(self.config_path, "r", encoding="utf-8") as f:
                for line in f:
                    self.sample_queries.append(json.loads(line))
        else:
            # Đọc file config
            with open(self.config_path, "r", encoding="utf-8") as f:
                self.config = json.load(f)

    def get_section(self, section_name):
        """Lấy một phần cấu hình theo tên"""
        return self.config.get(section_name, {})

    def get_value(self, section_name, key, default=None):
        """Lấy giá trị cụ thể trong một section"""
        return self.config.get(section_name, {}).get(key, default)

    def config_path(self):
        return self.config_path
