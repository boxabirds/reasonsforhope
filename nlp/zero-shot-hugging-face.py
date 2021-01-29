# from here https://api-inference.huggingface.co/docs/python/html/detailed_parameters.html#which-task-is-used-by-this-model

import json
import requests
import argparse
import sys
from timed import timed
import logging
log = logging.getLogger()
log.setLevel(logging.DEBUG)

# send logging to stdout and capture method timing
handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
log.addHandler(handler)

API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-mnli"



@timed
def query(payload, api_token):
    headers = {"Authorization": f"Bearer {api_token}"}
    data = json.dumps(payload)
    response = requests.request("POST", API_URL, headers=headers, data=data)
    return json.loads(response.content.decode("utf-8"))


parser = argparse.ArgumentParser()
parser.add_argument("--api-token", help="Huggingface API token from here: https://huggingface.co/settings/token")
args = parser.parse_args()
api_token = args.api_token
result = query(
    payload={
        "inputs": [
            "To Reduce Climate Impacts, the Building Industry Must Change",
            "Forecasting the 2021 renewable energy landscape",
            "This single number could reshape our climate future",
            "'We can't wait any longer': Joe Biden signs executive orders to address climate crisis",
            "Clean Energy Attracts Half A Trillion Dollars Of Funding For First Time",
            "Eco search engine commits to planting 1bn trees in Africa’s ‘Great Green Wall’",
            "Methane emissions from coal mines are higher than previously thought’",
            "Global ice loss is catching up to worst-case scenario predictions’",
            "Earth Loses 1.2 Trillion Tons of Ice Per Year, a Nearly 60% Increase From 1994",
        ],
        "parameters": {"candidate_labels": ["positive", "negative", "neutral"]},
    },
    api_token=api_token
    )

log.debug(json.dumps(result,indent=2))
