from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from urllib.parse import quote_plus

app = FastAPI()

@app.get("/go/gmail")
def go_gmail(p: str = "", u: str = "", d: str = ""):
    to = "info@thegooddecisions.com"
    su = f"Solicitud de presupuesto - {p} - {u}"
    body = f"""Hola TheGoodDecisions,

Quiero cotizar un proyecto:

- Producto(s): {p}
- Unidades por producto: {u}
- Fecha objetivo: {d}

Adjunto (si aplica):
- Ficha técnica
- Diseños vectoriales (.AI, .PDF o .SVG)

Detalles extra:
- Técnica de personalización (DTF, bordado, serigrafía, etc.)
- Tamaños y posiciones del diseño
- Colores (Pantone si aplica)
- Acabados finales (empaquetado, planchado, etc.)

Gracias."""
    gmail_url = (
        "https://mail.google.com/mail/?view=cm&fs=1"
        f"&to={quote_plus(to)}"
        f"&su={quote_plus(su)}"
        f"&body={quote_plus(body)}"
    )
    return RedirectResponse(gmail_url, status_code=302)
