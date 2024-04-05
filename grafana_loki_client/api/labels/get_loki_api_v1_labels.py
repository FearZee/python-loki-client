from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.labels_response_body import LabelsResponseBody
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    start: Union[Unset, int] = UNSET,
    end: Union[Unset, int] = UNSET,
    since: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["start"] = start

    params["end"] = end

    params["since"] = since

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/loki/api/v1/labels",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[LabelsResponseBody]:
    if response.status_code == HTTPStatus.OK:
        response_200 = LabelsResponseBody.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[LabelsResponseBody]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    start: Union[Unset, int] = UNSET,
    end: Union[Unset, int] = UNSET,
    since: Union[Unset, str] = UNSET,
) -> Response[LabelsResponseBody]:
    """
    Args:
        start (Union[Unset, int]):
        end (Union[Unset, int]):
        since (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[LabelsResponseBody]
    """

    kwargs = _get_kwargs(
        start=start,
        end=end,
        since=since,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    start: Union[Unset, int] = UNSET,
    end: Union[Unset, int] = UNSET,
    since: Union[Unset, str] = UNSET,
) -> Optional[LabelsResponseBody]:
    """
    Args:
        start (Union[Unset, int]):
        end (Union[Unset, int]):
        since (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        LabelsResponseBody
    """

    return sync_detailed(
        client=client,
        start=start,
        end=end,
        since=since,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    start: Union[Unset, int] = UNSET,
    end: Union[Unset, int] = UNSET,
    since: Union[Unset, str] = UNSET,
) -> Response[LabelsResponseBody]:
    """
    Args:
        start (Union[Unset, int]):
        end (Union[Unset, int]):
        since (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[LabelsResponseBody]
    """

    kwargs = _get_kwargs(
        start=start,
        end=end,
        since=since,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    start: Union[Unset, int] = UNSET,
    end: Union[Unset, int] = UNSET,
    since: Union[Unset, str] = UNSET,
) -> Optional[LabelsResponseBody]:
    """
    Args:
        start (Union[Unset, int]):
        end (Union[Unset, int]):
        since (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        LabelsResponseBody
    """

    return (
        await asyncio_detailed(
            client=client,
            start=start,
            end=end,
            since=since,
        )
    ).parsed
