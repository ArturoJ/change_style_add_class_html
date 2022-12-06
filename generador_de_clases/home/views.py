import re
from django.http import HttpResponse
from django.shortcuts import render

def inicio_views(request):
    return render(request, 'index.html')


def leer_datos(request):
    # Obtiene el contenido del campo "foo" del formulario HTML
    txt = request.POST['foo']
    # Inicializa la variable "separar" en 2
    separar = 2
    # Inicializa la lista vacía "lista"
    lista = []
    # Inicializa la variable de texto vacía "texto"
    texto = ''
    # Itera sobre cada carácter en el texto
    for a in txt:
        # Si encuentra un "<", agrega el texto actual a la lista y
        # establece la variable "texto" en una cadena vacía
        if a == '<':
            lista.append(texto)
            texto = ''
            separar = 0
        # Si encuentra un ">", establece la variable "separar" en 1
        elif a == '>':
            separar = 1

        # Si "separar" es 2, agrega el carácter actual al texto
        if separar == 2:
            texto += a

        # Si "separar" es 1, agrega el carácter actual al texto y
        # luego agrega el texto actual a la lista y establece la
        # variable "texto" en una cadena vacía
        if separar == 1:
            texto += a
            lista.append(texto)
            texto = ''
            separar = 2

        # Si "separar" es 0, agrega el carácter actual al texto
        if separar == 0:
            texto += a

    # Filtra la lista para eliminar elementos que contengan solo espacios en blanco
    filtered = filter(lambda x: not re.match(r'^\s*$', x), lista)
    # Inicializa la variable de texto vacía "texto_para_text_area"
    texto_para_text_area = ''
    # Itera sobre cada elemento filtrado en la lista
    for a in filtered:
        # Agrega el elemento actual al texto final, seguido de un salto de línea
        texto_para_text_area += a + '\n'

    # Devuelve el texto final como respuesta HTTP
    return HttpResponse(texto_para_text_area)


def separa_styles(request):
    # Define la variable global "new_class"
    global new_class
    # Obtiene el contenido del campo "foo2" del formulario HTML
    txt = request.POST['foo2']
    # Inicializa la variable "separar" en 2
    separar = 2
    # Inicializa la lista vacía "lista"
    lista = []
    # Inicializa la variable de texto vacía "texto"
    texto = ''
    # Itera sobre cada carácter en el texto
    for a in txt:
        # Si encuentra un "<", agrega el texto actual a la lista y
        # establece la variable "texto" en una cadena vacía
        if a == '<':
            lista.append(texto)
            texto = ''
            separar = 0
        # Si encuentra un ">", establece la variable "separar" en 1
        elif a == '>':
            separar = 1

        # Si "separar" es 2, agrega el carácter actual al texto
        if separar == 2:
            texto += a

        # Si "separar" es 1, agrega el carácter actual al texto y
        # luego agrega el texto actual a la lista y establece la
        # variable "texto" en una cadena vacía
        if separar == 1:
            texto += a
            lista.append(texto)
            texto = ''
            separar = 2

        # Si "separar" es 0, agrega el carácter actual al texto
        if separar == 0:
            texto += a

    # Filtra la lista para eliminar elementos que contengan solo espacios en blanco
    filtered = filter(lambda x: not re.match(r'^\s*$', x), lista)
    # Inicializa la variable de texto vacía "texto_para_text_area"
    texto_para_text_area = ''
    # Inicializa la variable "class_add" en 0
    class_add = 0

    # Itera sobre cada elemento filtrado en la lista
    for a in filtered:
        # Incrementa la variable "class_add" en 1
        class_add += 1
        # Si el elemento contiene "class" y "style=", realiza las siguientes operaciones:
        if a.find('class') != -1 and a.find('style=') !=

            # Busca style y lo separa para mostrar en css
            select_style = re.compile('style=".*?"')
            search_style = select_style.findall(a)
            if str(search_style[0])[-2:-1] != ';':
                add_style_css = str(search_style[0])[7:-1] + ';'
            else:
                add_style_css = str(search_style[0])[7:-1]
            new_class += '''.clas_pers_''' + str(class_add) + '''{
    ''' + str(add_style_css) + '''
}

'''
            # Agrega a las clases actuales las nuevas
            select_class= re.compile('class=".*?"')
            search_class = select_class.findall(a)
            add_class = str(search_class[0])[:-1] + ' clas_pers_' + str(class_add) + '"'

            select_clear = re.compile('class=".*?"')
            cleaner_text = re.sub(select_clear, add_class, a)
            a = cleaner_text

            select_clear = re.compile('style=".*?"')
            cleaner_text = re.sub(select_clear, '', a)
            a = cleaner_text



        #Solo el que tenga style
        elif a.find('style=') != -1:
            #class_add += 1
            select_style = re.compile('style=".*?"')
            search_style = select_style.findall(a)
            if str(search_style[0])[-2:-1] != ';':
                add_style_css = str(search_style[0])[7:-1] + ';'
            else:
                add_style_css = str(search_style[0])[7:-1]

            new_class += '''.clas_pers_'''+ str(class_add) + '''{
    '''+str(add_style_css)+'''
}
            
'''
            select_clear = re.compile('style=".*?"')
            cleaner_text = re.sub(select_clear, 'class="clas_pers_' + str(class_add) + '"', a)
            a = cleaner_text


        texto_para_text_area += a + '\n'

    return HttpResponse(texto_para_text_area)


def ver_styles(request):

    global new_class
    return HttpResponse(new_class)
