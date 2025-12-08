import re


class string_extension:
    @staticmethod
    def clean_query_string(query: str) -> str:
        """
        Loại bỏ các ký tự không mong muốn khỏi chuỗi truy vấn.
        """
        # Ví dụ: loại bỏ các ký tự đặc biệt không cần thiết
        cleaned_query = (
            query.replace("\n", " ")
            .replace("\r", " ")
            .replace("update", "something wrong")
            .replace("delete", "something wrong")
            .strip()
        )

        return cleaned_query

    @staticmethod
    def verify_query_string(query: str) -> bool:
        """
        Kiểm tra tính hợp lệ của chuỗi truy vấn SQL.
        Trả về True nếu hợp lệ, False nếu phát hiện nguy hiểm.
        """

        # Danh sách từ khóa nguy hiểm (Oracle + PostgreSQL)
        forbidden_keywords = [
            "DROP",
            "ALTER",
            "TRUNCATE",
            "INSERT",
            "UPDATE",
            "DELETE",
            "MERGE",
            "CREATE",
            "RENAME",
            "GRANT",
            "REVOKE",
            "EXECUTE",
            "CALL",
            "VACUUM",
            "ANALYZE",
            "CLUSTER",
            "RESET",
            "SET",
        ]

        # Kiểm tra từ khóa nguy hiểm
        for keyword in forbidden_keywords:
            if keyword.lower() in query.lower():
                return False

        # Regex phát hiện SQL Injection phổ biến
        injection_patterns = [
            r"--",  # comment
            #r";",  # chèn thêm câu lệnh
            r"/\*.*\*/",  # comment block
            r"\bOR\b\s+1=1",  # OR 1=1
            r"\bAND\b\s+1=1",  # AND 1=1
            r"\bUNION\b\s+\bSELECT\b",  # UNION SELECT
            r"xp_cmdshell",  # MSSQL command execution
            r"information_schema",  # metadata schema
        ]

        for pattern in injection_patterns:
            if re.search(pattern, query, re.IGNORECASE):
                return False

        return True

    @staticmethod
    def exists_limit_clause(query: str, db_type: str = "mssql") -> bool:
        """
        Kiểm tra xem chuỗi truy vấn có chứa mệnh đề giới hạn số dòng hay không.
        Hỗ trợ PostgreSQL, MySQL, MSSQL, Oracle.
        """
        q = query.lower()

        if db_type.lower() in ["postgresql", "mysql"]:
            # LIMIT n
            return bool(re.search(r"\blimit\b\s+\d+", q))

        elif db_type.lower() in ["mssql", "sqlserver"]:
            # SELECT TOP n hoặc OFFSET ... FETCH NEXT n ROWS ONLY
            if re.search(r"\bselect\s+top\s+\d+", q):
                return True
            if re.search(
                r"\boffset\s+\d+\s+rows\s+fetch\s+next\s+\d+\s+rows\s+only", q
            ):
                return True
            return False

        elif db_type.lower() == "oracle":
            # ROWNUM <= n hoặc FETCH FIRST n ROWS ONLY
            if re.search(r"rownum\s*<=\s*\d+", q):
                return True
            if re.search(r"fetch\s+first\s+\d+\s+rows\s+only", q):
                return True
            return False

        else:
            raise ValueError(f"Unsupported db_type: {db_type}")

    @staticmethod
    def exceed_limit_record(query: str) -> bool:
        """
        Hàm kiểm tra xem truy vấn có vượt quá giới hạn số bản ghi cho phép hay không.
        Chưa triển khai.
        """
        pass
