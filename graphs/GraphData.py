import matplotlib.pyplot as plt

from CacheReplQuerySet import CacheReplQuerySet

def executeQueryHelper(dataBase, queryNames):
   if type(queryNames) is list:
      merge = False
      for queryName in queryNames:
         dataBase.executeQuery(queryName, merge)
         merge = True
         
   else:
      dataBase.executeQuery(queryNames)

def plotDataSet(dataBase, figureName, legendLoc,
                plotNameA, queryNameA, xFieldNameA, yFieldNameA,
                plotNameB, queryNameB, xFieldNameB, yFieldNameB,
                plotNameC, queryNameC, xFieldNameC, yFieldNameC,
                plotNameD, queryNameD, xFieldNameD, yFieldNameD):
                   
   executeQueryHelper(dataBase, queryNameA)
   xValues = dataBase.selectData(xFieldNameA)
   yValues = dataBase.selectData(yFieldNameA)
   plt.scatter(xValues, yValues, c='b', marker='s', label=plotNameA)
   
   executeQueryHelper(dataBase, queryNameB)
   xValues = dataBase.selectData(xFieldNameB)
   yValues = dataBase.selectData(yFieldNameB)
   plt.scatter(xValues, yValues, c='r', marker='^', label=plotNameB)

   executeQueryHelper(dataBase, queryNameC)
   xValues = dataBase.selectData(xFieldNameC)
   yValues = dataBase.selectData(yFieldNameC)
   plt.scatter(xValues, yValues, c='b', marker='o', label=plotNameC)
   
   executeQueryHelper(dataBase, queryNameD)
   xValues = dataBase.selectData(xFieldNameD)
   yValues = dataBase.selectData(yFieldNameD)
   plt.scatter(xValues, yValues, c='r', marker='D', label=plotNameD)

   plt.legend(loc=legendLoc)
   plt.title(figureName)
   plt.show()

db = CacheReplQuerySet("run_results.txt")

plotDataSet(db, "Effect of Cache Size on IPC", 'lower right',
            "I-Cache using LRU", "IX4LD512X4LUL", "il1_ksize", "ipc",
            "I-Cache using PLRU", "IX4CD512X4LUL", "il1_ksize", "ipc",
            "D-Cache using LRU", "I512X4LDX4LUL", "dl1_ksize", "ipc",
            "D-Cache using PLRU", "I512X4LDX4CUL", "dl1_ksize", "ipc")
plotDataSet(db, "Effect of Cache Size on Miss Rate", 'upper right',
            "I-Cache using LRU", "IX4LD512X4LUL", "il1_ksize", "il1_miss",
            "I-Cache using PLRU", "IX4CD512X4LUL", "il1_ksize", "il1_miss",
            "D-Cache using LRU", "I512X4LDX4LUL", "dl1_ksize", "dl1_miss",
            "D-Cache using PLRU", "I512X4LDX4CUL", "dl1_ksize", "dl1_miss")

queryIL1_L = [ 'I512X4LD512X4LUL', 'I1024X2LD512X4LUL', 'I256X8LD512X4LUL' ]
queryIL1_C = [ 'I512X4CD512X4LUL', 'I1024X2CD512X4LUL', 'I256X8CD512X4LUL' ]
queryDL1_L = [ 'I512X4LD512X4LUL', 'I512X4LD1024X2LUL', 'I512X4LD256X8LUL' ]
queryDL1_C = [ 'I512X4LD512X4CUL', 'I512X4LD1024X2CUL', 'I512X4LD256X8CUL' ]

plotDataSet(db, "Effect of Associativity on IPC", 'lower right',
            "I-Cache using LRU", queryIL1_L, "il1_ways", "ipc",
            "I-Cache using PLRU", queryIL1_C, "il1_ways", "ipc",
            "D-Cache using LRU", queryDL1_L, "dl1_ways", "ipc",
            "D-Cache using PLRU", queryDL1_C, "dl1_ways", "ipc")
plotDataSet(db, "Effect of Associativity on Miss Rate", 'upper right',
            "I-Cache using LRU", queryIL1_L, "il1_ways", "il1_miss",
            "I-Cache using PLRU", queryIL1_C, "il1_ways", "il1_miss",
            "D-Cache using LRU", queryDL1_L, "dl1_ways", "dl1_miss",
            "D-Cache using PLRU", queryDL1_C, "dl1_ways", "dl1_miss")
