
import argparse
import pprint
import yaml

import tmGrammars.configuration
from tmGrammars.grammar import Grammar
from tmGrammars.documents import DocumentCache
from tmGrammars.scopeActions import ScopeActions

#import contextLangServer.context.contextActions

def cli() :

  argParser  = argparse.ArgumentParser()
  argParser.add_argument('filePath', nargs='?',
    help="The base ConTeXt file to load"
  )
  tmGrammars.configuration.addArgParseArguments(argParser)

  cliArgs = vars(argParser.parse_args())

  tmGrammars.configuration.loadConfig(cliArgs)

  Grammar.collectRules()
  if cliArgs['prune'] : Grammar.pruneRules()

  filePath = cliArgs['filePath']
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

