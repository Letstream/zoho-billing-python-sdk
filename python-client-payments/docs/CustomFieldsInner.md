# CustomFieldsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** | Value of the custom field. | [optional] 
**label** | **str** | Label of the custom field. | [optional] 
**data_type** | **str** | Data type of the custom field. | [optional] 

## Example

```python
from ls_zoho_billing_payments.models.custom_fields_inner import CustomFieldsInner

# TODO update the JSON string below
json = "{}"
# create an instance of CustomFieldsInner from a JSON string
custom_fields_inner_instance = CustomFieldsInner.from_json(json)
# print the JSON string representation of the object
print(CustomFieldsInner.to_json())

# convert the object into a dict
custom_fields_inner_dict = custom_fields_inner_instance.to_dict()
# create an instance of CustomFieldsInner from a dict
custom_fields_inner_from_dict = CustomFieldsInner.from_dict(custom_fields_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


