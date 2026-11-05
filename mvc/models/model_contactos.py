import os
from supabase import create_client, Client
from dotenv import load_dotenv

load_dotenv()

class ModelContactos:

    def __init__(self) -> None:
        try:
            self.supabase: Client = create_client(
                os.environ.get("SUPABASE_URL" , ""),
                os.environ.get("SUPABASE_KEY" , "")
            )
        except Exception as error:
            print(f"ERROR 100: {error.args[0]}")

    # Muestra todos los registros
    def obtenerContactos(self):
        # SELECT * FROM CONTACTOS;
        response = self.supabase.table("contactos").select("*").execute()
        return response.data

    # Muestra un solo registro
    def buscarContacto(self, id_contacto: int):
        response = self.supabase.table("contactos").select("*").eq("id_contacto", id_contacto).execute()
        return response.data

    # Inserta un registro
    def insertarContacto(self, nombre, email, telefono):
        datos = {
            "nombre": nombre,
            "email": email,
            "telefono": telefono
        }
        response = self.supabase.table("nombre").insert(datos).excute()
        return response.data

    def borrarContacto(self, id_contacto: int):
        response = self.supabase.table("contactos").delete().eq("id_contacto").excute()
        return response.data

    def actualizarContacto(self, nombre, email, telefono):
        datos = {
            "nombre": nombre,
            "emil": email,
            "telefono": telefono
        }
        response = self.supabase.table("contactos").select("*").eq("id_contacto")
        return response.data

if __name__ == "__main__":
    model_contactos = ModelContactos()
    #print(model_contactos.obtenerContactos())
    #print(model_contactos.buscarContacto(2))
    #print(model_contactos.insertarContacto("harry","harry@gmail.com","1234567890"))
    #print(model_contactos.borrarContacto(2))
    #print(model_contactos.actualizarContacto("harry","harry3@gmai.com","6578490678"))