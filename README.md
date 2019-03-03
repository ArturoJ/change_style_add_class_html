change_style_add_class_html
==================

Proyecto sencillo que sustituye los style=”” dentro de un código html por clases dando el nuevo código y el código css, además perfecto para el desarrollo de traducciones por la separación del texto en líneas sin necesidad de entender código.
Por ejemplo:
``<div style=”color: #ffffff”>Texto de prueba</div>``
Y lo convierte en lo siguiente:
``<div class="clas_pers_1">``
``Texto de prueba``
``</div>``

``.clas_pers_1{``
``    color: #ffffff; ``
``}``
Tenga en cuenta que está desarrollado con:
- Django >= 2.1.7


