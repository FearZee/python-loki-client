from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.volume_response import VolumeResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    query: str,
    start: int,
    end: int,
    limit: Union[Unset, int] = 100,
    step: Union[Unset, str] = UNSET,
    target_labels: Union[Unset, str] = UNSET,
    aggregate_by: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["query"] = query

    params["start"] = start

    params["end"] = end

    params["limit"] = limit

    params["step"] = step

    params["targetLabels"] = target_labels

    params["aggregateBy"] = aggregate_by

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/loki/api/v1/index/volume_range",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[VolumeResponse]:
    if response.status_code == HTTPStatus.OK:
        response_200 = VolumeResponse.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[VolumeResponse]:
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
    start: int,
    end: int,
    limit: Union[Unset, int] = 100,
    step: Union[Unset, str] = UNSET,
    target_labels: Union[Unset, str] = UNSET,
    aggregate_by: Union[Unset, str] = UNSET,
) -> Response[VolumeResponse]:
    """
    Args:
        query (str):
        start (int):
        end (int):
        limit (Union[Unset, int]):  Default: 100.
        step (Union[Unset, str]):
        target_labels (Union[Unset, str]):
        aggregate_by (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[VolumeResponse]
    """

    kwargs = _get_kwargs(
        query=query,
        start=start,
        end=end,
        limit=limit,
        step=step,
        target_labels=target_labels,
        aggregate_by=aggregate_by,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    query: str,
    start: int,
    end: int,
    limit: Union[Unset, int] = 100,
    step: Union[Unset, str] = UNSET,
    target_labels: Union[Unset, str] = UNSET,
    aggregate_by: Union[Unset, str] = UNSET,
) -> Optional[VolumeResponse]:
    """
    Args:
        query (str):
        start (int):
        end (int):
        limit (Union[Unset, int]):  Default: 100.
        step (Union[Unset, str]):
        target_labels (Union[Unset, str]):
        aggregate_by (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        VolumeResponse
    """

    return sync_detailed(
        client=client,
        query=query,
        start=start,
        end=end,
        limit=limit,
        step=step,
        target_labels=target_labels,
        aggregate_by=aggregate_by,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    query: str,
    start: int,
    end: int,
    limit: Union[Unset, int] = 100,
    step: Union[Unset, str] = UNSET,
    target_labels: Union[Unset, str] = UNSET,
    aggregate_by: Union[Unset, str] = UNSET,
) -> Response[VolumeResponse]:
    """
    Args:
        query (str):
        start (int):
        end (int):
        limit (Union[Unset, int]):  Default: 100.
        step (Union[Unset, str]):
        target_labels (Union[Unset, str]):
        aggregate_by (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[VolumeResponse]
    """

    kwargs = _get_kwargs(
        query=query,
        start=start,
        end=end,
        limit=limit,
        step=step,
        target_labels=target_labels,
        aggregate_by=aggregate_by,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    query: str,
    start: int,
    end: int,
    limit: Union[Unset, int] = 100,
    step: Union[Unset, str] = UNSET,
    target_labels: Union[Unset, str] = UNSET,
    aggregate_by: Union[Unset, str] = UNSET,
) -> Optional[VolumeResponse]:
    """
    Args:
        query (str):
        start (int):
        end (int):
        limit (Union[Unset, int]):  Default: 100.
        step (Union[Unset, str]):
        target_labels (Union[Unset, str]):
        aggregate_by (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        VolumeResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            query=query,
            start=start,
            end=end,
            limit=limit,
            step=step,
            target_labels=target_labels,
            aggregate_by=aggregate_by,
        )
    ).parsed
