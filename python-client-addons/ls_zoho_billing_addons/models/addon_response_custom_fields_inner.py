# coding: utf-8

"""
    Addons

    An addon contains additional features that are not part of the subscribed plan, but are made available to customers on purchase of the addon. There are two kinds of addons - one-time and recurring. For a one-time addon, customers pay only once at the time of subscription, whereas for a recurring addon, customers have to pay for the addon each time they pay for the plan’s subscription. An addon can be associated with one or more plans of a product.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class AddonResponseCustomFieldsInner(BaseModel):
    """
    AddonResponseCustomFieldsInner
    """ # noqa: E501
    customfield_id: Optional[StrictStr] = None
    is_active: Optional[StrictStr] = None
    show_in_all_pdf: Optional[StrictStr] = None
    value_formatted: Optional[StrictStr] = None
    data_type: Optional[StrictStr] = None
    index: Optional[StrictInt] = None
    label: Optional[StrictStr] = Field(default=None, description="Label of the Custom Field")
    show_on_pdf: Optional[StrictStr] = None
    placeholder: Optional[StrictStr] = None
    value: Optional[StrictStr] = Field(default=None, description="Value of the Custom Field")
    __properties: ClassVar[List[str]] = ["customfield_id", "is_active", "show_in_all_pdf", "value_formatted", "data_type", "index", "label", "show_on_pdf", "placeholder", "value"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of AddonResponseCustomFieldsInner from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AddonResponseCustomFieldsInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "customfield_id": obj.get("customfield_id"),
            "is_active": obj.get("is_active"),
            "show_in_all_pdf": obj.get("show_in_all_pdf"),
            "value_formatted": obj.get("value_formatted"),
            "data_type": obj.get("data_type"),
            "index": obj.get("index"),
            "label": obj.get("label"),
            "show_on_pdf": obj.get("show_on_pdf"),
            "placeholder": obj.get("placeholder"),
            "value": obj.get("value")
        })
        return _obj


