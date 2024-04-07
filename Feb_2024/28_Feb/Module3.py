from database_utils.readdb import UtilsDB,read_from_db

read_from_db()
UtilsDB.static_method() #UtilsDB without brackets is not a object
UtilsDB().readDBMySQL() #UtilsDB with brackets is a object
class_obj = UtilsDB()
class_obj.readDBMySQL()