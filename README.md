# Test task for data import into postgresql

1. To import the data you need to unpack split.rar into this folder.
   Split.rar contains in_network_00.jsonl that will be imported into the database.
2. Then you will need to install all python dependencies either via
   `pip install -r requirements.txt` or `uv sync && source .venv/bin/activate`
3. After it you need to run main.py, which will import network prices into db:
   `uv run main.py` or `python main.py`
4. If you want to run api.py and check out localhost:8000/docs or localhost:8000/redoc:
   `uv run api.py` or `python3 api.py`

Optionally you could run the postgresql yourself or spin it up with docker-compose:
`docker compose up -d`