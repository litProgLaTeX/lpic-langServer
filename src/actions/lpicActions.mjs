
function loadedStrParam(disp, ctx, aMessage, callArgs) {
  console.log("----------------------------------------------------------")
  console.log("loadedStrParam")
  console.log(aMessage)
  console.log("----------------------------------------------------------")
  ctx.append({
    'method'   : 'loadedStrParam',
    'msg'      : aMessage,
    'kwargs'   : callArgs,
    'dispType' : 'silly'
  })
}

export function registerActions(ScopeActions) {

  ScopeActions.addScopedAction(
    'source.c.lpic',
    import.meta.url,
    { },
    loadedStrParam
  )

  ScopeActions.addScopedAction(
    'source.ansic.header',
    import.meta.url,
    { },
    loadedStrParam
  )
}

/*

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

*/