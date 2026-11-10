import web 
from mvc.models.model_contactos import ModelContactos 

render = web.template.render('mvc/views', base='template')  

class ActualizarContacto:

    def GET(self, id_contacto): 

        model_contactos = ModelContactos()

        resultado = model_contactos.buscarContacto(int(id_contacto))
        
        contacto = resultado[0] if resultado else {} 

        print(contacto)  

        return render.actualizar_contacto(contacto) # type: ignore 