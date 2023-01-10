# Predefined Keywords that have high weightage
searchList = ['Python','Java','JavaScript','PHP','Ruby','Swift','Perl','SQL','Kotlin','Scala','Objective-C','Assemblylanguage','Rust','Fortran','MATLAB','COBOL','Ada','Haskell','Dart','VisualBasic','C++','c#','csharp','Lua','BASIC','Pascal','Prolog','Julia','Groovy','Erlang','HTML','ALGOL','APL','CSS','Elixir','Scriptinglanguage','CoffeeScript','Tcl','AppleScript','OCaml','ActionScript','VBScript','ECMAScript','AutoLISP','EmacsLisp','android','website','react','js','node','mongodb','express','mernstack','angular','vue','meanstack','jamstack','django','api','xml']

def removeWeightedWords(str):
    newInput = str.lower().replace(' ', ',').replace('-','')
    print(1)
    print(newInput)

    originalInput = ''
    for exclude in searchList:
        if exclude.lower() in newInput:
            newInput = newInput.replace(exclude.lower(), '')

    print(2)
    print(newInput)
    originalInput = newInput.lower().replace(',', ' ')
    return(originalInput)
   