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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ls_zoho_billing_addons.models.addon_response_custom_fields_inner import AddonResponseCustomFieldsInner
from ls_zoho_billing_addons.models.addon_response_plans_inner import AddonResponsePlansInner
from ls_zoho_billing_addons.models.addon_response_price_brackets_inner import AddonResponsePriceBracketsInner
from ls_zoho_billing_addons.models.addon_response_tags_inner import AddonResponseTagsInner
from ls_zoho_billing_addons.models.item_tax_preferences_inner import ItemTaxPreferencesInner
from typing import Optional, Set
from typing_extensions import Self

class RetrieveAnAddonResponseAddon(BaseModel):
    """
    RetrieveAnAddonResponseAddon
    """ # noqa: E501
    addon_code: Optional[StrictStr] = Field(default=None, description="Unique string of your choice which lets you identify this addon.")
    name: Optional[StrictStr] = Field(default=None, description="Name of your choice to be displayed in the interface and invoices.")
    unit: Optional[StrictStr] = Field(default=None, description="A name of your choice to refer to one unit of the addon.")
    unit_name: Optional[StrictStr] = Field(default=None, description="A name of your choice to refer to one unit of the addon.")
    pricing_scheme: Optional[StrictStr] = Field(default='unit', description="Pricing type of the addon can be changed and the values are <code>unit</code>, <code>volume</code>, <code>tier</code> or <code>package</code>. To know more about pricing schemes click <a href=\"/billing/help/product-catalog/subscription-items/addons.html#pricing-schemes\">here.</a>")
    price_brackets: Optional[List[AddonResponsePriceBracketsInner]] = Field(default=None, description="Array of objects which contains the start quantity, end quantity and price")
    type: Optional[StrictStr] = Field(default='recurring', description="Indicates type of the addon. This could be either <code>recurring</code> or <code>one_time</code>.")
    interval_unit: Optional[StrictStr] = Field(default='monthly', description="The billing frequency of the addon only if type is recurring and the values can be <code>monthly</code> or <code>yearly</code>.")
    tags: Optional[List[AddonResponseTagsInner]] = None
    custom_fields: Optional[List[AddonResponseCustomFieldsInner]] = Field(default=None, description="Custom fields for a Addon.")
    applicable_to_all_plans: Optional[StrictBool] = Field(default=True, description="If the addon is to be associated with all plans, applicable_to_all_plans is set to <code>true</code>; otherwise, it is set to <code>false</code>.")
    plans: Optional[List[AddonResponsePlansInner]] = Field(default=None, description="List of plans that the addon needs to be associated with. If an addon is to be associated with only two plans - \"basic\" and \"professional\", then <code>applicable_to_all_plans</code> is set to false. Only the plan codes of the plans that need to be associated with are required.")
    status: Optional[StrictStr] = Field(default=None, description="Status of the addon. It can either be <code>active</code> or <code>inactive</code>.")
    product_id: Optional[StrictStr] = Field(default=None, description="Product ID to which you want to associate this addon with.")
    description: Optional[StrictStr] = Field(default=None, description="Short description regarding the addon.")
    store_markup_description: Optional[StrictStr] = Field(default=None, description="Long Description regarding the plan.")
    product_type: Optional[StrictStr] = Field(default=None, description="Product type for UK Edition.")
    hsn_or_sac: Optional[StrictStr] = Field(default=None, description="HSN or SAC code for Goods/Services addon")
    sat_item_key_code: Optional[StrictStr] = Field(default=None, description="Add SAT Item Key Code for your goods/services. Download the <a href= http://omawww.sat.gob.mx/tramitesyservicios/Paginas/documentos/catCFDI_V_4_07122022.xls  >CFDI Catalogs.</a>")
    unitkey_code: Optional[StrictStr] = Field(default=None, description="Add Unit Key Code for your goods/services. Download the <a href= http://omawww.sat.gob.mx/tramitesyservicios/Paginas/documentos/catCFDI_V_4_07122022.xls  >CFDI Catalogs.</a>")
    item_tax_preferences: Optional[List[ItemTaxPreferencesInner]] = Field(default=None, description="Tax preferenece for addon")
    tax_id: Optional[StrictStr] = Field(default='no tax will be associated', description="Tax ID to which you would like to associate with this addon.")
    created_time: Optional[StrictStr] = Field(default=None, description="Time at which the addon was created.")
    updated_time: Optional[StrictStr] = Field(default=None, description="Time at which the addon details were last updated.")
    __properties: ClassVar[List[str]] = ["addon_code", "name", "unit", "unit_name", "pricing_scheme", "price_brackets", "type", "interval_unit", "tags", "custom_fields", "applicable_to_all_plans", "plans", "status", "product_id", "description", "store_markup_description", "product_type", "hsn_or_sac", "sat_item_key_code", "unitkey_code", "item_tax_preferences", "tax_id", "created_time", "updated_time"]

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
        """Create an instance of RetrieveAnAddonResponseAddon from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in price_brackets (list)
        _items = []
        if self.price_brackets:
            for _item_price_brackets in self.price_brackets:
                if _item_price_brackets:
                    _items.append(_item_price_brackets.to_dict())
            _dict['price_brackets'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in tags (list)
        _items = []
        if self.tags:
            for _item_tags in self.tags:
                if _item_tags:
                    _items.append(_item_tags.to_dict())
            _dict['tags'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in custom_fields (list)
        _items = []
        if self.custom_fields:
            for _item_custom_fields in self.custom_fields:
                if _item_custom_fields:
                    _items.append(_item_custom_fields.to_dict())
            _dict['custom_fields'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in plans (list)
        _items = []
        if self.plans:
            for _item_plans in self.plans:
                if _item_plans:
                    _items.append(_item_plans.to_dict())
            _dict['plans'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in item_tax_preferences (list)
        _items = []
        if self.item_tax_preferences:
            for _item_item_tax_preferences in self.item_tax_preferences:
                if _item_item_tax_preferences:
                    _items.append(_item_item_tax_preferences.to_dict())
            _dict['item_tax_preferences'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of RetrieveAnAddonResponseAddon from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "addon_code": obj.get("addon_code"),
            "name": obj.get("name"),
            "unit": obj.get("unit"),
            "unit_name": obj.get("unit_name"),
            "pricing_scheme": obj.get("pricing_scheme") if obj.get("pricing_scheme") is not None else 'unit',
            "price_brackets": [AddonResponsePriceBracketsInner.from_dict(_item) for _item in obj["price_brackets"]] if obj.get("price_brackets") is not None else None,
            "type": obj.get("type") if obj.get("type") is not None else 'recurring',
            "interval_unit": obj.get("interval_unit") if obj.get("interval_unit") is not None else 'monthly',
            "tags": [AddonResponseTagsInner.from_dict(_item) for _item in obj["tags"]] if obj.get("tags") is not None else None,
            "custom_fields": [AddonResponseCustomFieldsInner.from_dict(_item) for _item in obj["custom_fields"]] if obj.get("custom_fields") is not None else None,
            "applicable_to_all_plans": obj.get("applicable_to_all_plans") if obj.get("applicable_to_all_plans") is not None else True,
            "plans": [AddonResponsePlansInner.from_dict(_item) for _item in obj["plans"]] if obj.get("plans") is not None else None,
            "status": obj.get("status"),
            "product_id": obj.get("product_id"),
            "description": obj.get("description"),
            "store_markup_description": obj.get("store_markup_description"),
            "product_type": obj.get("product_type"),
            "hsn_or_sac": obj.get("hsn_or_sac"),
            "sat_item_key_code": obj.get("sat_item_key_code"),
            "unitkey_code": obj.get("unitkey_code"),
            "item_tax_preferences": [ItemTaxPreferencesInner.from_dict(_item) for _item in obj["item_tax_preferences"]] if obj.get("item_tax_preferences") is not None else None,
            "tax_id": obj.get("tax_id") if obj.get("tax_id") is not None else 'no tax will be associated',
            "created_time": obj.get("created_time"),
            "updated_time": obj.get("updated_time")
        })
        return _obj


