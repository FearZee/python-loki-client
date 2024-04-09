import datetime
from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.direction import Direction
from ...models.query_range_response_body import QueryRangeResponseBody
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    query: str,
    limit: Union[Unset, int] = 100,
    start: Union[Unset, datetime.datetime, float, int] = UNSET,
    end: Union[Unset, datetime.datetime, float, int] = UNSET,
    step: Union[Unset, datetime.datetime, float, int] = UNSET,
    interval: Union[Unset, float] = UNSET,
    direction: Union[Unset, Direction] = UNSET,
    x_scope_org_id: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}
    if not isinstance(x_scope_org_id, Unset):
        headers["X-Scope-OrgID"] = x_scope_org_id

    params: Dict[str, Any] = {}

    params["query"] = query

    params["limit"] = limit

    json_start: Union[Unset, float, int, str]
    if isinstance(start, Unset):
        json_start = UNSET
    elif isinstance(start, datetime.datetime):
        json_start = start.isoformat()
    else:
        json_start = start
    params["start"] = json_start

    json_end: Union[Unset, float, int, str]
    if isinstance(end, Unset):
        json_end = UNSET
    elif isinstance(end, datetime.datetime):
        json_end = end.isoformat()
    else:
        json_end = end
    params["end"] = json_end

    json_step: Union[Unset, float, int, str]
    if isinstance(step, Unset):
        json_step = UNSET
    elif isinstance(step, datetime.datetime):
        json_step = step.isoformat()
    else:
        json_step = step
    params["step"] = json_step

    params["interval"] = interval

    json_direction: Union[Unset, str] = UNSET
    if not isinstance(direction, Unset):
        json_direction = direction.value

    params["direction"] = json_direction

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/loki/api/v1/query_range",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[QueryRangeResponseBody]:
    if response.status_code == HTTPStatus.OK:
        response_200 = QueryRangeResponseBody.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[QueryRangeResponseBody]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    query: str,
    limit: Union[Unset, int] = 100,
    start: Union[Unset, datetime.datetime, float, int] = UNSET,
    end: Union[Unset, datetime.datetime, float, int] = UNSET,
    step: Union[Unset, datetime.datetime, float, int] = UNSET,
    interval: Union[Unset, float] = UNSET,
    direction: Union[Unset, Direction] = UNSET,
    x_scope_org_id: Union[Unset, str] = UNSET,
) -> Response[QueryRangeResponseBody]:
    """
    Args:
        query (str):
        limit (Union[Unset, int]):  Default: 100.
        start (Union[Unset, datetime.datetime, float, int]):
        end (Union[Unset, datetime.datetime, float, int]):
        step (Union[Unset, datetime.datetime, float, int]):
        interval (Union[Unset, float]):
        direction (Union[Unset, Direction]):
        x_scope_org_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[QueryRangeResponseBody]
    """

    kwargs = _get_kwargs(
        query=query,
        limit=limit,
        start=start,
        end=end,
        step=step,
        interval=interval,
        direction=direction,
        x_scope_org_id=x_scope_org_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    query: str,
    limit: Union[Unset, int] = 100,
    start: Union[Unset, datetime.datetime, float, int] = UNSET,
    end: Union[Unset, datetime.datetime, float, int] = UNSET,
    step: Union[Unset, datetime.datetime, float, int] = UNSET,
    interval: Union[Unset, float] = UNSET,
    direction: Union[Unset, Direction] = UNSET,
    x_scope_org_id: Union[Unset, str] = UNSET,
) -> Optional[QueryRangeResponseBody]:
    """
    Args:
        query (str):
        limit (Union[Unset, int]):  Default: 100.
        start (Union[Unset, datetime.datetime, float, int]):
        end (Union[Unset, datetime.datetime, float, int]):
        step (Union[Unset, datetime.datetime, float, int]):
        interval (Union[Unset, float]):
        direction (Union[Unset, Direction]):
        x_scope_org_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        QueryRangeResponseBody
    """

    return sync_detailed(
        client=client,
        query=query,
        limit=limit,
        start=start,
        end=end,
        step=step,
        interval=interval,
        direction=direction,
        x_scope_org_id=x_scope_org_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    query: str,
    limit: Union[Unset, int] = 100,
    start: Union[Unset, datetime.datetime, float, int] = UNSET,
    end: Union[Unset, datetime.datetime, float, int] = UNSET,
    step: Union[Unset, datetime.datetime, float, int] = UNSET,
    interval: Union[Unset, float] = UNSET,
    direction: Union[Unset, Direction] = UNSET,
    x_scope_org_id: Union[Unset, str] = UNSET,
) -> Response[QueryRangeResponseBody]:
    """
    Args:
        query (str):
        limit (Union[Unset, int]):  Default: 100.
        start (Union[Unset, datetime.datetime, float, int]):
        end (Union[Unset, datetime.datetime, float, int]):
        step (Union[Unset, datetime.datetime, float, int]):
        interval (Union[Unset, float]):
        direction (Union[Unset, Direction]):
        x_scope_org_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[QueryRangeResponseBody]
    """

    kwargs = _get_kwargs(
        query=query,
        limit=limit,
        start=start,
        end=end,
        step=step,
        interval=interval,
        direction=direction,
        x_scope_org_id=x_scope_org_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    query: str,
    limit: Union[Unset, int] = 100,
    start: Union[Unset, datetime.datetime, float, int] = UNSET,
    end: Union[Unset, datetime.datetime, float, int] = UNSET,
    step: Union[Unset, datetime.datetime, float, int] = UNSET,
    interval: Union[Unset, float] = UNSET,
    direction: Union[Unset, Direction] = UNSET,
    x_scope_org_id: Union[Unset, str] = UNSET,
) -> Optional[QueryRangeResponseBody]:
    """
    Args:
        query (str):
        limit (Union[Unset, int]):  Default: 100.
        start (Union[Unset, datetime.datetime, float, int]):
        end (Union[Unset, datetime.datetime, float, int]):
        step (Union[Unset, datetime.datetime, float, int]):
        interval (Union[Unset, float]):
        direction (Union[Unset, Direction]):
        x_scope_org_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        QueryRangeResponseBody
    """

    return (
        await asyncio_detailed(
            client=client,
            query=query,
            limit=limit,
            start=start,
            end=end,
            step=step,
            interval=interval,
            direction=direction,
            x_scope_org_id=x_scope_org_id,
        )
    ).parsed
