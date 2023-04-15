
import argparse
import pprint
import yaml

from tmGrammars.grammar import Grammar
from tmGrammars.documents import DocumentCache
from tmGrammars.scopeActions import ScopeActions

#import contextLangServer.context.contextActions

def cli() :

  argParser  = argparse.ArgumentParser()
  argParser.add_argument('filePath', nargs='?',
    help="The base ConTeXt file to load OR the tmLanguage syntax file to save")
  argParser.add_argument('--save', metavar="base.scope", default='',
      help="Save a full tmLanguage syntax for use with VScode")

  argParser.add_argument('--check', action='store_true',
    help="Check the loaded grammar for missing and extra patterns"
  )
  argParser.add_argument('--prune', action='store_true',
    help="Prune unused patterns from grammar"
  )
  argParser.add_argument("--grammar", action='store_true',
    help="Show the currently loaded Grammar"
  )
  argParser.add_argument("--patterns", action='store_true',
    help="Show the patterns"
  )
  argParser.add_argument('--scopePaths', action='store_true',
    help="List the scopePaths found in the current grammar"
  )
  argParser.add_argument("--rules", action='store_true',
    help="Show the rules"
  )
  argParser.add_argument("--actions", action='store_true',
    help="Show the actions"
  )
  cliArgs = vars(argParser.parse_args())
  #print(yaml.dump(cliArgs))
  filePath = cliArgs['filePath']

  

  if cliArgs['actions'] :
    ScopeActions.printActions()
    return

  Grammar.loadFromResourceDir('lpicSyntaxes')
  Grammar.collectRules()
  if cliArgs['prune'] : Grammar.pruneRules()

  if cliArgs['patterns'] :
    Grammar.printPatternReferences()
    return

  if cliArgs['rules'] :
    Grammar.printRules()
    return

  if cliArgs['grammar'] :
    Grammar.printGrammar()
    return

  if cliArgs['save'] : 
    if Grammar.savedToFile(cliArgs['save'], filePath) :
      print(f"Saved current syntax to the tmLanguage.json file:\n  {filePath}\n")
    else :
      print(f"base.scope [{cliArgs['save']}] not found in grammar\n")
    return
  
  if cliArgs['check'] :
    Grammar.printCheckRepositoryReport()
    return

  if cliArgs['scopePaths'] :
    Grammar.printScopePaths()
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

