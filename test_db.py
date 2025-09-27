import pymysql
import os
from dotenv import load_dotenv
import mysql.connector  # अगर mysql use कर रहे हो

# .env file load करो
load_dotenv()
try:
    conn = pymysql.connect(host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_NAME"))
    print("Connected to DB OK")
    conn.close()
except Exception as e:
    print("DB connection error:", e)
