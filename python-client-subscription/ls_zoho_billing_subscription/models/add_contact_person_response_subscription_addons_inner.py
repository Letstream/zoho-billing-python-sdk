# coding: utf-8

"""
    Subscriptions

    A subscription enables you to charge customers at specified intervals for a plan of their choice.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set
from typing_extensions import Self

class AddContactPersonResponseSubscriptionAddonsInner(BaseModel):
    """
    AddContactPersonResponseSubscriptionAddonsInner
    """ # noqa: E501
    addon_code: Optional[StrictStr] = Field(default=None, description="Addon code of the addon.")
    name: Optional[Any] = Field(default=None, description="Name of the addon.")
    addon_description: Optional[StrictStr] = Field(default=None, description="Description of the addon exclusive to this subscription. This will be displayed in place of the addon name in invoices generated for this subscription.")
    quantity: Optional[StrictInt] = Field(default=None, description="Required quantity of the chosen addon.")
    price: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="A value can be provided here if the per unit addon price has to be overridden for this subscription.")
    discount: Optional[Any] = Field(default=None, description="Discount applied for the addon.")
    total: Optional[Any] = Field(default=None, description="Total amount for the addon.")
    tax_id: Optional[Any] = Field(default=None, description="Unique ID of the tax applied for the addon.")
    __properties: ClassVar[List[str]] = ["addon_code", "name", "addon_description", "quantity", "price", "discount", "total", "tax_id"]

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
        """Create an instance of AddContactPersonResponseSubscriptionAddonsInner from a JSON string"""
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
        # set to None if name (nullable) is None
        # and model_fields_set contains the field
        if self.name is None and "name" in self.model_fields_set:
            _dict['name'] = None

        # set to None if discount (nullable) is None
        # and model_fields_set contains the field
        if self.discount is None and "discount" in self.model_fields_set:
            _dict['discount'] = None

        # set to None if total (nullable) is None
        # and model_fields_set contains the field
        if self.total is None and "total" in self.model_fields_set:
            _dict['total'] = None

        # set to None if tax_id (nullable) is None
        # and model_fields_set contains the field
        if self.tax_id is None and "tax_id" in self.model_fields_set:
            _dict['tax_id'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AddContactPersonResponseSubscriptionAddonsInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "addon_code": obj.get("addon_code"),
            "name": obj.get("name"),
            "addon_description": obj.get("addon_description"),
            "quantity": obj.get("quantity"),
            "price": obj.get("price"),
            "discount": obj.get("discount"),
            "total": obj.get("total"),
            "tax_id": obj.get("tax_id")
        })
        return _obj


