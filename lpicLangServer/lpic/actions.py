
from contextLangServer.processor.scopeActions import ScopeActions
from contextLangServer.processor.documents import Document

@ScopeActions.method('meta.source.lpic.include')
def lpicInclude(someThing) :
  print("meta.source.lpic.include", someThing)