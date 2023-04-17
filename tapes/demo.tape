Output tapes/demo.gif

Set Shell "zsh"
Set FontSize 32
Set Width 1600
Set Height 900

Type "python sql2gpt.py add arail sqlite:///$HOME/.arail/arail.db" Sleep 500ms  Enter
Sleep 1s
Type "python sql2gpt.py print_schema arail" Sleep 500ms Enter
Sleep 3s
Type "python sql2gpt.py get_prompt arail" Sleep 500ms Enter
Sleep 10s
