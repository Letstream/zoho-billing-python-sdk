# CustomFieldsUpdateInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customfield_id** | **int** |  | [optional] 
**value** | **str** | Value of the Custom Field | [optional] 

## Example

```python
from ls_zoho_billing_invoices.models.custom_fields_update_inner import CustomFieldsUpdateInner

# TODO update the JSON string below
json = "{}"
# create an instance of CustomFieldsUpdateInner from a JSON string
custom_fields_update_inner_instance = CustomFieldsUpdateInner.from_json(json)
# print the JSON string representation of the object
print(CustomFieldsUpdateInner.to_json())

# convert the object into a dict
custom_fields_update_inner_dict = custom_fields_update_inner_instance.to_dict()
# create an instance of CustomFieldsUpdateInner from a dict
custom_fields_update_inner_from_dict = CustomFieldsUpdateInner.from_dict(custom_fields_update_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


