from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.volume_response_data import VolumeResponseData


T = TypeVar("T", bound="VolumeResponse")


@_attrs_define
class VolumeResponse:
    """
    Attributes:
        status (Union[Unset, str]):  Example: success.
        data (Union[Unset, VolumeResponseData]):
    """

    status: Union[Unset, str] = UNSET
    data: Union[Unset, "VolumeResponseData"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        status = self.status

        data: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.data, Unset):
            data = self.data.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if status is not UNSET:
            field_dict["status"] = status
        if data is not UNSET:
            field_dict["data"] = data

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.volume_response_data import VolumeResponseData

        d = src_dict.copy()
        status = d.pop("status", UNSET)

        _data = d.pop("data", UNSET)
        data: Union[Unset, VolumeResponseData]
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = VolumeResponseData.from_dict(_data)

        volume_response = cls(
            status=status,
            data=data,
        )

        volume_response.additional_properties = d
        return volume_response

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
