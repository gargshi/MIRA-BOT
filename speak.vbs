Dim s
set s = CreateObject("sapi.spvoice")
Set s.Voice = s.GetVoices.Item(Wscript.Arguments(1))
s.Speak Wscript.Arguments(0)