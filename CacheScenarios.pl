import subprocess
import os
import sys

def cacheRun(scenarioIndex, percent, paramList, fileName):
   print ("Executing scenario " + str(scenarioIndex) + "(" + str(round(percent*100, 1)) + "%):" +
	  " IL1=" + str(paramList['il1Sets']) + "x" + str(paramList['il1Ways']) + "," + paramList['il1Repl'] +
          " DL1=" + str(paramList['dl1Sets']) + "x" + str(paramList['dl1Ways']) + "," + paramList['dl1Repl'] +
	  " UL2=" + str(paramList['ul2Sets']) + "x" + str(paramList['ul2Ways']) + "," + paramList['ul2Repl'])

   subprocess.run(["./RunParams",
		   str(paramList['il1Sets']), str(paramList['il1Ways']), paramList['il1Repl'],
		   str(paramList['dl1Sets']), str(paramList['dl1Ways']), paramList['dl1Repl'],
		   str(paramList['ul2Sets']), str(paramList['ul2Ways']), paramList['ul2Repl'],
		   fileName ])

def runScenarios(scenarioList, fileName):
   scenarioCount = len(scenarioList)
   scenarioIndex = 1
   for scenario in scenarioList:
      percentComplete = scenarioIndex / scenarioCount
      cacheRun(scenarioIndex, percentComplete, scenario, fileName)
      scenarioIndex = scenarioIndex + 1

def getSetSize(kSize, ways):
    blockSize = 64

    return int((kSize * 1024) / (blockSize * ways))

def buildScenarioSet(il1Sets, il1Ways, dl1Sets, dl1Ways, ul2Sets, ul2Ways):
   replTypes = [ 'l', 'c' ] 
   scenarioSet = []

   for ul2Repl in [ 'l' ]: #replTypes:
      for dl1Repl in replTypes:
         for il1Repl in replTypes:
            params = {'il1Sets': il1Sets, 'il1Ways': il1Ways, 'il1Repl': il1Repl,
                      'dl1Sets': dl1Sets, 'dl1Ways': dl1Ways, 'dl1Repl': dl1Repl,
                      'ul2Sets': ul2Sets, 'ul2Ways': ul2Ways, 'ul2Repl': ul2Repl }
            scenarioSet.append(params)
   return scenarioSet
   
def buildScenarios():
   il1kSizes = [  64, 128, 256 ]
   il1WaysL  = [   2,   4,   8 ]
   dl1kSizes = [  64, 128, 256 ]
   dl1WaysL  = [   2,   4,   8 ]
   ul2kSizes = [ 512 ]
   #ul2kSizes = [ 128, 256, 512 ]
   ul2WaysL  = [  8 ]
   #ul2WaysL  = [   4,  16,  32 ]

   scenarios = []

   for ul2kSize in ul2kSizes:
      for ul2Ways in ul2WaysL:
         ul2Sets = getSetSize(ul2kSize, ul2Ways)

         for dl1kSize in dl1kSizes:
            for dl1Ways in dl1WaysL:
               dl1Sets = getSetSize(dl1kSize, dl1Ways)

               for il1kSize in il1kSizes:
                  for il1Ways in il1WaysL:
                     il1Sets = getSetSize(il1kSize, il1Ways)

                     scenarioSet = buildScenarioSet(il1Sets, il1Ways, dl1Sets, dl1Ways, ul2Sets, ul2Ways)

                     for scenario in scenarioSet:
                        scenarios.append(scenario)
   return scenarios

def cacheScenarios(fileName):
   scenarioList = buildScenarios()
   print("Scenario count: " + str(len(scenarioList)))
   runScenarios(scenarioList, fileName)

def getFileName():
   if (len(sys.argv) != 2):
      fileName = input("Enter file name: ")
   else:
      fileName = sys.argv[1]

   if (os.path.isfile(fileName)):
      print ("File Exists")
      sys.exit()

   return fileName

fileName = getFileName()
cacheScenarios(fileName)
