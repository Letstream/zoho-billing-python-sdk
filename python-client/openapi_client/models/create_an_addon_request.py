# coding: utf-8

"""
    Addons

    An addon contains additional features that are not part of the subscribed plan, but are made available to customers on purchase of the addon. There are two kinds of addons - one-time and recurring. For a one-time addon, customers pay only once at the time of subscription, whereas for a recurring addon, customers have to pay for the addon each time they pay for the plan’s subscription. An addon can be associated with one or more plans of a product.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
import pprint
from pydantic import BaseModel, ConfigDict, Field, StrictStr, ValidationError, field_validator
from typing import Any, List, Optional
from openapi_client.models.create_an_addon_request_one_of import CreateAnAddonRequestOneOf
from openapi_client.models.create_an_addon_request_one_of1 import CreateAnAddonRequestOneOf1
from openapi_client.models.create_an_addon_request_one_of2 import CreateAnAddonRequestOneOf2
from openapi_client.models.create_an_addon_request_one_of3 import CreateAnAddonRequestOneOf3
from pydantic import StrictStr, Field
from typing import Union, List, Set, Optional, Dict
from typing_extensions import Literal, Self

CREATEANADDONREQUEST_ONE_OF_SCHEMAS = ["CreateAnAddonRequestOneOf", "CreateAnAddonRequestOneOf1", "CreateAnAddonRequestOneOf2", "CreateAnAddonRequestOneOf3"]

class CreateAnAddonRequest(BaseModel):
    """
    CreateAnAddonRequest
    """
    # data type: CreateAnAddonRequestOneOf
    oneof_schema_1_validator: Optional[CreateAnAddonRequestOneOf] = None
    # data type: CreateAnAddonRequestOneOf1
    oneof_schema_2_validator: Optional[CreateAnAddonRequestOneOf1] = None
    # data type: CreateAnAddonRequestOneOf2
    oneof_schema_3_validator: Optional[CreateAnAddonRequestOneOf2] = None
    # data type: CreateAnAddonRequestOneOf3
    oneof_schema_4_validator: Optional[CreateAnAddonRequestOneOf3] = None
    actual_instance: Optional[Union[CreateAnAddonRequestOneOf, CreateAnAddonRequestOneOf1, CreateAnAddonRequestOneOf2, CreateAnAddonRequestOneOf3]] = None
    one_of_schemas: Set[str] = { "CreateAnAddonRequestOneOf", "CreateAnAddonRequestOneOf1", "CreateAnAddonRequestOneOf2", "CreateAnAddonRequestOneOf3" }

    model_config = ConfigDict(
        validate_assignment=True,
        protected_namespaces=(),
    )


    def __init__(self, *args, **kwargs) -> None:
        if args:
            if len(args) > 1:
                raise ValueError("If a position argument is used, only 1 is allowed to set `actual_instance`")
            if kwargs:
                raise ValueError("If a position argument is used, keyword arguments cannot be used.")
            super().__init__(actual_instance=args[0])
        else:
            super().__init__(**kwargs)

    @field_validator('actual_instance')
    def actual_instance_must_validate_oneof(cls, v):
        instance = CreateAnAddonRequest.model_construct()
        error_messages = []
        match = 0
        # validate data type: CreateAnAddonRequestOneOf
        if not isinstance(v, CreateAnAddonRequestOneOf):
            error_messages.append(f"Error! Input type `{type(v)}` is not `CreateAnAddonRequestOneOf`")
        else:
            match += 1
        # validate data type: CreateAnAddonRequestOneOf1
        if not isinstance(v, CreateAnAddonRequestOneOf1):
            error_messages.append(f"Error! Input type `{type(v)}` is not `CreateAnAddonRequestOneOf1`")
        else:
            match += 1
        # validate data type: CreateAnAddonRequestOneOf2
        if not isinstance(v, CreateAnAddonRequestOneOf2):
            error_messages.append(f"Error! Input type `{type(v)}` is not `CreateAnAddonRequestOneOf2`")
        else:
            match += 1
        # validate data type: CreateAnAddonRequestOneOf3
        if not isinstance(v, CreateAnAddonRequestOneOf3):
            error_messages.append(f"Error! Input type `{type(v)}` is not `CreateAnAddonRequestOneOf3`")
        else:
            match += 1
        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when setting `actual_instance` in CreateAnAddonRequest with oneOf schemas: CreateAnAddonRequestOneOf, CreateAnAddonRequestOneOf1, CreateAnAddonRequestOneOf2, CreateAnAddonRequestOneOf3. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when setting `actual_instance` in CreateAnAddonRequest with oneOf schemas: CreateAnAddonRequestOneOf, CreateAnAddonRequestOneOf1, CreateAnAddonRequestOneOf2, CreateAnAddonRequestOneOf3. Details: " + ", ".join(error_messages))
        else:
            return v

    @classmethod
    def from_dict(cls, obj: Union[str, Dict[str, Any]]) -> Self:
        return cls.from_json(json.dumps(obj))

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Returns the object represented by the json string"""
        instance = cls.model_construct()
        error_messages = []
        match = 0

        # deserialize data into CreateAnAddonRequestOneOf
        try:
            instance.actual_instance = CreateAnAddonRequestOneOf.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into CreateAnAddonRequestOneOf1
        try:
            instance.actual_instance = CreateAnAddonRequestOneOf1.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into CreateAnAddonRequestOneOf2
        try:
            instance.actual_instance = CreateAnAddonRequestOneOf2.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into CreateAnAddonRequestOneOf3
        try:
            instance.actual_instance = CreateAnAddonRequestOneOf3.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))

        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into CreateAnAddonRequest with oneOf schemas: CreateAnAddonRequestOneOf, CreateAnAddonRequestOneOf1, CreateAnAddonRequestOneOf2, CreateAnAddonRequestOneOf3. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when deserializing the JSON string into CreateAnAddonRequest with oneOf schemas: CreateAnAddonRequestOneOf, CreateAnAddonRequestOneOf1, CreateAnAddonRequestOneOf2, CreateAnAddonRequestOneOf3. Details: " + ", ".join(error_messages))
        else:
            return instance

    def to_json(self) -> str:
        """Returns the JSON representation of the actual instance"""
        if self.actual_instance is None:
            return "null"

        if hasattr(self.actual_instance, "to_json") and callable(self.actual_instance.to_json):
            return self.actual_instance.to_json()
        else:
            return json.dumps(self.actual_instance)

    def to_dict(self) -> Optional[Union[Dict[str, Any], CreateAnAddonRequestOneOf, CreateAnAddonRequestOneOf1, CreateAnAddonRequestOneOf2, CreateAnAddonRequestOneOf3]]:
        """Returns the dict representation of the actual instance"""
        if self.actual_instance is None:
            return None

        if hasattr(self.actual_instance, "to_dict") and callable(self.actual_instance.to_dict):
            return self.actual_instance.to_dict()
        else:
            # primitive type
            return self.actual_instance

    def to_str(self) -> str:
        """Returns the string representation of the actual instance"""
        return pprint.pformat(self.model_dump())


