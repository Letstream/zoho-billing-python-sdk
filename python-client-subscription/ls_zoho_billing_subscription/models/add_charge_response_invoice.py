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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from ls_zoho_billing_subscription.models.add_charge_response_invoice_comments_inner import AddChargeResponseInvoiceCommentsInner
from ls_zoho_billing_subscription.models.add_charge_response_invoice_invoice_items_inner import AddChargeResponseInvoiceInvoiceItemsInner
from ls_zoho_billing_subscription.models.billing_address import BillingAddress
from ls_zoho_billing_subscription.models.buy_one_time_addon_response_invoice_payments_inner import BuyOneTimeAddonResponseInvoicePaymentsInner
from typing import Optional, Set
from typing_extensions import Self

class AddChargeResponseInvoice(BaseModel):
    """
    AddChargeResponseInvoice
    """ # noqa: E501
    invoice_id: Optional[StrictStr] = Field(default=None, description="Unique ID generated for an invoice.")
    number: Optional[StrictStr] = Field(default=None, description="Unique number generated for the invoice.")
    status: Optional[StrictStr] = Field(default=None, description="The status of the subscription. It can be <code>live</code>, <code>trial</code>, <code>dunning</code>, <code>unpaid</code>, <code>non_renewing</code>, <code>cancelled</code>, <code>creation_failed</code>, <code>cancelled_from_dunning</code>, <code>expired</code>, <code>trial_expired</code> or <code>future</code>.")
    invoice_items: Optional[List[AddChargeResponseInvoiceInvoiceItemsInner]] = Field(default=None, description="The list of items which are all included in the invoice. Each item object will have <code>item_id</code>, <code>name</code>, <code>code</code>, <code>price</code>, <code>quantity</code> and <code>item_total</code>.")
    invoice_date: Optional[StrictStr] = Field(default=None, description="Date in which the invoice was generated.")
    due_date: Optional[StrictStr] = Field(default=None, description="Date on which the payment is due for the invoice.")
    payment_expected_date: Optional[StrictStr] = Field(default=None, description="A date to specify the expected payment date.")
    ach_payment_initiated: Optional[StrictBool] = Field(default=None, description="Set to true if ACH payment is initiated.")
    transaction_type: Optional[StrictStr] = Field(default=None, description="Small description about the type of transaction.")
    customer_id: Optional[StrictStr] = Field(default=None, description="Customer ID of the customer for whom a subscription needs to be created.")
    customer_name: Optional[StrictStr] = Field(default=None, description="Name of the customer.")
    email: Optional[StrictStr] = Field(default=None, description="Email address of the customer.")
    total: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Total amount for the plan.")
    payment_made: Optional[Any] = Field(default=None, description="Payments can be made in multiple instalments. payment_made refers to the amount paid for the invoice in the respective instalment.")
    balance: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The unpaid amount of an invoice.")
    credits_applied: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Credits applied for the invoice.")
    write_off_amount: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The unpaid amount of an invoice that is written off.")
    payments: Optional[List[BuyOneTimeAddonResponseInvoicePaymentsInner]] = Field(default=None, description="List of payment objects. Each object will contain <code>payment_id</code>, <code>payment_mode</code>, <code>invoice_payment_id</code>, <code>gateway_transaction_id</code>, <code>description</code>, <code>date</code>, <code>reference_number</code> and <code>amount</code>.")
    currency_code: Optional[StrictStr] = Field(default=None, description="Currency code of the currency in which the customer wants to pay. If <code>currency_code</code> is not specified here, the currency chosen in your Zoho Billing organization will be used for billing. <code>currency_id</code> and <code>currency_symbol</code> are set automatically in accordance to the currency_code.")
    currency_symbol: Optional[StrictStr] = Field(default=None, description="Symbol of the customer's currency.")
    created_time: Optional[StrictStr] = Field(default=None, description="Time at which the subscription was created.")
    updated_time: Optional[StrictStr] = Field(default=None, description="Time at which the subscription details were last updated.")
    billing_address: Optional[BillingAddress] = None
    comments: Optional[List[AddChargeResponseInvoiceCommentsInner]] = Field(default=None, description="Lists the comments added by the system or by user.")
    __properties: ClassVar[List[str]] = ["invoice_id", "number", "status", "invoice_items", "invoice_date", "due_date", "payment_expected_date", "ach_payment_initiated", "transaction_type", "customer_id", "customer_name", "email", "total", "payment_made", "balance", "credits_applied", "write_off_amount", "payments", "currency_code", "currency_symbol", "created_time", "updated_time", "billing_address", "comments"]

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
        """Create an instance of AddChargeResponseInvoice from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in invoice_items (list)
        _items = []
        if self.invoice_items:
            for _item_invoice_items in self.invoice_items:
                if _item_invoice_items:
                    _items.append(_item_invoice_items.to_dict())
            _dict['invoice_items'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in payments (list)
        _items = []
        if self.payments:
            for _item_payments in self.payments:
                if _item_payments:
                    _items.append(_item_payments.to_dict())
            _dict['payments'] = _items
        # override the default output from pydantic by calling `to_dict()` of billing_address
        if self.billing_address:
            _dict['billing_address'] = self.billing_address.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in comments (list)
        _items = []
        if self.comments:
            for _item_comments in self.comments:
                if _item_comments:
                    _items.append(_item_comments.to_dict())
            _dict['comments'] = _items
        # set to None if payment_made (nullable) is None
        # and model_fields_set contains the field
        if self.payment_made is None and "payment_made" in self.model_fields_set:
            _dict['payment_made'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AddChargeResponseInvoice from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "invoice_id": obj.get("invoice_id"),
            "number": obj.get("number"),
            "status": obj.get("status"),
            "invoice_items": [AddChargeResponseInvoiceInvoiceItemsInner.from_dict(_item) for _item in obj["invoice_items"]] if obj.get("invoice_items") is not None else None,
            "invoice_date": obj.get("invoice_date"),
            "due_date": obj.get("due_date"),
            "payment_expected_date": obj.get("payment_expected_date"),
            "ach_payment_initiated": obj.get("ach_payment_initiated"),
            "transaction_type": obj.get("transaction_type"),
            "customer_id": obj.get("customer_id"),
            "customer_name": obj.get("customer_name"),
            "email": obj.get("email"),
            "total": obj.get("total"),
            "payment_made": obj.get("payment_made"),
            "balance": obj.get("balance"),
            "credits_applied": obj.get("credits_applied"),
            "write_off_amount": obj.get("write_off_amount"),
            "payments": [BuyOneTimeAddonResponseInvoicePaymentsInner.from_dict(_item) for _item in obj["payments"]] if obj.get("payments") is not None else None,
            "currency_code": obj.get("currency_code"),
            "currency_symbol": obj.get("currency_symbol"),
            "created_time": obj.get("created_time"),
            "updated_time": obj.get("updated_time"),
            "billing_address": BillingAddress.from_dict(obj["billing_address"]) if obj.get("billing_address") is not None else None,
            "comments": [AddChargeResponseInvoiceCommentsInner.from_dict(_item) for _item in obj["comments"]] if obj.get("comments") is not None else None
        })
        return _obj


