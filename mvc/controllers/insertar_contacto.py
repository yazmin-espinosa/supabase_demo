import os
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
        formulario = web.input(foto={})
        #Obtiene el valor del input 'nombre'
        nombre = formulario['nombre']
        #Obtiene el valor del input 'email'
        email = formulario['email']
        #Obtiene el valor del input 'telefono'
        telefono = formulario['telefono']

        archivo = formulario['foto']
        foto = archivo.filename

        ruta = os.path.join("static/fotos/",foto)
        with open(ruta, "wb") as file:
            file.write(formulario.foto.read())

        model_contactos = ModelContactos()
        datos = model_contactos.insertarContacto(nombre, email, telefono,foto)

        web.header('Content-Type', 'text/html')
        html = """
            <h1>Contacto almacenado correctamente</h1>
            <a href='/contactos'>Regresar</a>
        """

        return html