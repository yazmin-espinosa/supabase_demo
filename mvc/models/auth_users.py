import os
from supabase import create_client, Client
from dotenv import load_dotenv
import logging

# Lee las variables de entorno
load_dotenv()

# Configura el sistema de logging
logger = logging.getLogger(__name__)

class AuthUsers:

    def __init__(self) -> None:
        try:
            self.supabase: Client = create_client(
                os.environ.get("SUPABASE_URL", ""),
                os.environ.get("SUPABASE_KEY", "")
            )
            
        except Exception as error:
            logger.error(f"ERROR 100: {str(error)}")
            print(f"ERROR 100: {str(error)}")

    def iniciarSesion(self, email:str, password:str):
        try:
            response = self.supabase.auth.sign_in_with_password({
                "email":email,
                "password":password
            })
            print(f"Inicio de sesión exitoso:{response.session.access_token}")
            return response.session.access_token # type: ignore

        except Exception as error:
            logger.error(f"ERROR 101: {str(error)}")
            print(f"ERROR 101: {str(error)}")

    def registrarUsuarios(self, email:str, password:str)-> str | None:
        try:
            response = self.supabase.auth.sign_up({
                "email":email,
                "password":password
            })
            print(f"Usuario registrado exitosamente")
            return response.user.id # type: ignore

        except Exception as error:
            logger.error(f"ERROR 102: {str(error)}")
            print(f"ERROR 102: {str(error)}")
            return None

if __name__=="__main__":
    print("Autenticación de Usuarios")
    objeto = AuthUsers()
    objeto.iniciarSesion("dejah@email.com","12345") # Contraseña no valida
    objeto.iniciarSesion("dejah@email.com","123456") # Contraseña valida