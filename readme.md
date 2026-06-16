# Supabase + Z-API Challenge

Projeto desenvolvido para processo seletivo da b2bflow.

## Tecnologias

- Python
- Supabase
- Z-API
- python-dotenv

## Configuração

Crie um arquivo `.env` baseado em `.env.example`.

## Banco

Execute o script `setup.sql` no Supabase.

## Instalação

```bash
pip install -r requirements.txt
```

## Execução

```bash
python src/main.py
```

## Fluxo

1. Busca contatos no Supabase
2. Personaliza a mensagem
3. Envia via Z-API
4. Registra logs da execução