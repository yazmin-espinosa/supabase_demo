import os
import hashlib
import hmac
import logging
from typing import Any, cast
from supabase import create_client, Client
from dotenv import load_dotenv

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
            logger.error("ERROR 100: %s", error)
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
            response = self.supabase.table("contactos").select("*").execute()
            registros = response.data or []
            
            for registro in registros:
                # Si tu columna en Supabase se llama "id", la leemos aquí
                # y creamos/modificamos el campo "id_contacto" para la vista
                id_num = int(registro.get("id") or registro.get("id_contacto"))
                registro["id_contacto"] = self.generar_hash(id_num)
                contactos.append(registro)
                
            return contactos
        except Exception as error:
            logger.error("ERROR 101: %s", error)
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
            logger.error("ERROR 102: %s", error)
            print(f"ERROR 102: {str(error)}")
            return []

    def insertarContacto(self, nombre: str, email: str, telefono: str):
        try:
            datos = {
                "nombre": nombre,
                "email": email,
                "telefono": telefono
            }
            response = self.supabase.table("contactos").insert(datos).execute()
            return response.data
        except Exception as error:
            logger.error("ERROR 103: %s", error)
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
            logger.error("ERROR 104: %s", error)
            print(f"ERROR 104: {str(error)}")
            return None

    def actualizarContacto(self, id_contacto: str, nombre: str, email: str, telefono: str):
        try:
            id_real = self.validar_hash(id_contacto)
            if id_real is None:
                return None
            datos = {
                "nombre": nombre,
                "email": email,
                "telefono": telefono
            }
            response = self.supabase.table("contactos").update(datos).eq("id", id_real).execute()
            return response.data
        except Exception as error:
            logger.error("ERROR 105: %s", error)
            print(f"ERROR 105: {str(error)}")
            return None