import os
import mysql.connector

def init_db():
    conn = mysql.connector.connect(
        host=os.getenv('DB_HOST', 'localhost'),
        user=os.getenv('DB_USER', 'api_gateway'),
        password=os.getenv('DB_PASSWORD', ''),
        database=os.getenv('DB_NAME', 'api_gateway_fifo')
    )
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS api_calls (
            id INT AUTO_INCREMENT PRIMARY KEY,
            data TEXT NOT NULL,
            timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

if __name__ == "__main__":
    init_db()
