from airflow.lineage.backend import LineageBackend
from airflow.lineage.entities import File

import requests

class ExampleBackend(LineageBackend):

    def send_lineage(self, operator, inlets=None, outlets=None, context=None):
        url = "https://webhook.site/8fe779dc-10ae-4917-8f41-685723a31064"
        data = {
            "operator": operator.__class__.__name__,
            "inlets": [str(inlet) for inlet in inlets],
            "outlets": [str(outlet) for outlet in outlets],
            "context": context,
        }
        try:
            requests.post(url, json=data)
            operator.log.info(f"Sent lineage to {url}: {data}")
        except Exception as e:
            operator.log.error(e)
