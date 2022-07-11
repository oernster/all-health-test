from fastapi import APIRouter
from fastapi.responses import HTMLResponse


router = APIRouter()


@router.get("/", tags=["root"], response_class=HTMLResponse)
def read_root():
    return """<html><header><H1>Exchange rate retrieval API.</H1></header>
              <body><H2>Pre-requisites:</H2>
              <p>1) Run source virtualenv venv on the command line.<\p>
              <p>2) Run pip3 install -r requirements.txt</p>
              <p>3) Run python3 ingest.py</body></p>
              <H3>API docs can be found at /docs or /redoc</H3></html>"""
    return html
