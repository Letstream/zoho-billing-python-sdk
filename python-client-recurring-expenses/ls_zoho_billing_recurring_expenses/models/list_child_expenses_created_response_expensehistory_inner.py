# coding: utf-8

"""
    Recurring Expenses

    Recurring expenses are those expenses that repeat itself after a fixed interval of time.<br><br><b>Possible error codes: </b><br><table><thead><tr><th>Error Code</th><th>Message</th></tr></thead><tbody><tr><td><span style=\"color:#FF0000;\"> 4027</span></td><td>Please select a valid date range</td></tr><tr><td><span style=\"color:#FF0000;\"> 5012</span></td><td>Recurrence Name already exists</td></tr><tr><td><span style=\"color:#FF0000;\"> 5015</span></td><td>Enter a valid expense amount</td></tr></tbody></table>

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

class ListChildExpensesCreatedResponseExpensehistoryInner(BaseModel):
    """
    ListChildExpensesCreatedResponseExpensehistoryInner
    """ # noqa: E501
    expense_id: Optional[StrictStr] = Field(default=None, description="Unoque ID of the expense")
    var_date: Optional[StrictStr] = Field(default=None, description="Date of expense creation", alias="date")
    account_name: Optional[StrictStr] = Field(default=None, description="For which Account the Expense is raised. <code>Maximum length [100]</code>")
    customer_name: Optional[StrictStr] = Field(default=None, description="Name of the Custome for which expense is raised. <code>Maximum length [100]</code>")
    total: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Total expense")
    status: Optional[StrictStr] = Field(default=None, description="Status of the recurring expense")
    vendor_name: Optional[StrictStr] = Field(default=None, description="Name of the seller")
    paid_through_account_name: Optional[StrictStr] = Field(default=None, description="Account from which payment was made")
    __properties: ClassVar[List[str]] = ["expense_id", "date", "account_name", "customer_name", "total", "status", "vendor_name", "paid_through_account_name"]

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
        """Create an instance of ListChildExpensesCreatedResponseExpensehistoryInner from a JSON string"""
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
        """Create an instance of ListChildExpensesCreatedResponseExpensehistoryInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "expense_id": obj.get("expense_id"),
            "date": obj.get("date"),
            "account_name": obj.get("account_name"),
            "customer_name": obj.get("customer_name"),
            "total": obj.get("total"),
            "status": obj.get("status"),
            "vendor_name": obj.get("vendor_name"),
            "paid_through_account_name": obj.get("paid_through_account_name")
        })
        return _obj


