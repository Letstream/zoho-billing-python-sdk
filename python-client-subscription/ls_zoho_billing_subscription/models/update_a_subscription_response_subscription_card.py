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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class UpdateASubscriptionResponseSubscriptionCard(BaseModel):
    """
    Customer's card object. This contains <code>payment_gateway</code>, <code>last_four_digits</code>, <code>expiry_month</code> and <code>expiry_year</code>.
    """ # noqa: E501
    card_id: Optional[Any] = Field(default=None, description="Customer's card ID.")
    last_four_digits: Optional[StrictInt] = Field(default=None, description="Last four digits of the customer's card.")
    payment_gateway: Optional[StrictStr] = Field(default=None, description="Payment gateway through which payment needs to be made. Supported payment gateway values <code>test_gateway</code>, <code>payflow_pro</code>, <code>stripe</code>, <code>2checkout</code>, <code>authorize_net</code>, <code>payments_pro</code>, <code>forte</code>, <code>worldpay</code>, <code>wepay</code>.")
    expiry_month: Optional[StrictInt] = Field(default=None, description="Expiry month of the customer's card.")
    expiry_year: Optional[StrictInt] = Field(default=None, description="Expiry year of the customer's card.")
    __properties: ClassVar[List[str]] = ["card_id", "last_four_digits", "payment_gateway", "expiry_month", "expiry_year"]

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
        """Create an instance of UpdateASubscriptionResponseSubscriptionCard from a JSON string"""
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
        # set to None if card_id (nullable) is None
        # and model_fields_set contains the field
        if self.card_id is None and "card_id" in self.model_fields_set:
            _dict['card_id'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of UpdateASubscriptionResponseSubscriptionCard from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "card_id": obj.get("card_id"),
            "last_four_digits": obj.get("last_four_digits"),
            "payment_gateway": obj.get("payment_gateway"),
            "expiry_month": obj.get("expiry_month"),
            "expiry_year": obj.get("expiry_year")
        })
        return _obj


