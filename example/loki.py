import httpx #https://www.python-httpx.org
import trio # async handling https://github.com/python-trio/trio 
import tempfile
from rich import print as print # handles all kind of console output in an appealing manner
import rich.progress
import json
import time

from grafana_loki_client import Client
from grafana_loki_client.api.ready import get_ready
from grafana_loki_client.api.query import get_loki_api_v1_query



BASE_URL = "http://localhost:3100"
client = Client(base_url=BASE_URL)

basic_info:dict = {
    "url_ready": '/ready',
    "url_log_level": '/log_level',
    "url_service": '/services',
    "url_config": '/config',
    "url_metrics": '/metrics',
    "url_check_query":'/loki/api/v1/format_query'
}

"""for key in basic_info:
    print(f" {str(key).upper()[4:]} : {httpx.get(basic_info[key]).text}")"""

###### works good, maybe a class and separate handling ---> meta info; info regarding the system

#payload:str = 'query={host=~".*", filename="/var/log/auth.log"} |= `` ' # works
payload:str = 'query={job="varlogs"} |= ``|json ' # 

url02:str = '/loki/api/v1/query'
url03:str = '/loki/api/v1/query'
"""
url04:str = '/loki/api/v1/status/buildinfo'
url05:str = 
url06:str = '/loki/api/v1/labels'
url12:str = '/loki/api/v1/series'

url14:str = '/loki/api/v1/index/volume' #<-
"""
# url06:str = '/loki/api/v1/labels'
# r06 = httpx.get(url06)
# print(r06.text)
# r02 = httpx.get(url02)
"""
r04 = httpx.get(url04)
r05 = httpx.get(url05, params=payload)
#r06 = httpx.get(url06)"""
#print(r03.keys())
#print(r03["data"].keys())
#print(r03["data"]["result"])
#print(dict(r03["data"]["result"][0]).keys())
#print(dict(r03["data"]["result"][0])["values"]) <----- #List of lists


async def call(url):
    start_time = time.time()
    print(start_time)

    if get_loki_api_v1_format_query.asyncio(client=client):
        return url()
    else:
        print(f"Your query: {payload} is not valid")

async def gather_data(url)->list[str]:
    res: list = list()
    try:
        r = await call(url())
        print(1)
        rr:dict = r.json()
        print(2)
        print(rr)
        for i in list(dict(rr["data"]["result"][0])["values"]):
            res.append(i[1])
    except:
        # wait one minute and play a game
        print("try again in one minute")
    return res

def clear(string:str, character:str)->str:
    return "".join(i for i in string if i not in character)

dd_keys:list = ["file_name","month", "day", "time", "host", "command_pid", "command_level", "message"]

def create_dict(dd_keys:list,log_list:list)->dict[str,str]:

    dd: dict = dict()
    for log in log_list:
        print(log)
        ll = str(log).split(" ")
        lll:str = " ".join(i for i in ll[6:])
        for i in range(6):
            dd[dd_keys[i]] = ll[i]
        dd[dd_keys[-1]] = lll



lista:list = trio.run(gather_data, get_loki_api_v1_query.asyncio(client=client, query=payload))
print(lista)

dd : dict = create_dict(dd_keys,lista)
print(dd)
#### scanner  -- lexer --- parser

# print(httpx.get(basic_info["url_log_level"]).text)
# print(httpx.get(basic_info["url_service"]).text)