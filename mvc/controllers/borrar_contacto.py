import web 
from mvc.models.model_contactos import ModelContactos  

render = web.template.render('mvc/views', base='template') 

class BorrarContacto:

    def GET(self, id_contacto):

        model_contactos = ModelContactos()

        resultado = model_contactos.buscarContacto(id_contacto)

        # Pasa la lista completa (resultado) o una lista vacía para mantener la estructura de la vista
        contacto = resultado if resultado else []

        print(contacto)

        return render.borrar_contacto(contacto) # type: ignore

    def POST(self, id_contacto):

        model_contactos = ModelContactos()

        model_contactos.borrarContacto(id_contacto)

        raise web.seeother('/contactos')