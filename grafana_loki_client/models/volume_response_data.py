from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.volume_response_data_result_type import VolumeResponseDataResultType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.volume_response_result import VolumeResponseResult


T = TypeVar("T", bound="VolumeResponseData")


@_attrs_define
class VolumeResponseData:
    """
    Attributes:
        result_type (Union[Unset, VolumeResponseDataResultType]):
        result (Union[Unset, List['VolumeResponseResult']]):
    """

    result_type: Union[Unset, VolumeResponseDataResultType] = UNSET
    result: Union[Unset, List["VolumeResponseResult"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        result_type: Union[Unset, str] = UNSET
        if not isinstance(self.result_type, Unset):
            result_type = self.result_type.value

        result: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.result, Unset):
            result = []
            for result_item_data in self.result:
                result_item = result_item_data.to_dict()
                result.append(result_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if result_type is not UNSET:
            field_dict["resultType"] = result_type
        if result is not UNSET:
            field_dict["result"] = result

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.volume_response_result import VolumeResponseResult

        d = src_dict.copy()
        _result_type = d.pop("resultType", UNSET)
        result_type: Union[Unset, VolumeResponseDataResultType]
        if isinstance(_result_type, Unset):
            result_type = UNSET
        else:
            result_type = VolumeResponseDataResultType(_result_type)

        result = []
        _result = d.pop("result", UNSET)
        for result_item_data in _result or []:
            result_item = VolumeResponseResult.from_dict(result_item_data)

            result.append(result_item)

        volume_response_data = cls(
            result_type=result_type,
            result=result,
        )

        volume_response_data.additional_properties = d
        return volume_response_data

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
