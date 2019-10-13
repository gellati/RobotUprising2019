import base64

encoded1 = 'Q1IzMzktYXJpc2UtcmVzZWFyY2gtdm95YWdl'
data = base64.b64decode(encoded1)
print data

# letters missing?
###########Q1lZMZQTY29TCG91BMQTBWVTB3J5LWNVBNNWAXJHY3K=
encoded2 = 'Q1IzMzQtY29tcG91bmQTBWVtb3J5LWNvbnNwAXJhY3k='
data2 = base64.b64decode(encode2)
print data2
