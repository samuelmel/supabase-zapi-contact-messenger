from supabase import create_client, Client
import os

class SupabaseService:
    def __init__(self): # Inicializa o cliente do Supabase usando as variáveis de ambiente

        self.client = create_client(
            os.getenv("SUPABASE_URL"),
            os.getenv("SUPABASE_KEY")
        )

    def get_contacts(self): # método para buscar os contatos
        response = (self.client
            .table("contacts")
            .select("*")
            .execute()
        )
        
        return response.data