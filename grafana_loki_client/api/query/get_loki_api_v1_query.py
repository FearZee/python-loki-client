import datetime
from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.direction import Direction
from ...models.query_response_body import QueryResponseBody
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    query: str,
    limit: int = 100,
    time: Union[Unset, datetime.datetime] = UNSET,
    direction: Direction,
    x_scope_org_id: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}
    if not isinstance(x_scope_org_id, Unset):
        headers["X-Scope-OrgID"] = x_scope_org_id

    params: Dict[str, Any] = {}

    params["query"] = query

    params["limit"] = limit

    json_time: Union[Unset, str] = UNSET
    if not isinstance(time, Unset):
        json_time = time.isoformat()
    params["time"] = json_time

    json_direction = direction.value
    params["direction"] = json_direction

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/loki/api/v1/query",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[QueryResponseBody]:
    if response.status_code == HTTPStatus.OK:
        response_200 = QueryResponseBody.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[QueryResponseBody]:
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
    limit: int = 100,
    time: Union[Unset, datetime.datetime] = UNSET,
    direction: Direction,
    x_scope_org_id: Union[Unset, str] = UNSET,
) -> Response[QueryResponseBody]:
    """
    Args:
        query (str):
        limit (int):  Default: 100.
        time (Union[Unset, datetime.datetime]):
        direction (Direction):
        x_scope_org_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[QueryResponseBody]
    """

    kwargs = _get_kwargs(
        query=query,
        limit=limit,
        time=time,
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
    limit: int = 100,
    time: Union[Unset, datetime.datetime] = UNSET,
    direction: Direction,
    x_scope_org_id: Union[Unset, str] = UNSET,
) -> Optional[QueryResponseBody]:
    """
    Args:
        query (str):
        limit (int):  Default: 100.
        time (Union[Unset, datetime.datetime]):
        direction (Direction):
        x_scope_org_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        QueryResponseBody
    """

    return sync_detailed(
        client=client,
        query=query,
        limit=limit,
        time=time,
        direction=direction,
        x_scope_org_id=x_scope_org_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    query: str,
    limit: int = 100,
    time: Union[Unset, datetime.datetime] = UNSET,
    direction: Direction,
    x_scope_org_id: Union[Unset, str] = UNSET,
) -> Response[QueryResponseBody]:
    """
    Args:
        query (str):
        limit (int):  Default: 100.
        time (Union[Unset, datetime.datetime]):
        direction (Direction):
        x_scope_org_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[QueryResponseBody]
    """

    kwargs = _get_kwargs(
        query=query,
        limit=limit,
        time=time,
        direction=direction,
        x_scope_org_id=x_scope_org_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    query: str,
    limit: int = 100,
    time: Union[Unset, datetime.datetime] = UNSET,
    direction: Direction,
    x_scope_org_id: Union[Unset, str] = UNSET,
) -> Optional[QueryResponseBody]:
    """
    Args:
        query (str):
        limit (int):  Default: 100.
        time (Union[Unset, datetime.datetime]):
        direction (Direction):
        x_scope_org_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        QueryResponseBody
    """

    return (
        await asyncio_detailed(
            client=client,
            query=query,
            limit=limit,
            time=time,
            direction=direction,
            x_scope_org_id=x_scope_org_id,
        )
    ).parsed
