# LineItemsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**item_id** | **str** | Unique ID of the item. | [optional] 
**name** | **str** | The name of the line item | [optional] 
**description** | **str** | The description of the line items | [optional] 
**item_order** | **int** | The order of the line item_order | [optional] 
**bcy_rate** | **float** | base currency rate | [optional] 
**rate** | **float** | Rate of the line item. | [optional] 
**quantity** | **float** | The quantity of line item | [optional] 
**unit** | **str** | Unit of measuring the line item e.g. kgs, Nos. | [optional] 
**discount_amount** | **float** | The discount amount on the line item | [optional] 
**discount** | **float** | Discount applied to the invoice. It can be either in % or in amount. e.g. 12.5% or 190. | [optional] 
**tax_id** | **str** | ID of the tax or tax group applied to the quote | [optional] 
**tax_name** | **str** | The name of the tax | [optional] 
**tax_type** | **str** | The type of the tax | [optional] 
**tax_percentage** | **float** | The  percentage of tax levied | [optional] 
**item_total** | **float** | The total amount of the line items | [optional] 

## Example

```python
from ls_zoho_billing_quotes.models.line_items_inner import LineItemsInner

# TODO update the JSON string below
json = "{}"
# create an instance of LineItemsInner from a JSON string
line_items_inner_instance = LineItemsInner.from_json(json)
# print the JSON string representation of the object
print(LineItemsInner.to_json())

# convert the object into a dict
line_items_inner_dict = line_items_inner_instance.to_dict()
# create an instance of LineItemsInner from a dict
line_items_inner_from_dict = LineItemsInner.from_dict(line_items_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


