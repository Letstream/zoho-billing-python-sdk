# AddItemsToAPendingInvoiceRequestInvoiceItemsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **object** | Addon code of the addon. | [optional] 
**product_id** | **object** | Product ID of the product to which the addon is associated with. | [optional] 
**name** | **object** | Name for the item. | [optional] 
**description** | **object** | Description for the item. | [optional] 
**price** | **float** | Price of the item. | [optional] 
**quantity** | **int** | Required quantity of the chosen item. | [optional] 
**tax_id** | **object** | Unique ID of Tax or Tax Group that must be associated with the item. | [optional] 
**tax_exemption_id** | **object** | Unique Tax Exemption ID if you dont want to associate a tax to the plan. | [optional] 

## Example

```python
from ls_zoho_billing_invoices.models.add_items_to_a_pending_invoice_request_invoice_items_inner import AddItemsToAPendingInvoiceRequestInvoiceItemsInner

# TODO update the JSON string below
json = "{}"
# create an instance of AddItemsToAPendingInvoiceRequestInvoiceItemsInner from a JSON string
add_items_to_a_pending_invoice_request_invoice_items_inner_instance = AddItemsToAPendingInvoiceRequestInvoiceItemsInner.from_json(json)
# print the JSON string representation of the object
print(AddItemsToAPendingInvoiceRequestInvoiceItemsInner.to_json())

# convert the object into a dict
add_items_to_a_pending_invoice_request_invoice_items_inner_dict = add_items_to_a_pending_invoice_request_invoice_items_inner_instance.to_dict()
# create an instance of AddItemsToAPendingInvoiceRequestInvoiceItemsInner from a dict
add_items_to_a_pending_invoice_request_invoice_items_inner_from_dict = AddItemsToAPendingInvoiceRequestInvoiceItemsInner.from_dict(add_items_to_a_pending_invoice_request_invoice_items_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


