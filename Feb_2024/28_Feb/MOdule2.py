from database_utils import readdb

class_obj = readdb.UtilsDB()
print(class_obj.public_var)
print(class_obj._protected_var)
class_obj.readDBMySQL()
readdb.read_from_db()
class_obj.static_method()
readdb.UtilsDB.static_method()