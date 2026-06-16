from dotenv import load_dotenv
import os
load_dotenv() # Carrega as variáveis de ambiente do arquivo .env
from services.supabase_service import SupabaseService

supabase =  SupabaseService() # Cria uma instância do serviço do Supabase

contacts = supabase.get_contacts() # Busca os contatos usando o método do serviço

print(contacts) # Imprime os contatos obtidos do Supabase