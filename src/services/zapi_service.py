from utils.logger import logger
import requests
import os


class ZApiService:

    def __init__(self):

        self.url = os.getenv("ZAPI_INSTANCE_API")

    def send_message(self, phone: str, name: str): # método para enviar uma mensagem usando a API do ZAPI, recebendo o número de telefone e o nome do contato como parâmetros

        payload = {
            "phone": phone,
            "message": f"Olá, {name} tudo bem com você?"
        }

        try:

            response = requests.post(
                self.url,
                json=payload,
                timeout=10
            )

            response.raise_for_status()

            logger.info( # registra uma mensagem de informação no log indicando que a mensagem foi enviada com sucesso para o contato, mostrando o nome e o número de telefone do contato
                f"Message sent to {name} ({phone})"
            )

            return response

        except Exception as error:

            logger.error(
                f"Error sending message to {name}: {error}"
            )

            return None