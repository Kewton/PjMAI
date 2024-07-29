# setup(macbook)
```
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

# initialize
init database
```
python3 initdatabase.py
```

create secret_keys.py
```python
openai_api_key = <your api key>
claude_api_key = <your api key>
```

# exec
```
streamlit run run.py 
```