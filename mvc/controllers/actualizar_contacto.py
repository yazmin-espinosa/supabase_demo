import os
import web 
from mvc.models.model_contactos import ModelContactos  

render = web.template.render('mvc/views', base='template') 

class ActualizarContacto:

    def GET(self, id_contacto):

        model_contactos = ModelContactos()

        resultado = model_contactos.buscarContacto(id_contacto)

        # Pasa la lista completa (resultado) o una lista vacía para mantener la estructura de la vista
        contacto = resultado if resultado else []

        print(contacto)

        return render.actualizar_contacto(contacto) # type: ignore

    def POST(self, id_contacto):

        model_contactos = ModelContactos()

        # Busca el contacto actual para conservar su foto si no se sube una nueva
        resultado = model_contactos.buscarContacto(id_contacto)
        foto = resultado[0]['foto'].strip() if resultado and resultado[0].get('foto') else 'default.png'

        form = web.input(foto={})
        nombre = form.get('nombre', '')
        email = form.get('email', '')
        telefono = form.get('telefono', '')

        archivo = form.get('foto')
        if archivo and getattr(archivo, 'filename', ''):
            foto = os.path.basename(archivo.filename)
            ruta = os.path.join("static", "foto", foto)
            contenido = archivo.value if hasattr(archivo, 'value') else archivo.file.read()
            with open(ruta, "wb") as file:
                file.write(contenido)

        model_contactos.actualizarContacto(id_contacto, nombre, email, telefono, foto)

        raise web.seeother('/contactos')