import os

from dotenv import load_dotenv

load_dotenv()

DB_DATABASE = os.environ.get('DB_DATABASE')
DB_USER = os.environ.get('DB_USER')
DB_PASSWORD = os.environ.get('DB_PASSWORD')
DB_HOST = os.environ.get('DB_HOST')
DB_PORT = os.environ.get('DB_PORT')

S3_BUCKET = os.environ.get('S3_BUCKET')
S3_PREFIX = 'unmasked-documents/'
USAGE_MESSAGE = "You need to pass a file path and culture name as parameters"
