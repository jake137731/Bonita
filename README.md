
# BuildBetter

Deployment-ready Streamlit app that translates messy business work into the right AI request.

## Files
- `app.py` — Streamlit UI
- `buildbetter_logic.py` — inference and prompt-building logic
- `tests/test_logic.py` — pytest coverage for core logic
- `requirements.txt`

## Run locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Run tests

```bash
pytest -q
```
