from dotenv import load_dotenv

from services.supabase_service import SupabaseService
from services.zapi_service import ZApiService
from utils.logger import logger

load_dotenv()

logger.info("Application started")

supabase = SupabaseService()
zapi = ZApiService()

contacts = supabase.get_contacts() # obtém a lista de contatos do Supabase e armazena na variável contacts

for contact in contacts:

    response = zapi.send_message(
        contact["phone"],
        contact["name"]
    )

    print(
        f"Mensagem enviada para {contact['name']} - Status: {response.status_code}" # imprime o resultado do envio da mensagem para cada contato, mostrando o nome do contato e o status da resposta
    )

logger.info("Application finished")