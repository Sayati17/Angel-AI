import re
from conn import fetch_data

def sanitize_input(input_text):
    _, data2 = fetch_data()
    sanitize_names = [row[1] for row in data2]
    combined_pattern = r'\b(' + '|'.join(map(re.escape, sanitize_names)) + r')\b'
    input_text = re.sub(combined_pattern, '', input_text, flags=re.IGNORECASE).strip()
    return input_text