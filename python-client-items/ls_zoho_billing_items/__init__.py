# coding: utf-8

# flake8: noqa

"""
    Items

    A product is the item offered for sale. It can be a commodity. Based on the type of your business, you can offer one or more goods.<br><br><b>Possible error codes: </b><br><table><thead><tr><th>Error Code</th><th>Message</th></tr></thead><tbody><tr><td><span style=\"color:#FF0000;\"> 1000</span></td><td>The item name already exist</td></tr><tr><tr><td><span style=\"color:#FF0000;\"> 2006</span></td><td>Item does not exist</td></tr><td><span style=\"color:#FF0000;\"> 2049</span></td><td>Items which are a part of other transactions cannot be deleted. Instead, mark them as inactive</td></tr><tr><td><span style=\"color:#FF0000;\"> 2076</span></td><td>Product type cannot be changed for Items having transactions</td></tr></tbody></table>

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


__version__ = "1.0.0"

# Define package exports
__all__ = [
    "ItemsApi",
    "ApiResponse",
    "ApiClient",
    "Configuration",
    "OpenApiException",
    "ApiTypeError",
    "ApiValueError",
    "ApiKeyError",
    "ApiAttributeError",
    "ApiException",
    "CreateAnItemRequest",
    "CreateAnItemResponse",
    "CustomFieldsInner",
    "DeleteAnItemResponse",
    "ItemResponse",
    "ItemTaxPreferencesInner",
    "ListItemsResponse",
    "ListItemsResponseItemsInner",
    "MarkAsActiveResponse",
    "MarkAsInactiveResponse",
    "RetrieveAnItemResponse",
    "UpdateAnItemRequest",
    "UpdateAnItemResponse",
    "UpdateAnItemResponseItem",
    "WarehousesInner",
]

# import apis into sdk package
from ls_zoho_billing_items.api.items_api import ItemsApi as ItemsApi

# import ApiClient
from ls_zoho_billing_items.api_response import ApiResponse as ApiResponse
from ls_zoho_billing_items.api_client import ApiClient as ApiClient
from ls_zoho_billing_items.configuration import Configuration as Configuration
from ls_zoho_billing_items.exceptions import OpenApiException as OpenApiException
from ls_zoho_billing_items.exceptions import ApiTypeError as ApiTypeError
from ls_zoho_billing_items.exceptions import ApiValueError as ApiValueError
from ls_zoho_billing_items.exceptions import ApiKeyError as ApiKeyError
from ls_zoho_billing_items.exceptions import ApiAttributeError as ApiAttributeError
from ls_zoho_billing_items.exceptions import ApiException as ApiException

# import models into sdk package
from ls_zoho_billing_items.models.create_an_item_request import CreateAnItemRequest as CreateAnItemRequest
from ls_zoho_billing_items.models.create_an_item_response import CreateAnItemResponse as CreateAnItemResponse
from ls_zoho_billing_items.models.custom_fields_inner import CustomFieldsInner as CustomFieldsInner
from ls_zoho_billing_items.models.delete_an_item_response import DeleteAnItemResponse as DeleteAnItemResponse
from ls_zoho_billing_items.models.item_response import ItemResponse as ItemResponse
from ls_zoho_billing_items.models.item_tax_preferences_inner import ItemTaxPreferencesInner as ItemTaxPreferencesInner
from ls_zoho_billing_items.models.list_items_response import ListItemsResponse as ListItemsResponse
from ls_zoho_billing_items.models.list_items_response_items_inner import ListItemsResponseItemsInner as ListItemsResponseItemsInner
from ls_zoho_billing_items.models.mark_as_active_response import MarkAsActiveResponse as MarkAsActiveResponse
from ls_zoho_billing_items.models.mark_as_inactive_response import MarkAsInactiveResponse as MarkAsInactiveResponse
from ls_zoho_billing_items.models.retrieve_an_item_response import RetrieveAnItemResponse as RetrieveAnItemResponse
from ls_zoho_billing_items.models.update_an_item_request import UpdateAnItemRequest as UpdateAnItemRequest
from ls_zoho_billing_items.models.update_an_item_response import UpdateAnItemResponse as UpdateAnItemResponse
from ls_zoho_billing_items.models.update_an_item_response_item import UpdateAnItemResponseItem as UpdateAnItemResponseItem
from ls_zoho_billing_items.models.warehouses_inner import WarehousesInner as WarehousesInner
