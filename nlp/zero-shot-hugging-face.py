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
            "Everyday shopping from brands like Heinz and Yakult helps destroy rainforests, report claims.",
            "Everyday shopping from brands like Heinz and Yakult helps destroy rainforests, report claims. Big companies and lenders ‘failing to halt loss of vital tree cover’, contributing to nature and climate crises. Shoppers are unknowingly fuelling the destruction of tropical rainforests, as companies produce millions of everyday products linked to deforestation, a report claims. Brands including Kraft Heinz, Starbucks, Yakult and Rachel’s Organic buy large amounts of products such as soya to feed animals – for which swathes of tropical forests are cleared. And nearly 100 major financial institutions, including Blackrock, are ignoring tropical deforestation in their public policies, while providing $2.7 trillion (£2 trillion) that risks fuelling the climate and biodiversity crisis, the analysis says. Every six seconds an area of rainforest the size of a football pitch is destroyed to produce commodities such as soya, beef, palm oil, leather, timber and paper, according to environmental organisation Global Canopy. Destroying these forests is one of the biggest causes of the twin climate and biodiversity crises. The charity’s annual Forest 500 Report looked at 350 companies worldwide that produce, trade or use the largest amounts of those products, and their lenders, and ranked them by their relevant policies. It found that 107 companies whose products use meat, fish, dairy and eggs failed to recognise their links to deforestation through the soya they bought for animal feed.  ",
        ],
        "parameters": {"candidate_labels": ["positive", "negative", "neutral"]},
    },
    api_token=api_token
    )

log.debug(json.dumps(result,indent=2))
