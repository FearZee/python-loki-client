from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.query_range_response_data_result_type import (
    QueryRangeResponseDataResultType,
)

if TYPE_CHECKING:
    from ..models.query_range_response_result import QueryRangeResponseResult
    from ..models.query_statistics import QueryStatistics


T = TypeVar("T", bound="QueryRangeResponseData")


@_attrs_define
class QueryRangeResponseData:
    """
    Attributes:
        result_type (QueryRangeResponseDataResultType): Indicates the type of result. Can be 'vector' or 'streams'.
        result (List['QueryRangeResponseResult']):
        stats (QueryStatistics):
    """

    result_type: QueryRangeResponseDataResultType
    result: List["QueryRangeResponseResult"]
    stats: "QueryStatistics"
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        result_type = self.result_type.value

        result = []
        for result_item_data in self.result:
            result_item = result_item_data.to_dict()
            result.append(result_item)

        stats = self.stats.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "resultType": result_type,
                "result": result,
                "stats": stats,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.query_range_response_result import QueryRangeResponseResult
        from ..models.query_statistics import QueryStatistics

        d = src_dict.copy()
        result_type = QueryRangeResponseDataResultType(d.pop("resultType"))

        result = []
        _result = d.pop("result")
        for result_item_data in _result:
            result_item = QueryRangeResponseResult.from_dict(result_item_data)

            result.append(result_item)

        stats = QueryStatistics.from_dict(d.pop("stats"))

        query_range_response_data = cls(
            result_type=result_type,
            result=result,
            stats=stats,
        )

        query_range_response_data.additional_properties = d
        return query_range_response_data

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
