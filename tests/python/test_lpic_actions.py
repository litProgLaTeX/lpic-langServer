
import yaml

from contextLangServer.processor.scopeActions import ScopeActions

import lpicLangServer.lpic.actions

def test_lpicActions_listMethods() :
  print(yaml.dump(ScopeActions.actions))
  assert False