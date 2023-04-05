
from contextLangServer.processor.scopeActions import ScopeActions

@ScopeActions.method('source.ansic.code')
def loadedStrParam(disp, ctx, aMessage, **kwargs) :
  print("-----------------------------------------")
  print('loadedStrParam')
  print(aMessage)
  print("-----------------------------------------")
  ctx.append({
    'method'   : 'loadedStrParam',
    'msg'      : aMessage,
    'kwargs'   : kwargs,
    'dispType' : type(disp)
  })

@ScopeActions.method('source.ansic.header')
def loadedStrParam(disp, ctx, aMessage, **kwargs) :
  print("-----------------------------------------")
  print('loadedStrParam')
  print(aMessage)
  print("-----------------------------------------")
  ctx.append({
    'method'   : 'loadedStrParam',
    'msg'      : aMessage,
    'kwargs'   : kwargs,
    'dispType' : type(disp)
  })


"""

\definetyping%
  [MkIVCode]%
  [ option=TEX, numbering=line, tab=2,
    before={\noindent\startLitProgFrame}, after=\stopLitProgFrame
  ]

\definetyping%
  [MpIVCode]%
  [ option=MP, numbering=line, tab=2,
    before={\noindent\startLitProgFrame}, after=\stopLitProgFrame
  ]

\definetyping%
  [LuaCode]%
  [option=LUA, numbering=line, tab=2,
    before={\noindent\startLitProgFrame}, after=\stopLitProgFrame
  ]

\definetyping%
  [LuaTemplate]%
  [option=LUA, numbering=line, tab=2,
    before={\noindent\startLitProgFrame}, after=\stopLitProgFrame
  ]

\def\defaultCHeaderLicense{\dosingleempty\lpicSingleArgRelax}
\def\createsCHeader{\dodoubleempty\lpicDoubleArgRelax}
\def\addCHeaderLicense{\dodoubleempty\lpicDoubleArgRelax}

\definetyping%
  [CHeader]%
  [option=CPP, numbering=line, tab=2,
    before={\noindent\startLitProgFrame}, after=\stopLitProgFrame
  ]

\def\defaultCCodeLicense{\dosingleempty\lpicSingleArgRelax}
\def\buildsCCodeLibrary{\dodoubleempty\lpicDoubleArgRelax}
\def\buildsCCodeApplication{\dodoubleempty\lpicDoubleArgRelax}
\def\createsCCode{\dodoubleempty\lpicDoubleArgRelax}
\\def\\addCCodeLicense{\dodoubleempty\lpicDoubleArgRelax}

\\definetyping%
  [CCode]%
  [option=CPP, numbering=line, tab=2,
    before={\noindent\startLitProgFrame}, after=\stopLitProgFrame
  ]

\\unexpanded\def\indexCCode[#1]{
  \directlua{
    thirddata.litProg.addCCodeIndex('#1')
  }
}

"""
