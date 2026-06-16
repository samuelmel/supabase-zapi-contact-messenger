from supabase import create_client
from utils.logger import logger
import os


class SupabaseService:

    def __init__(self):

        self.client = create_client(
            os.getenv("SUPABASE_URL"),
            os.getenv("SUPABASE_KEY")
        )

    def get_contacts(self, limit: int = 3): # método para obter os contatos do Supabase, com um limite de 3 contatos por padrão

        try:

            response = (
                self.client
                .table("contacts")
                .select("*")
                .limit(limit)
                .execute()
            )

            logger.info # registra uma mensagem de informação no log indicando quantos contatos foram carregados com sucesso
            (
                f"{len(response.data)} contacts loaded"
            )

            return response.data

        except Exception as error: # captura qualquer exceção que possa ocorrer durante a obtenção dos contatos e imprime o erro, retornando uma lista vazia

            print(
                f"Error fetching contacts: {error}"
            )

            return []