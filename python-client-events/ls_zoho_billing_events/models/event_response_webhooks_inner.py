# coding: utf-8

"""
    Events

    Events can be used to let you know when something happens in your organization. Every happening in your organization will be recorded as a new Event. For example, when a new payment is received, we will create a <code>payment_thankyou</code> event; when a subscription is created, we will create a <code>subscription_created</code> event.<br/> <br/>You can retrieve these events individually or as a <a href=\"https://www.zoho.com/billing/api/v1/events/#list-of-events\">list</a> using our API. If you want to update the data on your server when an event occurs, you can use webhooks to send these event objects directly to an endpoint on your application’s server. Learn more about <a href=\"https://www.zoho.com/billing/help/settings/automation.html\">webhooks</a>.<br/><br/>

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

class EventResponseWebhooksInner(BaseModel):
    """
    EventResponseWebhooksInner
    """ # noqa: E501
    webhook_id: Optional[StrictStr] = Field(default=None, description="The unique ID generated for a webhook by the server. This can be used as an identifier.")
    url: Optional[StrictStr] = Field(default=None, description="The URL for which the webhook is sent.")
    status: Optional[StrictStr] = Field(default=None, description="Status of the webhook. This can be <code>success</code>, <code>scheduled</code> or <code>failure</code>.")
    last_updated_time: Optional[StrictStr] = Field(default=None, description="The time at which the webhook was last sent.")
    __properties: ClassVar[List[str]] = ["webhook_id", "url", "status", "last_updated_time"]

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
        """Create an instance of EventResponseWebhooksInner from a JSON string"""
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
        """Create an instance of EventResponseWebhooksInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "webhook_id": obj.get("webhook_id"),
            "url": obj.get("url"),
            "status": obj.get("status"),
            "last_updated_time": obj.get("last_updated_time")
        })
        return _obj


