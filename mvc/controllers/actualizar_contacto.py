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

        form = web.input()
        nombre = form.get('nombre', '')
        email = form.get('email', '')
        telefono = form.get('telefono', '')

        model_contactos.actualizarContacto(id_contacto, nombre, email, telefono)

        raise web.seeother('/contactos')