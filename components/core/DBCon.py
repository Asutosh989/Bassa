import MySQLdb
import os
import logging

from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), '../../.env')
load_dotenv(dotenv_path)

_db=None

def get_db_con ():
    global _db
    if _db==None:
        try:
            _db=MySQLdb.connect(host=os.environ.get('BASSA_DB_HOST', '127.0.0.1'),
                                port=os.environ.get('BASSA_DB_PORT',3306),
                                user=os.environ.get('BASSA_DB_USERNAME', 'bassa'),
                                passwd=os.environ.get('BASSA_DB_PASSWORD', 'bassa'),
                                db=os.environ.get('BASSA_DB_NAME', 'bassa'))
            return _db
        except Exception as e:
            logging.exception(e)
            return None
    else:
        return _db

def close_db_con ():
    if _db!=None:
        _db.close()
