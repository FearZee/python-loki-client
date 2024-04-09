import json
import time

import httpx
import trio
from grafana_loki_client import Client
from grafana_loki_client.api.format_query import get_loki_api_v1_format_query
from grafana_loki_client.api.query_range import get_loki_api_v1_query_range
from grafana_loki_client.api.ready import get_ready
from rich import print as rprint  # Renamed print function to avoid conflict with built-in print

BASE_URL = "http://localhost:3100"
client = Client(base_url=BASE_URL)

# payload:str = '{foo="bar2"}'
payload:str = 'sum(rate({foo="bar2"}[10m])) by (level)'
dd_keys:list = ["file_name","month", "day", "time", "host", "command_pid", "command_level", "message"]


async def perform_initial_checks():
    # Check readiness of Loki instance
    ready_response = await get_ready.asyncio(client=client)
    if ready_response.status_code == 200:
        rprint("Loki instance is ready.")
    else:
        rprint("Loki instance is not ready. Exiting.")
        return False

    format_query_response = await get_loki_api_v1_format_query.asyncio(client=client, query='{foo= "bar"}')
    if format_query_response.status == "success":
        rprint("Query formatting check passed.")
    else:
        rprint("Query formatting check failed. Exiting.")
        return False

    return True


async def call(url):
    # Perform initial checks before making any query
    initial_checks_passed = await perform_initial_checks()
    if not initial_checks_passed:
        return  # Exit if initial checks fail

    start_time = time.time()
    rprint(start_time)

    r = await url(client=client, query=payload)

    return r


async def gather_data(url) -> list[str]:
    res: list = []
    try:
        r = await call(url)
        if r.status != "success":
            raise httpx.HTTPError(f"HTTP error: {r.status_code}")

        rr = r.data
        # rprint(rr.result)
        if len(rr.result) == 0:
            raise KeyError("Empty Result")

        print(rr.result[0].values)
        for item in rr.result[0].values:
            res.append(item[1])
    except httpx.HTTPError as e:
        rprint(f"HTTP error: {e}")
    except json.JSONDecodeError as e:
        rprint(f"JSON decoding error: {e}")
    # except KeyError as e:
    #     rprint(f"Key error: {e}")
    except Exception as e:
        rprint(f"An error occurred: {e}")
    return res


def create_dict(dd_keys: list, log_list: list) -> dict:
    dd_list = []  #
    rprint(log_list)
    for log in log_list:
        ll = log.split(" ")  # No need to convert to str again
        lll = " ".join(ll[6:])  # Simplified slicing
        dd = {}  # Create a new dictionary for each log
        for i in range(6):
            dd[dd_keys[i]] = ll[i]
        dd[dd_keys[-1]] = lll
        dd_list.append(dd)  # Append each log's dictionary to dd_list
    return dd_list


async def main():
    lista: list = await gather_data(get_loki_api_v1_query_range.asyncio)
    rprint(lista)

    # dd_list: list = create_dict(dd_keys, lista)
    # rprint(dd_list)


if __name__ == "__main__":
    trio.run(main)  # Execute the main function using trio.run
