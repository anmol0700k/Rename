import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "12658994")

API_HASH = os.environ.get("API_HASH", "588df9088e18efcac76ba0d6e5769fd8")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6243118913:AAGvl4yUEngA1y1wQjYMH3ju-teMEJf-Tz4") 

FORCE_SUB = os.environ.get("FORCE_SUB", "Pros_Movies_Empire") 

DB_NAME = os.environ.get("DB_NAME","cluster0")     

DB_URL = os.environ.get("DB_URL","mongodb+srv://Anmol0700:Anmol0700@cluster0.j4pel8a.mongodb.net/?retryWrites=true&w=majority")
 
FLOOD = int(os.environ.get("FLOOD", "10"))

START_PIC = os.environ.get("START_PIC", "https://telegra.ph/file/30576a3ff888028463310.jpg")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '1663603208').split()]

PORT = os.environ.get("PORT", "8080")
