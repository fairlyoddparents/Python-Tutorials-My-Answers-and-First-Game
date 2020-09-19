import xlsxwriter

#Here is the data we want to add to the excel file
txt = "La comida habla por sí sola, y el menú cuenta con la tradicional bandeja montañera, original de la zona paisa o antioqueña, un plato que desde cualquier punto que se mire es gigantesca con su guarnición de chicharrón piel tostada de cerdo, arroz, frijoles, tajadas de plátano maduro, arepa de maíz, tajada de [Anterior]aguacate[Siguiente], carne molida o frita y huevo frito por encima, es cuestión de gusto y apetito. Algo ya más sofisticado es la cazuela de mariscos, una espesa sopa que hace sudar desde la primera cucharada con un buen aliño marino de camarones, muelas de cangrejo, ostras, anillos y trozos de pulpo."
part1 = txt.split("[Anterior]")[0]
term = txt.split("[Anterior]")[1].split("[Siguiente]")[0]
part2 = txt.split("[Siguiente]")[1]
year = int("2003")
author = "PRENSA"
country = "EE. UU."
topic = "05.Gastronomía, cocina"
publication = "Eduardo Marceles (Nueva York), 2003"
url = "http://corpus.rae.es/cgi-bin/crpsrvEx.dll?visualizar?tipo1=5&tipo2=0&iniItem=0&ordenar1=0&ordenar2=0&FID=161218\000\C000O16122018002033222.1076.1072&desc={B}+{I}+aguacate{|I},+en+todos+los+medios,+en+{I}CREA+{|I}+{|B}{BR}&tamVen=1&marcas=0#acierto0"
#Avoid \000 elimination in url
href = url.replace('\000', '\\000')



#Create workbook (excel file)
workbook = xlsxwriter.Workbook('concept.xlsx', {'strings_to_urls':False})
worksheet = workbook.add_worksheet('data')
#Add headers to the first row in bold letters
headers = ['Sentence', 'Link', 'Year', 'Author', 'Country', 'Topic', 'Publication']
bold_letters = workbook.add_format({'bold':True})
worksheet.write_row('A1', headers, bold_letters)



#Create format & set format
general_format = workbook.add_format({'text_wrap':1, 'valign':'top'})
url_format = workbook.add_format({'valign':'top'})
year_format = workbook.add_format({'text_wrap':1, 'align':'left', 'valign':'top'})
concept_format = workbook.add_format({'bold':True, 'font_color':'#8b1728', 'italic':True, 'underline':True})
worksheet.set_column('A:A', 50, general_format)
worksheet.set_column('F:F', 20, general_format)
worksheet.set_column('G:G', 25, general_format)



#Add information to worksheet
worksheet.write_rich_string('A2', part1, concept_format, term, part2)
worksheet.write('B2', href, url_format)
worksheet.write('C2', year, year_format)
worksheet.write('D2', author, general_format)
worksheet.write('E2', country, general_format)
worksheet.write('F2', topic, general_format)
worksheet.write('G2', publication, general_format)

"""
#If you want to write more than one value,
#put them in a list like in the example below

data = [txt, url, year, author, country, topic, publication]
worksheet.write_row('A1', data)
"""




workbook.close()
