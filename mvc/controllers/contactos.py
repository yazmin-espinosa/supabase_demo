import web 
from mvc.models.model_contactos import ModelContactos  

render = web.template.render('mvc/views', base='template') 

class Contactos:

    def GET(self):

        model_contactos = ModelContactos() 

        # Almacena en datos los registros recibidos de Supabase
        datos = model_contactos.obtenerContactos()

        print(datos) 

        # Envía los datos recibidos a la vista contactos.html 
        return render.contactos(datos) 
    