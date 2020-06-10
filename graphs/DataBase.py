class DataBase():
   def __init__(this, fileName, fieldNames, fieldTypes):
      this.dataBase = []
      # should add exception if number of fieldNames != fieldTypes
      this.fieldNames = fieldNames
      this.fieldTypes = fieldTypes
      this.__buildDB(fileName)
      this.__currentData = None
      
   def addRecord(this, fields):
      record = {}
               
      for idx in range(len(fields)):
         if (this.fieldTypes[idx] == "int"):
            record[this.fieldNames[idx]] = int(fields[idx])
         elif (this.fieldTypes[idx] == "float"):
            record[this.fieldNames[idx]] = float(fields[idx])
         else:
            record[this.fieldNames[idx]] = fields[idx]
         
      this.dataBase.append(record)

   def parseLine(this, line, idx):
      fields = line.split()
      fields.append(idx)
      this.addRecord(fields)

   def __buildDB(this, fileName):
      idx = 0
      with open(fileName) as fileH:
         for line in fileH:
            this.parseLine(line, idx)
            idx = idx + 1
   
   def queryData(this, statement, merge=False):
      if (not merge):
         this.__currentData = []
   
      for record in this.dataBase:
         match = True
         for condition in statement:
            if (record[condition['fieldName']] != condition['value']):
               match = False
               break
         if (match):
            this.__currentData.append(record)
         
      return this.__currentData
      
   def selectData(this, fieldName):
      selData = []
      for record in this.__currentData:
         selData.append(record[fieldName])
      
      return selData
   
   def printData(this, data):
      for record in data:
         print(record)
