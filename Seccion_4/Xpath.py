
## Syntax 
# // encuentra cualquier tipo de atributto en el texto HTML

# Xpath, podemos obtener elementos html con //tag, este tambien se puede seleccionar atravez de corchetes //tag[0]
# Tambien podemos buscar el elemento atravez del atributo //tag[@Atributo="Valor"] es similar a como lo hacemos con soup.find(atributto,class_=)

## Funciones
# contains() : Busca texto dentro de un elemento
# start-with() : Busca texto apartir de un elemento    # Syntax : //tag[contains(@Atributo, "Valor")]

## Operadores logicos
# and/or : estos se usan igual que en cualquier lenguaje y su sintaxis es #Syntax : //tag[(expresion 1 ) and/or (expresion 2)] 

## Ejemplos
#//h1[1] # Se obtiene el primer elemento h1
#//h1[@class = title] # Se obtiene el h1 atravez de la clase
#//p[(@class = paragraph_1) and @class = paragraph_2]  # No devuelve nada ya que no hay quien satisfaga esta operacion
#//p[(@class = paragraph_1) or @class = paragraph_2]  # Devielve ambos ya que ambos existen
#//p[constain(@class, "_2")] # Esto sirve para cuando tenemos que localizar atravez de una palabra o pista de elemento  


# Hijos, Padres, Nietos, etc    @atributo, () agrupa, [index] indice
# //article/h1 # Con esto queremos decir que queremos el elemento h1 hijo de article
# //article//h1//text() : Busca texto dentro de el elemento este llamado como una funcion
# //h1.. # Estos punto punto al igual que los niveles de carpeteas podemos obtener el elemento padre que en este caso seria article
# //article/* # Esto funciona para cuando queramos tomar todos los elementos dentro de una etiqueta HTML
# //article/*/text() # Esta convinacion podemos capturar todos los textos dentrode article
