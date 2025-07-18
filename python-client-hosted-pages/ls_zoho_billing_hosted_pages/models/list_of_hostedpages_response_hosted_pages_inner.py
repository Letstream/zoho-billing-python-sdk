# coding: utf-8

"""
    Hosted-Pages

    Zoho Billing provides a hosted payment page to integrate with your websites. You can securely integrate with Zoho Billing for collecting your customer's sensitive card information through the hosted page. These Hosted Pages will expire within one hour.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class ListOfHostedpagesResponseHostedPagesInner(BaseModel):
    """
    ListOfHostedpagesResponseHostedPagesInner
    """ # noqa: E501
    hostedpage_id: Optional[StrictStr] = Field(default=None, description="Unique ID generated by the server. This is used to identify the generated hosted page.")
    status: Optional[StrictStr] = Field(default=None, description="Status of the hosted page generated. This can be <code>fresh</code>, <code>read</code>, <code>success</code>, <code>failed</code>, <code>cancelled</code> or <code>force_cancelled</code>.")
    url: Optional[StrictStr] = Field(default=None, description="The URL of the hosted page generated.")
    action: Optional[StrictStr] = Field(default=None, description="Action that needs to be performed using the hosted page. This can be <code>new_subscription</code>, <code>update_subscription</code>, <code>update_card</code> or <code>one_time_addon</code>.")
    expiring_time: Optional[StrictStr] = Field(default=None, description="The time at which the hosted page will expire.")
    created_time: Optional[StrictStr] = Field(default=None, description="The time at which the hosted page was created.")
    __properties: ClassVar[List[str]] = ["hostedpage_id", "status", "url", "action", "expiring_time", "created_time"]

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
        """Create an instance of ListOfHostedpagesResponseHostedPagesInner from a JSON string"""
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
        """Create an instance of ListOfHostedpagesResponseHostedPagesInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "hostedpage_id": obj.get("hostedpage_id"),
            "status": obj.get("status"),
            "url": obj.get("url"),
            "action": obj.get("action"),
            "expiring_time": obj.get("expiring_time"),
            "created_time": obj.get("created_time")
        })
        return _obj


