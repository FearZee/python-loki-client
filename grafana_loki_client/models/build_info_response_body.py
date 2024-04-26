import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="BuildInfoResponseBody")


@_attrs_define
class BuildInfoResponseBody:
    """
    Attributes:
        version (Union[Unset, str]):
        revision (Union[Unset, str]):
        branch (Union[Unset, str]):
        build_date (Union[Unset, datetime.datetime]):
        build_user (Union[Unset, str]):
        go_version (Union[Unset, str]):
    """

    version: Union[Unset, str] = UNSET
    revision: Union[Unset, str] = UNSET
    branch: Union[Unset, str] = UNSET
    build_date: Union[Unset, datetime.datetime] = UNSET
    build_user: Union[Unset, str] = UNSET
    go_version: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        version = self.version

        revision = self.revision

        branch = self.branch

        build_date: Union[Unset, str] = UNSET
        if not isinstance(self.build_date, Unset):
            build_date = self.build_date.isoformat()

        build_user = self.build_user

        go_version = self.go_version

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if version is not UNSET:
            field_dict["version"] = version
        if revision is not UNSET:
            field_dict["revision"] = revision
        if branch is not UNSET:
            field_dict["branch"] = branch
        if build_date is not UNSET:
            field_dict["buildDate"] = build_date
        if build_user is not UNSET:
            field_dict["buildUser"] = build_user
        if go_version is not UNSET:
            field_dict["goVersion"] = go_version

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        version = d.pop("version", UNSET)

        revision = d.pop("revision", UNSET)

        branch = d.pop("branch", UNSET)

        _build_date = d.pop("buildDate", UNSET)
        build_date: Union[Unset, datetime.datetime]
        if isinstance(_build_date, Unset):
            build_date = UNSET
        else:
            build_date = isoparse(_build_date)

        build_user = d.pop("buildUser", UNSET)

        go_version = d.pop("goVersion", UNSET)

        build_info_response_body = cls(
            version=version,
            revision=revision,
            branch=branch,
            build_date=build_date,
            build_user=build_user,
            go_version=go_version,
        )

        build_info_response_body.additional_properties = d
        return build_info_response_body

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
