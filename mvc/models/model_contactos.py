
import os
from supabase import create_client, Client
from dotenv import load_dotenv

load_dotenv()

class ModelContactos:

    def __init__(self) -> None:
        try:
            self.supabase: Client = create_client(
                os.environ.get("SUPABASE_URL", ""),
                os.environ.get("SUPABASE_KEY", "")
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
        response = self.supabase.table("contactos").select("*").eq("id", id_contacto).execute()
        return response.data

    # Inserta un registro
    # El try y el ecxept sirve para ver errores de manera mas facil.
    # Se ele puede poner cualquier numero pero conviene hacerlso desde el 100
    def insertarContacto(self, nombre, email, telefono):
        datos = {
            "nombre": nombre,
            "email": email,
            "telefono": telefono
        }
        response = self.supabase.table("contactos").insert(datos).execute()
        return response.data
    except Exception as error:
        print(f"ERROR 103: {os.error.args[0]}")

    # Borra un registro por su ID
    def borrarContacto(self, id_contacto: int):
        response = self.supabase.table("contactos").delete().eq("id", id_contacto).execute()
        return response.data

    # Actualiza un registro por su ID
    def actualizarContacto(self, id_contacto: int, nombre, email, telefono):
        datos = {
            "nombre": nombre,
            "email": email,
            "telefono": telefono
        }
        response = self.supabase.table("contactos").update(datos).eq("id", id_contacto).execute()
        return response.data

if __name__ == "__main__":
    model_contactos = ModelContactos()
    #print(model_contactos.obtenerContactos())
    #print(model_contactos.buscarContacto(1))
    #print(model_contactos.insertarContacto("harry","harry@gmail.com","1234567890"))
    #print(model_contactos.borrarContacto(3))
    #print(model_contactos.actualizarContacto(2,"harry","harry3@gmail.com","6578490678"))
