# WarehousesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**warehouse_id** | **str** | Enter warehouse ID | [optional] 
**warehouse_name** | **str** | Enter warehouse name | [optional] 
**status** | **str** | Status of the item. It can be &lt;code&gt;active&lt;/code&gt; or &lt;code&gt;inactive&lt;/code&gt;. It tells whether the Item is available for transactions. | [optional] 
**is_primary** | **bool** | Mention whether the item is primary or not | [optional] 
**warehouse_stock_on_hand** | **str** | Current available stock in your warehouse. | [optional] 
**warehouse_available_stock** | **str** | Available stock in your warehouse. | [optional] 
**warehouse_actual_available_stock** | **str** | Actual available stock in your warehouse. | [optional] 

## Example

```python
from ls_zoho_billing_items.models.warehouses_inner import WarehousesInner

# TODO update the JSON string below
json = "{}"
# create an instance of WarehousesInner from a JSON string
warehouses_inner_instance = WarehousesInner.from_json(json)
# print the JSON string representation of the object
print(WarehousesInner.to_json())

# convert the object into a dict
warehouses_inner_dict = warehouses_inner_instance.to_dict()
# create an instance of WarehousesInner from a dict
warehouses_inner_from_dict = WarehousesInner.from_dict(warehouses_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


