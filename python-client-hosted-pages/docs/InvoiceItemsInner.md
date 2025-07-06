# InvoiceItemsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**item_id** | **str** | The ID of the item included in the invoice. | [optional] 
**name** | **object** | Name which denotes the invoice. | [optional] 
**description** | **object** | Small description about the Invoice item. | [optional] 
**code** | **str** | code for the response received. | [optional] 
**price** | **float** | Price of a plan for a particular subscription. If a value is provided here, the plan’s price for this subscription will be changed to the given value. If no value is provided, the plan’s price would be the same as what it was when it was created. | [optional] 
**quantity** | **int** | Required quantity of the chosen plan. | [optional] 
**discount_amount** | **float** | The discount amount included in an invoice on applying a coupon. | [optional] 
**item_total** | **int** | Cost of an item included in the invoice. This would be the product of quantity of the item included and the price of that item. | [optional] 
**tax_id** | **str** | Unique ID of the tax or tax group that can be collected from the contact. Tax can be given only if &lt;code&gt;is_taxable&lt;/code&gt; is &lt;code&gt;true&lt;/code&gt;. | [optional] 
**tax_exemption_id** | **str** | Unique ID of the tax exemption. | [optional] 
**tax_exemption_code** | **str** | Unique code of the tax exemption. | [optional] 

## Example

```python
from ls_zoho_billing_hosted_pages.models.invoice_items_inner import InvoiceItemsInner

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


