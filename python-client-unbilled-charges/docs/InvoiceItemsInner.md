# InvoiceItemsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**item_id** | **str** | The ID of the item included in the invoice. | [optional] 
**name** | **str** | Name of the item. | [optional] 
**description** | **object** | Description for the item. | [optional] 
**code** | **str** | Item code of the item. | [optional] 
**price** | **str** | Price of the item included in the invoice. | [optional] 
**quantity** | **int** | Quantity of the item. | [optional] 
**discount_amount** | **float** | The discount amount included on applying a coupon. | [optional] 
**item_total** | **int** | This would be the product of quantity of the item included and the price of that item. | [optional] 
**tax_id** | **object** | Unique ID of Tax or Tax Group that must be associated with the item. | [optional] 
**tax_exemption_id** | **object** | Unique Tax Exemption ID if you dont want to associate a tax to the plan. | [optional] 
**tax_exemption_code** | **str** | Unique code to denote the tax exemption. | [optional] 

## Example

```python
from ls_zoho_billing_unbilled_charges.models.invoice_items_inner import InvoiceItemsInner

# TODO update the JSON string below
json = "{}"
# create an instance of InvoiceItemsInner from a JSON string
invoice_items_inner_instance = InvoiceItemsInner.from_json(json)
# print the JSON string representation of the object
print(InvoiceItemsInner.to_json())

# convert the object into a dict
invoice_items_inner_dict = invoice_items_inner_instance.to_dict()
# create an instance of InvoiceItemsInner from a dict
invoice_items_inner_from_dict = InvoiceItemsInner.from_dict(invoice_items_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


