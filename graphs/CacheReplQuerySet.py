from CacheReplacementDB import CacheReplacementDB

class CacheReplQuerySet(CacheReplacementDB):
   def __init__(this, fileName):
      super().__init__(fileName)
      this.__buildQuerySet()
      
   def __buildQuerySet(this):
      this.__querySet = {}
      
      statement = [ { 'fieldName': "il1_ways", 'value': 4 },
                    { 'fieldName': "il1_algorithm", 'value': "l" },
                    { 'fieldName': "dl1_sets", 'value': 512 },
                    { 'fieldName': "dl1_ways", 'value': 4 },
                    { 'fieldName': "dl1_algorithm", 'value': "l" },
                    { 'fieldName': "ul2_algorithm", 'value': "l" } ]
      this.__querySet['IX4LD512X4LUL'] = statement
      statement = [ { 'fieldName': "il1_ways", 'value': 4 },
                    { 'fieldName': "il1_algorithm", 'value': "c" },
                    { 'fieldName': "dl1_sets", 'value': 512 },
                    { 'fieldName': "dl1_ways", 'value': 4 },
                    { 'fieldName': "dl1_algorithm", 'value': "l" },
                    { 'fieldName': "ul2_algorithm", 'value': "l" } ]
      this.__querySet['IX4CD512X4LUL'] = statement
      statement = [ { 'fieldName': "il1_sets", 'value': 512 },
                    { 'fieldName': "il1_ways", 'value': 4 },
                    { 'fieldName': "il1_algorithm", 'value': "l" },
                    { 'fieldName': "dl1_ways", 'value': 4 },
                    { 'fieldName': "dl1_algorithm", 'value': "l" },
                    { 'fieldName': "ul2_algorithm", 'value': "l" } ]
      this.__querySet['I512X4LDX4LUL'] = statement
      statement = [ { 'fieldName': "il1_sets", 'value': 512 },
                    { 'fieldName': "il1_ways", 'value': 4 },
                    { 'fieldName': "il1_algorithm", 'value': "c" },
                    { 'fieldName': "dl1_ways", 'value': 4 },
                    { 'fieldName': "dl1_algorithm", 'value': "l" },
                    { 'fieldName': "ul2_algorithm", 'value': "l" } ]
      this.__querySet['I512X4LDX4CUL'] = statement
      
      statement = [ { 'fieldName': "il1_sets", 'value': 512 },
                    { 'fieldName': "il1_ways", 'value': 4 },
                    { 'fieldName': "il1_algorithm", 'value': "l" },
                    { 'fieldName': "dl1_sets", 'value': 512 },
                    { 'fieldName': "dl1_ways", 'value': 4 },
                    { 'fieldName': "dl1_algorithm", 'value': "l" },
                    { 'fieldName': "ul2_algorithm", 'value': "l" } ]
      this.__querySet['I512X4LD512X4LUL'] = statement
      statement = [ { 'fieldName': "il1_sets", 'value': 1024 },
                    { 'fieldName': "il1_ways", 'value': 2 },
                    { 'fieldName': "il1_algorithm", 'value': "l" },
                    { 'fieldName': "dl1_sets", 'value': 512 },
                    { 'fieldName': "dl1_ways", 'value': 4 },
                    { 'fieldName': "dl1_algorithm", 'value': "l" },
                    { 'fieldName': "ul2_algorithm", 'value': "l" } ]
      this.__querySet['I1024X2LD512X4LUL'] = statement
      statement = [ { 'fieldName': "il1_sets", 'value': 256 },
                    { 'fieldName': "il1_ways", 'value': 8 },
                    { 'fieldName': "il1_algorithm", 'value': "l" },
                    { 'fieldName': "dl1_sets", 'value': 512 },
                    { 'fieldName': "dl1_ways", 'value': 4 },
                    { 'fieldName': "dl1_algorithm", 'value': "l" },
                    { 'fieldName': "ul2_algorithm", 'value': "l" } ]
      this.__querySet['I256X8LD512X4LUL'] = statement
      statement = [ { 'fieldName': "il1_sets", 'value': 512 },
                    { 'fieldName': "il1_ways", 'value': 4 },
                    { 'fieldName': "il1_algorithm", 'value': "c" },
                    { 'fieldName': "dl1_sets", 'value': 512 },
                    { 'fieldName': "dl1_ways", 'value': 4 },
                    { 'fieldName': "dl1_algorithm", 'value': "l" },
                    { 'fieldName': "ul2_algorithm", 'value': "l" } ]
      this.__querySet['I512X4CD512X4LUL'] = statement
      statement = [ { 'fieldName': "il1_sets", 'value': 1024 },
                    { 'fieldName': "il1_ways", 'value': 2 },
                    { 'fieldName': "il1_algorithm", 'value': "c" },
                    { 'fieldName': "dl1_sets", 'value': 512 },
                    { 'fieldName': "dl1_ways", 'value': 4 },
                    { 'fieldName': "dl1_algorithm", 'value': "l" },
                    { 'fieldName': "ul2_algorithm", 'value': "l" } ]
      this.__querySet['I1024X2CD512X4LUL'] = statement
      statement = [ { 'fieldName': "il1_sets", 'value': 256 },
                    { 'fieldName': "il1_ways", 'value': 8 },
                    { 'fieldName': "il1_algorithm", 'value': "c" },
                    { 'fieldName': "dl1_sets", 'value': 512 },
                    { 'fieldName': "dl1_ways", 'value': 4 },
                    { 'fieldName': "dl1_algorithm", 'value': "l" },
                    { 'fieldName': "ul2_algorithm", 'value': "l" } ]
      this.__querySet['I256X8CD512X4LUL'] = statement
      statement = [ { 'fieldName': "il1_sets", 'value': 512 },
                    { 'fieldName': "il1_ways", 'value': 4 },
                    { 'fieldName': "il1_algorithm", 'value': "l" },
                    { 'fieldName': "dl1_sets", 'value': 1024 },
                    { 'fieldName': "dl1_ways", 'value': 2 },
                    { 'fieldName': "dl1_algorithm", 'value': "l" },
                    { 'fieldName': "ul2_algorithm", 'value': "l" } ]
      this.__querySet['I512X4LD1024X2LUL'] = statement
      statement = [ { 'fieldName': "il1_sets", 'value': 512 },
                    { 'fieldName': "il1_ways", 'value': 4 },
                    { 'fieldName': "il1_algorithm", 'value': "l" },
                    { 'fieldName': "dl1_sets", 'value': 256 },
                    { 'fieldName': "dl1_ways", 'value': 8 },
                    { 'fieldName': "dl1_algorithm", 'value': "l" },
                    { 'fieldName': "ul2_algorithm", 'value': "l" } ]
      this.__querySet['I512X4LD256X8LUL'] = statement
      statement = [ { 'fieldName': "il1_sets", 'value': 512 },
                    { 'fieldName': "il1_ways", 'value': 4 },
                    { 'fieldName': "il1_algorithm", 'value': "l" },
                    { 'fieldName': "dl1_sets", 'value': 512 },
                    { 'fieldName': "dl1_ways", 'value': 4 },
                    { 'fieldName': "dl1_algorithm", 'value': "c" },
                    { 'fieldName': "ul2_algorithm", 'value': "l" } ]
      this.__querySet['I512X4LD512X4CUL'] = statement
      statement = [ { 'fieldName': "il1_sets", 'value': 512 },
                    { 'fieldName': "il1_ways", 'value': 4 },
                    { 'fieldName': "il1_algorithm", 'value': "l" },
                    { 'fieldName': "dl1_sets", 'value': 1024 },
                    { 'fieldName': "dl1_ways", 'value': 2 },
                    { 'fieldName': "dl1_algorithm", 'value': "c" },
                    { 'fieldName': "ul2_algorithm", 'value': "l" } ]
      this.__querySet['I512X4LD1024X2CUL'] = statement
      statement = [ { 'fieldName': "il1_sets", 'value': 512 },
                    { 'fieldName': "il1_ways", 'value': 4 },
                    { 'fieldName': "il1_algorithm", 'value': "l" },
                    { 'fieldName': "dl1_sets", 'value': 256 },
                    { 'fieldName': "dl1_ways", 'value': 8 },
                    { 'fieldName': "dl1_algorithm", 'value': "c" },
                    { 'fieldName': "ul2_algorithm", 'value': "l" } ]
      this.__querySet['I512X4LD256X8CUL'] = statement

   def executeQuery(this, name, merge=False):
      return this.queryData(this.__querySet[name], merge)
      
        
