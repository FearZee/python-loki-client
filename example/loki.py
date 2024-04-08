import httpx
import trio
import tempfile
from rich import print as rprint  # Renamed print function to avoid conflict with built-in print
import json
import time

from grafana_loki_client import Client
from grafana_loki_client.api.ready import get_ready
from grafana_loki_client.api.query import get_loki_api_v1_query
from grafana_loki_client.api.format_query import get_loki_api_v1_format_query

BASE_URL = "http://localhost:3100"
client = Client(base_url=BASE_URL)

payload:str = 'query={job="varlogs"} |= ``|json '
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
    res: list = []  # Use list literal instead of list()
    try:
        r = await call(url)  # Await the result of the call function
        print(1)
        rr: dict = r.json()
        rprint(2)
        rprint(rr)
        for i in dict(rr["data"]["result"][0])["values"]:
            res.append(i[1])
    except Exception as e:  # Catch specific exceptions here
        rprint(f"An error occurred: {e}")
        rprint("Try again in one minute")
    return res


def create_dict(dd_keys: list, log_list: list) -> dict:
    dd_list = []  # Use list to store dictionaries instead of overwriting dd in each iteration
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
    lista: list = await gather_data(get_loki_api_v1_query.asyncio)
    rprint(lista)

    dd_list: list = create_dict(dd_keys, lista)
    rprint(dd_list)


if __name__ == "__main__":
    trio.run(main)  # Execute the main function using trio.run
