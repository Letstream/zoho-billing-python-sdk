# ItemCustomFieldsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** | Label of the Custom Field | [optional] 
**value** | **str** | Value of the Custom Field | [optional] 

## Example

```python
from ls_zoho_billing_hosted_pages.models.item_custom_fields_inner import ItemCustomFieldsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ItemCustomFieldsInner from a JSON string
item_custom_fields_inner_instance = ItemCustomFieldsInner.from_json(json)
# print the JSON string representation of the object
print(ItemCustomFieldsInner.to_json())

# convert the object into a dict
item_custom_fields_inner_dict = item_custom_fields_inner_instance.to_dict()
# create an instance of ItemCustomFieldsInner from a dict
item_custom_fields_inner_from_dict = ItemCustomFieldsInner.from_dict(item_custom_fields_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


