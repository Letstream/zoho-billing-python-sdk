# UpdateCustomFieldsResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**index** | **int** | Index of the custom field. It can hold any value from 1 to 10. | [optional] 
**value** | **str** | Value of the Custom Field | [optional] 
**label** | **str** | Label of the Custom Field | [optional] 
**data_type** | **str** | Data type of the custom field. | [optional] 
**customfield_id** | **str** | Unique ID to denote the custom field. | [optional] 

## Example

```python
from ls_zoho_billing_subscription.models.update_custom_fields_response_data import UpdateCustomFieldsResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateCustomFieldsResponseData from a JSON string
update_custom_fields_response_data_instance = UpdateCustomFieldsResponseData.from_json(json)
# print the JSON string representation of the object
print(UpdateCustomFieldsResponseData.to_json())

# convert the object into a dict
update_custom_fields_response_data_dict = update_custom_fields_response_data_instance.to_dict()
# create an instance of UpdateCustomFieldsResponseData from a dict
update_custom_fields_response_data_from_dict = UpdateCustomFieldsResponseData.from_dict(update_custom_fields_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


