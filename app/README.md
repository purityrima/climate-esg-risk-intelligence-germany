# Streamlit deployment

Run the platform from the repository root:

```bash
python -m pip install -r requirements-deploy.txt
streamlit run app/streamlit_app.py
```

For Streamlit Community Cloud, select `app/streamlit_app.py` as the entrypoint
and Python 3.12 as the runtime. The deployed application reads only processed
data and exported model artefacts; it does not retrain the FFNN.
