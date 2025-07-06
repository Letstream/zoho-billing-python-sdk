# UpdateCustomFieldsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] [readonly] 
**message** | **str** |  | [optional] [readonly] 
**custom_fields** | [**List[UpdateCustomFieldsResponseCustomFieldsInner]**](UpdateCustomFieldsResponseCustomFieldsInner.md) | Additional fields for the invoices. | [optional] 

## Example

```python
from ls_zoho_billing_invoices.models.update_custom_fields_response import UpdateCustomFieldsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateCustomFieldsResponse from a JSON string
update_custom_fields_response_instance = UpdateCustomFieldsResponse.from_json(json)
# print the JSON string representation of the object
print(UpdateCustomFieldsResponse.to_json())

# convert the object into a dict
update_custom_fields_response_dict = update_custom_fields_response_instance.to_dict()
# create an instance of UpdateCustomFieldsResponse from a dict
update_custom_fields_response_from_dict = UpdateCustomFieldsResponse.from_dict(update_custom_fields_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


