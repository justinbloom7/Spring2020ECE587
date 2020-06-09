from CacheReplQuerySet import CacheReplQuerySet

db = CacheReplQuerySet("run_results.txt")
data = db.executeQuery('TESTQ')
db.printData(data)
