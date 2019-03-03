import re
from django.http import HttpResponse
from django.shortcuts import render

def inicio_views(request):
    return render(request, 'index.html')


def leer_datos(request):
    txt = request.POST['foo']
    separar = 2
    lista = []
    texto = ''''''
    for a in txt:
        if a == '<':
            lista.append(texto)
            texto = ''''''
            separar = 0
        elif a == '>':
            separar = 1

        if separar == 2:
            texto += a

        if separar == 1:
            texto += a
            lista.append(texto)
            texto = ''''''
            separar = 2

        if separar == 0:
            texto += a

    filtered = filter(lambda x: not re.match(r'^\s*$', x), lista)
    texto_para_text_area = ''''''
    for a in filtered:
        texto_para_text_area += a+'\n'

    return HttpResponse(texto_para_text_area)



new_class = ''''''
def separa_styles(request):
    global new_class
    txt = request.POST['foo2']
    separar = 2
    lista = []
    texto = ''''''
    for a in txt:

        if a == '<':
            lista.append(texto)
            texto = ''''''
            separar = 0
        elif a == '>':
            separar = 1

        if separar == 2:
            texto += a

        if separar == 1:
            texto += a
            lista.append(texto)
            texto = ''''''
            separar = 2

        if separar == 0:
            texto += a

    filtered = filter(lambda x: not re.match(r'^\s*$', x), lista)
    texto_para_text_area = ''''''
    class_add = 0


    for a in filtered:
        class_add += 1
        #Solo los que tengan style y class
        if a.find('class') != -1 and a.find('style=') != -1:


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
