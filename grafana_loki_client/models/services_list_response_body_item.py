from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.service_state_enum import ServiceStateEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="ServicesListResponseBodyItem")


@_attrs_define
class ServicesListResponseBodyItem:
    """
    Attributes:
        service_name (Union[Unset, str]): The name of the service.
        state (Union[Unset, ServiceStateEnum]):
    """

    service_name: Union[Unset, str] = UNSET
    state: Union[Unset, ServiceStateEnum] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        service_name = self.service_name

        state: Union[Unset, str] = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if service_name is not UNSET:
            field_dict["service_name"] = service_name
        if state is not UNSET:
            field_dict["state"] = state

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        service_name = d.pop("service_name", UNSET)

        _state = d.pop("state", UNSET)
        state: Union[Unset, ServiceStateEnum]
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = ServiceStateEnum(_state)

        services_list_response_body_item = cls(
            service_name=service_name,
            state=state,
        )

        services_list_response_body_item.additional_properties = d
        return services_list_response_body_item

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
