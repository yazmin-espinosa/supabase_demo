import os
from supabase import create_client, Client
from dotenv import load_dotenv
import hashlib
import hmac
from typing import Any, cast
import logging

load_dotenv()

logger = logging.getLogger(__name__)

class ModelContactos:

    def __init__(self) -> None:
        try:
            self.supabase: Client = create_client(
                os.environ.get("SUPABASE_URL", ""),
                os.environ.get("SUPABASE_KEY", "")
            )
            self.SECRET_KEY = b"holi"
        except Exception as error:
            logger.error(f"ERROR 100: {str(error)}")
            print(f"ERROR 100: {str(error)}")

    def generar_hash(self, id: int) -> str:
        try:
            mensaje = str(id).encode("utf-8")
            firma = hmac.new(self.SECRET_KEY, mensaje, hashlib.sha256).hexdigest()
            return f"{id}:{firma}"
        except Exception as error:
            logger.error("ERROR 106: %s", error)
            print(f"ERROR 106: {str(error)}")
            return ""

    def validar_hash(self, hash_a_validar: str) -> int | None:
        try:
            id_str, sep, _ = hash_a_validar.partition(":")
            if sep and id_str.isdigit():
                token_esperado = self.generar_hash(int(id_str))
                if hmac.compare_digest(token_esperado, hash_a_validar):
                    return int(id_str)
            return None
        except Exception as error:
            logger.error("ERROR 107: %s", error)
            print(f"ERROR 107: {str(error)}")
            return None

    def obtenerContactos(self) -> list[dict[str, Any]]:
        contactos: list[dict[str, Any]] = []
        try:
            response = self.supabase.table("contactos").select("*").order("id", desc=False).execute()
            registros = response.data or []
            
            for registro in registros:
                reg = cast(dict[str, Any], registro)
                id_num = int(reg.get("id") or reg.get("id_contacto") or 0)
                reg["id_contacto"] = self.generar_hash(id_num)
                contactos.append(reg)

            return contactos
        except Exception as error:
            logger.error(f"ERROR 101: {str(error)}")
            print(f"ERROR 101: {str(error)}")
            return []

    def buscarContacto(self, id_contacto: str):
        try:
            id_real = self.validar_hash(id_contacto)
            if id_real is None:
                return []
            # Filtramos por el ID entero original de Supabase (columna "id")
            response = self.supabase.table("contactos").select("*").eq("id", id_real).execute()
            return response.data
        except Exception as error:
            logger.error(f"ERROR 102: {str(error)}")
            print(f"ERROR 102: {str(error)}")
            return []

    def insertarContacto(self, nombre: str, email: str, telefono: str, foto: str):
        try:
            #INSERT INTO contactos(nombre, email, telefono, foto) VALUES(?, ?, ?, ?,);
            datos = {
                "nombre": nombre,
                "email": email,
                "telefono": telefono,
                "foto": foto
            }
            response = self.supabase.table("contactos").insert(datos).execute()
            return response.data
        except Exception as error:
            logger.error(f"ERROR 103: {str(error)}")
            print(f"ERROR 103: {str(error)}")
            return None

    def borrarContacto(self, id_contacto: str):
        try:
            id_real = self.validar_hash(id_contacto)
            if id_real is None:
                return None
            response = self.supabase.table("contactos").delete().eq("id", id_real).execute()
            return response.data
        except Exception as error:
            logger.error(f"ERROR 104: {str(error)}")
            print(f"ERROR 104: {str(error)}")
            return None

    def actualizarContacto(self, id_contacto: str, nombre: str, email: str, telefono: str, foto: str):
        try:
            id_real = self.validar_hash(id_contacto)
            if id_real is None:
                return None
            datos = {
                "nombre": nombre,
                "email": email,
                "telefono": telefono,
                "foto": foto
            }
            response = self.supabase.table("contactos").update(datos).eq("id", id_real).execute()
            return response.data
        except Exception as error:
            logger.error(f"ERROR 105: {str(error)}")
            print(f"ERROR 105: {str(error)}")
            return None

if __name__=="__main__":
    model_contactos = ModelContactos()
    print(model_contactos.obtenerContactos())
    print(model_contactos.buscarContacto("1:hash_ejemplo"))
    print(model_contactos.insertarContacto("Juan", "juan@email.com", "5551234567", "default.png"))
    print(model_contactos.actualizarContacto("1:hash_ejemplo", "Juan", "juan@email.com", "5551234567", "default.png"))
    print(model_contactos.borrarContacto("1:hash_ejemplo"))