from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.volume_response_result_metric import VolumeResponseResultMetric


T = TypeVar("T", bound="VolumeResponseResult")


@_attrs_define
class VolumeResponseResult:
    """
    Attributes:
        metric (Union[Unset, VolumeResponseResultMetric]):
        values (Union[Unset, List[List[str]]]):
    """

    metric: Union[Unset, "VolumeResponseResultMetric"] = UNSET
    values: Union[Unset, List[List[str]]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        metric: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.metric, Unset):
            metric = self.metric.to_dict()

        values: Union[Unset, List[List[str]]] = UNSET
        if not isinstance(self.values, Unset):
            values = []
            for values_item_data in self.values:
                values_item = values_item_data

                values.append(values_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if metric is not UNSET:
            field_dict["metric"] = metric
        if values is not UNSET:
            field_dict["values"] = values

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.volume_response_result_metric import VolumeResponseResultMetric

        d = src_dict.copy()
        _metric = d.pop("metric", UNSET)
        metric: Union[Unset, VolumeResponseResultMetric]
        if isinstance(_metric, Unset):
            metric = UNSET
        else:
            metric = VolumeResponseResultMetric.from_dict(_metric)

        values = []
        _values = d.pop("values", UNSET)
        for values_item_data in _values or []:
            values_item = cast(List[str], values_item_data)

            values.append(values_item)

        volume_response_result = cls(
            metric=metric,
            values=values,
        )

        volume_response_result.additional_properties = d
        return volume_response_result

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
