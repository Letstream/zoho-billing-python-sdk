# coding: utf-8

"""
    Credit-Notes

    Credit notes are created when a refund is to be made to a customer. A credit note object allows you to keep track of all credit note related information.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ls_zoho_billing_credit_notes.models.create_a_credit_note_request_creditnote_items_inner import CreateACreditNoteRequestCreditnoteItemsInner
from ls_zoho_billing_credit_notes.models.item_custom_fields_inner import ItemCustomFieldsInner
from typing import Optional, Set
from typing_extensions import Self

class CreateACreditNoteRequest(BaseModel):
    """
    CreateACreditNoteRequest
    """ # noqa: E501
    customer_id: StrictStr = Field(description="Customer ID of the customer for whom the credit note is raised.")
    contact_persons: Optional[List[StrictStr]] = Field(default=None, description="Contact Persons associated with the credit note.")
    var_date: StrictStr = Field(description="The date on which credit note is raised.", alias="date")
    exchange_rate: Optional[StrictStr] = Field(default=None, description="Exchange rate for the currency associated with the customer.")
    creditnote_items: List[CreateACreditNoteRequestCreditnoteItemsInner] = Field(description="List of items involved in the credit note. This contains <code>item_id</code>, <code>description</code>, <code>quantity</code>, <code>price</code> and <code>item_total</code>.")
    creditnote_number: StrictStr = Field(description="Unique number generated (starts with CN) which will be displayed in the interface and credit notes.")
    ignore_auto_number_generation: Optional[StrictBool] = Field(default=None, description="Set to true if you need to provide your own credit note number.")
    reference_number: Optional[StrictStr] = Field(default=None, description="Reference number generated for the payment. A string of your choice can also be used as the reference number.")
    custom_fields: Optional[List[ItemCustomFieldsInner]] = Field(default=None, description="Additional fields for the Credit-Notes.")
    notes: Optional[StrictStr] = Field(default=None, description="A short note for the credit note.")
    terms: Optional[StrictStr] = Field(default=None, description="Terms & condition to be displayed in the credit note.")
    template_id: Optional[StrictStr] = Field(default=None, description="Unique ID of the creditnote template")
    tax_treatment: Optional[StrictStr] = Field(default=None, description="VAT treatment for the invoice .Choose whether the contact falls under: </br><code>home_country_mexico</code>,<code>border_region_mexico</code>,<code>non_mexico</code> supported only for <b>MX</b>.")
    cfdi_usage: Optional[StrictStr] = Field(default=None, description="Choose CFDI Usage. Allowed values:</br><code>acquisition_of_merchandise</code>, <code>return_discount_bonus</code>, <code>general_expense</code>, <code>buildings</code>, <code>furniture_office_equipment</code>, <code>transport_equipment</code>, <code>computer_equipmentdye_molds_tools</code>, <code>telephone_communication</code>, <code>satellite_communication</code>, <code>other_machinery_equipment</code>, <code>hospital_expense</code>, <code>medical_expense_disability</code>, <code>funeral_expense</code>, <code>donation</code>, <code>interest_mortage_loans</code>, <code>contribution_sar</code>, <code>medical_expense_insurance_pormium</code>, <code>school_transportation_expense</code>, <code>deposit_saving_account</code>, <code>payment_educational_service</code>, <code>no_tax_effect</code>, <code>payment</code>, <code>payroll</code>.")
    cfdi_reference_type: Optional[StrictStr] = Field(default=None, description="Choose CFDI Reference Type. Allowed values:</br><code>return_of_merchandise</code>, <code>substitution_previous_cfdi</code>, <code>transfer_of_goods</code>, <code>invoice_generated_from_order</code>, <code>cfdi_for_advance</code>.")
    __properties: ClassVar[List[str]] = ["customer_id", "contact_persons", "date", "exchange_rate", "creditnote_items", "creditnote_number", "ignore_auto_number_generation", "reference_number", "custom_fields", "notes", "terms", "template_id", "tax_treatment", "cfdi_usage", "cfdi_reference_type"]

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
        """Create an instance of CreateACreditNoteRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in creditnote_items (list)
        _items = []
        if self.creditnote_items:
            for _item_creditnote_items in self.creditnote_items:
                if _item_creditnote_items:
                    _items.append(_item_creditnote_items.to_dict())
            _dict['creditnote_items'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in custom_fields (list)
        _items = []
        if self.custom_fields:
            for _item_custom_fields in self.custom_fields:
                if _item_custom_fields:
                    _items.append(_item_custom_fields.to_dict())
            _dict['custom_fields'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CreateACreditNoteRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "customer_id": obj.get("customer_id"),
            "contact_persons": obj.get("contact_persons"),
            "date": obj.get("date"),
            "exchange_rate": obj.get("exchange_rate"),
            "creditnote_items": [CreateACreditNoteRequestCreditnoteItemsInner.from_dict(_item) for _item in obj["creditnote_items"]] if obj.get("creditnote_items") is not None else None,
            "creditnote_number": obj.get("creditnote_number"),
            "ignore_auto_number_generation": obj.get("ignore_auto_number_generation"),
            "reference_number": obj.get("reference_number"),
            "custom_fields": [ItemCustomFieldsInner.from_dict(_item) for _item in obj["custom_fields"]] if obj.get("custom_fields") is not None else None,
            "notes": obj.get("notes"),
            "terms": obj.get("terms"),
            "template_id": obj.get("template_id"),
            "tax_treatment": obj.get("tax_treatment"),
            "cfdi_usage": obj.get("cfdi_usage"),
            "cfdi_reference_type": obj.get("cfdi_reference_type")
        })
        return _obj


