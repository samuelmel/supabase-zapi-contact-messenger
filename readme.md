# Supabase Z-API Contact Messenger

Projeto desenvolvido para o processo seletivo da b2bflow.

A aplicação busca contatos armazenados no Supabase e envia mensagens personalizadas via Z-API utilizando Python.

## Tecnologias Utilizadas

- Python 3.12+
- Supabase
- Z-API
- Requests
- Python Dotenv

## Estrutura da Tabela

Execute o seguinte SQL no Supabase:

```sql
CREATE TABLE contacts (
    id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    name TEXT NOT NULL,
    phone TEXT NOT NULL
);
```

Exemplo de registro:

```sql
INSERT INTO contacts (name, phone)
VALUES
('Gustavo', '5520999999999');
```

## Variáveis de Ambiente

Crie um arquivo `.env` na raiz do projeto:

```env
SUPABASE_URL=
SUPABASE_KEY=
ZAPI_INSTANCE_API=
```

## Instalação

Clone o repositório:

```bash
git clone <repository-url>
```

Crie e ative o ambiente virtual:

```bash
python -m venv .venv
```

Windows:

```bash
.venv\Scripts\activate
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

## Execução

Execute:

```bash
python src/main.py
```

## Funcionamento

1. Busca até 3 contatos cadastrados no Supabase.
2. Personaliza a mensagem utilizando o nome do contato.
3. Envia a mensagem via Z-API.
4. Registra logs da execução.

Mensagem enviada:

```text
Olá, <nome_contato> tudo bem com você?
```

## Logs

Os logs são armazenados em:

```text
logs/app.log
```