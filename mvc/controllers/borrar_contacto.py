import web 
from mvc.models.model_contactos import ModelContactos  

render = web.template.render('mvc/views', base='template')  

class BorrarContacto:

    def GET(self, id_contacto): 

        model_contactos = ModelContactos()

        resultado = model_contactos.buscarContacto(int(id_contacto))

        # Envía la lista completa para mantener compatibilidad con $contacto[0] en el HTML
        contacto = resultado if resultado else []

        print(contacto)

        return render.borrar_contacto(contacto) # type: ignore