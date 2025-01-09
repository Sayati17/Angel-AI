import re
from conn import mysqlConnect

class sanitizePrompt:
    def __init__(self, db_connection):
        self.db_connection = db_connection

    def sanitize(self, input_text):

        if not self.db_connection.connection:
            self.db_connection.connect()

        _, data2 = self.db_connection.fetch_data()
        sanitize_text = [row[1] for row in data2]
        combined_pattern = r'\b(' + '|'.join(map(re.escape, sanitize_text)) + r')\b'
        input_text = re.sub(combined_pattern, '', input_text, flags=re.IGNORECASE).strip()
        return input_text
    
    def sanitize_input(self,user_input):
        db_connection = mysqlConnect()
        sanitizer = sanitizePrompt(db_connection)
        sanitized_text = sanitizer.sanitize(user_input)
        db_connection.closeConn()
        return sanitized_text