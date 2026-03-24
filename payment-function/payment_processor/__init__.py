import logging
import json
import azure.functions as func
from ..function_app import match_payments

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("Processing payment matching request.")

    try:
        data = req.get_json()

        payments = data.get("payments", [])
        invoices = data.get("invoices", [])

        result = match_payments(payments, invoices)

        return func.HttpResponse(
            json.dumps(result),
            mimetype="application/json",
            status_code=200
        )

    except Exception as e:
        logging.error(f"Error: {str(e)}")
        return func.HttpResponse(str(e), status_code=500)