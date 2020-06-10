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

   def __multiplyVectors(this, v1, v2, scalar=1):
      for idx in range(len(v1)):
         v1[idx] = int(v1[idx] * v2[idx] * scalar)

   def selectData(this, fieldName):
      if (fieldName == "il1_ksize"):
         data = super().selectData("il1_sets")
         ways = super().selectData("il1_ways")
         this.__multiplyVectors(data, ways, 64 / 1024)
      elif (fieldName == "dl1_ksize"):
         data = super().selectData("dl1_sets")
         ways = super().selectData("dl1_ways")
         this.__multiplyVectors(data, ways, 64 / 1024)
      elif (fieldName == "ul2_ksize"):
         data = super().selectData("ul2_sets")
         ways = super().selectData("ul2_ways")
         this.__multiplyVectors(data, ways, 64 / 1024)
      else:
         data = super().selectData(fieldName)
         
      return data
