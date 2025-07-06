# AddItemsToAPendingInvoiceResponseInvoiceInvoiceItemsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**item_id** | **str** | The ID of the item included in the invoice. | [optional] 
**name** | **str** | Name of the item included in the invoice. | [optional] 
**description** | **object** | Small description about the Invoice item. | [optional] 
**tags** | [**List[TagsInner]**](TagsInner.md) |  | [optional] 
**item_custom_fields** | [**List[ItemCustomFieldsInner]**](ItemCustomFieldsInner.md) | Custom fields for a item. | [optional] 
**code** | **str** | Item code of the item included in the invoice. | [optional] 
**price** | **str** | Price of the item included in the invoice. | [optional] 
**quantity** | **int** | Quantity of the item included in the invoice. | [optional] 
**discount_amount** | **float** | The discount amount included in an invoice on applying a coupon. | [optional] 
**item_total** | **int** | Cost of an item included in the invoice. This would be the product of quantity of the item included and the price of that item. | [optional] 
**tax_id** | **str** | Tax ID to which you would like to associate with this plan. | [optional] 
**product_type** | **str** | Product type for UK Edition. | [optional] 
**hsn_or_sac** | **str** | HSN or SAC code for Goods/Services | [optional] 
**tax_exemption_id** | **str** | Unique Tax Exemption ID if you dont want to associate a tax to the plan. | [optional] 
**tax_exemption_code** | **str** | Unique code to denote the tax exemption. | [optional] 

## Example

```python
from ls_zoho_billing_invoices.models.add_items_to_a_pending_invoice_response_invoice_invoice_items_inner import AddItemsToAPendingInvoiceResponseInvoiceInvoiceItemsInner

# TODO update the JSON string below
json = "{}"
# create an instance of AddItemsToAPendingInvoiceResponseInvoiceInvoiceItemsInner from a JSON string
add_items_to_a_pending_invoice_response_invoice_invoice_items_inner_instance = AddItemsToAPendingInvoiceResponseInvoiceInvoiceItemsInner.from_json(json)
# print the JSON string representation of the object
print(AddItemsToAPendingInvoiceResponseInvoiceInvoiceItemsInner.to_json())

# convert the object into a dict
add_items_to_a_pending_invoice_response_invoice_invoice_items_inner_dict = add_items_to_a_pending_invoice_response_invoice_invoice_items_inner_instance.to_dict()
# create an instance of AddItemsToAPendingInvoiceResponseInvoiceInvoiceItemsInner from a dict
add_items_to_a_pending_invoice_response_invoice_invoice_items_inner_from_dict = AddItemsToAPendingInvoiceResponseInvoiceInvoiceItemsInner.from_dict(add_items_to_a_pending_invoice_response_invoice_invoice_items_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


