import re

html_text = '<p><f><hi rend=CURS>Beben y brindan; al fondo coro cosechando, pisando <a name=acierto2></a><a href=#acierto1><img src=/icono/acierto1.gif align=middle alt=[Anterior] border=0></a><font color="Red" size="3">uva</font><a href=#acierto2><img src=/icono/acierto2.gif align=middle alt=[Siguiente] border=0></a> y embotellando vino.</hi></f></p>'

paragraph_sin_font = html_text.replace('<font color="Red" size="3">', "FOONT")
paragraph_sin_font = paragraph_sin_font.replace("</font>", "FOONT")
paragraph_sin_html = re.sub(r'<.*?>', "", paragraph_sin_font)

print(paragraph_sin_html)
