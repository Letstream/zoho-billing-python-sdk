# UnbilledChargeItemsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**unbilled_charge_item_id** | **str** | Unique ID generated for an item in the unbilled charge. | [optional] 
**product_id** | **str** | The ID of the product included in the unbilled charge. | [optional] 
**name** | **str** | Name of the item. | [optional] 
**description** | **object** | Description for the item. | [optional] 
**code** | **str** | Item code of the item. | [optional] 
**price** | **str** | Price of the item included in the invoice. | [optional] 
**quantity** | **int** | Quantity of the item. | [optional] 
**discount_amount** | **float** | The discount amount included on applying a coupon. | [optional] 
**item_total** | **int** | This would be the product of quantity of the item included and the price of that item. | [optional] 
**tax_id** | **object** | Unique ID of Tax or Tax Group that must be associated with the item. | [optional] 
**product_type** | **str** | Product type for UK Edition. | [optional] 
**hsn_or_sac** | **str** | HSN or SAC code for Goods/Services | [optional] 
**tax_exemption_id** | **object** | Unique Tax Exemption ID if you dont want to associate a tax to the plan. | [optional] 
**tax_exemption_code** | **str** | Unique code to denote the tax exemption. | [optional] 

## Example

```python
from ls_zoho_billing_unbilled_charges.models.unbilled_charge_items_inner import UnbilledChargeItemsInner

# TODO update the JSON string below
json = "{}"
# create an instance of UnbilledChargeItemsInner from a JSON string
unbilled_charge_items_inner_instance = UnbilledChargeItemsInner.from_json(json)
# print the JSON string representation of the object
print(UnbilledChargeItemsInner.to_json())

# convert the object into a dict
unbilled_charge_items_inner_dict = unbilled_charge_items_inner_instance.to_dict()
# create an instance of UnbilledChargeItemsInner from a dict
unbilled_charge_items_inner_from_dict = UnbilledChargeItemsInner.from_dict(unbilled_charge_items_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


