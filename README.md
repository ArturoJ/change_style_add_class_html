change_style_add_class_html
==================

Proyecto sencillo destinado a colaboración para su mejora, que sustituye los style="" dentro de un código html por clases dando el nuevo código y el código css, además perfecto para el desarrollo de traducciones por la separación del texto en líneas sin necesidad de entender código.

Por ejemplo:

``<div style="color: #ffffff">Texto de prueba</div>``


Y lo convierte en lo siguiente:

Código HTML:

``<div class="clas_pers_1">``

``Texto de prueba``

``</div>``

Código CSS:

``.clas_pers_1{``

``    color: #ffffff; ``

``}``


Tenga en cuenta que está desarrollado con:
- Django >= 2.1.7


Funcionamiento
==================

Hay 4 textarea y tres botones:

1º -> Coloque el su código html en texto plano en el primer textarea

2º -> Pulse el botón ``Paso 1``

3º -> Pulse el botón ``Paso 2``

4º -> Pulse el botón ``Pase 3``

Para ver lo que realiza cada botón puede copiar el contenido de los textarea y ver como lo formatea en cada paso.
