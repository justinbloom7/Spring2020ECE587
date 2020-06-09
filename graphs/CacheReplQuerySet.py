from CacheReplacementDB import CacheReplacementDB

class CacheReplQuerySet(CacheReplacementDB):
   def __init__(this, fileName):
      super().__init__(fileName)
      this.__buildQuerySet()
      
   def __buildQuerySet(this):
      this.__querySet = {}
      
      statement = [ { 'fieldName': "dl1_sets", 'value': 512 },
                    { 'fieldName': "dl1_ways", 'value': 4 },
                    { 'fieldName': "dl1_algorithm", 'value': "l" } ]
      this.__querySet['TESTQ'] = statement

   def executeQuery(this, name):
      return this.selectData(this.__querySet[name])
