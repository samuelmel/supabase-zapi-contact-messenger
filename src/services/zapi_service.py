import os
import requests


class ZApiService: # classe para lidar com a API do ZAPI

    def __init__(self):
        self.url = os.getenv("ZAPI_INSTANCE_API")

    def send_message(self, phone: str, name: str): # enviar mensagem para o número de telefone com o nome do contato

        payload = {
            "phone": phone,
            "message": f"Olá, {name} tudo bem com você?"
        }

        try: # tenta enviar a mensagem e retorna o resultado, caso haja um erro, captura a exceção e retorna o erro em formato de dicionário

            response = requests.post(
                self.url,
                json=payload,
                timeout=10
            )

            response.raise_for_status()

            return {
                "success": True,
                "status_code": response.status_code,
                "response": response.json()
            }

        except requests.RequestException as error:

            return {
                "success": False,
                "error": str(error)
            }