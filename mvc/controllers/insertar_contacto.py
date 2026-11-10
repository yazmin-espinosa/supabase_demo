import web 
from mvc.models.model_contactos import ModelContactos  

render = web.template.render('mvc/views', base='template') 


class InsertarContacto:

    # Rederiza la vista insertar_contacto.html
    def GET(self):

        return render.insertar_contacto() # type: ignore
    
    #Recibee los input del formulario y accede a cada uno
    #Utilizando del atributo "name"
    def POST(self):

        #Accede a los datos del formulario 'contactos'
        formulario = web.input()
        #Obtiene el valor del input 'nombre'
        nombre = formulario['nombre']
        #Obtiene el valor del input 'email'
        email = formulario['email']
        #Obtiene el valor del input 'telefono'
        telefono = formulario['telefono']

        #
        #print(f"Nombre: {nombre}")
        #print(f"Email: {email}")
        #print(f"Telefono: {telefono}")

        model_contactos = ModelContactos()
        
        datos=model_contactos.insertarContacto(nombre, email, telefono)

        web.header('Content-Type', 'text/html')
        html = """
            <h1>Contacto almacenado correctamente</h1>
            <a href='/contactos'>Regresar</a>
        """

        return html