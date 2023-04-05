
import argparse
import pprint
import yaml

from contextLangServer.processor.grammar import Grammar
from contextLangServer.processor.documents import DocumentCache
#from .extract import extractFrom

def cli() :

  argParser  = argparse.ArgumentParser()
  argParser.add_argument('filePath', nargs='?',
    help="The base ConTeXt file to load OR the tmLanguage syntax file to save")
  argParser.add_argument('--save', metavar="base.scope", default='',
      help="Save a full tmLanguage syntax for use with VScode")
  argParser.add_argument('--check', metavar="base.scope", default='',
    help="Check the loaded grammar for missing and extra patterns"
  )
  argParser.add_argument('--prune', action='store_true',
    help="Prune unused patterns from grammar"
  )
  argParser.add_argument('--scopePaths', action='store_true',
    help="List the scopePaths found in the current grammar"
  )
  argParser.add_argument('--onlyActions', action='store_true',
    help="Limit the scope paths to those with loaded actions"
  )
  cliArgs = vars(argParser.parse_args())
  print(yaml.dump(cliArgs))
  filePath = cliArgs['filePath']

  Grammar.loadFromResourceDir('contextLangServer.context.syntax')
  Grammar.loadFromResourceDir('lpicLangServer.lpic.syntax')

  Grammar.dumpGrammar()

  if cliArgs['save'] : 
    if cliArgs['prune'] :
      Grammar.pruneRepository(cliArgs['save'])
    if Grammar.savedToFile(cliArgs['save'], filePath) :
      print(f"Saved current syntax to the tmLanguage.json file:\n  {filePath}\n")
    else :
      print(f"base.scope [{cliArgs['save']}] not found in grammar\n")
    return
  
  if cliArgs['check'] :
    prunedPatterns = []
    if cliArgs['prune'] :
      prunedPatterns = Grammar.pruneRepository(cliArgs['check'])
    missingPatterns, extraPatterns, patternReferences = Grammar.checkRepository(cliArgs['check'])
    print("")
    print("--missing patterns-----------------------------------------------")
    if missingPatterns : print(yaml.dump(missingPatterns))
    else : print("")
    print("--extra patterns-------------------------------------------------")
    if extraPatterns : print(yaml.dump(extraPatterns))
    else : print("")
    if prunedPatterns :
      print("--pruned patterns------------------------------------------------")
      print(yaml.dump(prunedPatterns))
    print("--patterns-------------------------------------------------------")
    if patternReferences : print(yaml.dump(patternReferences))
    else : print("")
    print("-----------------------------------------------------------------")
    return

  if cliArgs['scopePaths'] :
    withAction = False
    if cliArgs['onlyActions'] : withAction = True
    scopePaths = Grammar.collectScopePaths(withAction=withAction)
    print("---scope paths---------------------------------------------")
    print(yaml.dump(scopePaths))
    print("----------------------------------------------------------")
    return

  if filePath == None :
    print("You MUST specify a filePath when extracting LPiC code")
    return
  
  print(f"Extracting LPiC code from:\n  {filePath}\n")
  doc = DocumentCache.loadFromFile(filePath)

  print("---document keys------------------------------------------")
  print(yaml.dump(list(DocumentCache.documents.keys())))
  print("---document-----------------------------------------------")
  print(yaml.dump(doc))
  print("----------------------------------------------------------")

