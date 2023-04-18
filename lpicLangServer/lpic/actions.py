
from tmGrammars.scopeActions import ScopeActions
from tmGrammars.documents import Document

@ScopeActions.method('meta.source.lpic.include')
def lpicInclude(someThing) :
  print("meta.source.lpic.include", someThing)