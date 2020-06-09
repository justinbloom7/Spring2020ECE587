from DataBase import DataBase

class CacheReplacementDB(DataBase):
   def __init__(this, fileName):
      # should add exception if number of fieldNames != fieldTypes
      fieldNames = [ "il1_sets", "il1_ways", "il1_algorithm",
                     "dl1_sets", "dl1_ways", "dl1_algorithm",
                     "ul2_sets", "ul2_ways", "ul2_algorithm",
                     "ipc", "il1_miss", "dl1_miss", "ul2_miss",
                     "row_number" ]
      fieldTypes = [ "int", "int", "str",
                     "int", "int", "str",
                     "int", "int", "str",
                     "float", "float", "float", "float",
                     "int" ]
      super().__init__(fileName, fieldNames, fieldTypes)
