# UpdateCustomFieldsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**custom_fields** | [**List[UpdateCustomFieldsRequestCustomFieldsInner]**](UpdateCustomFieldsRequestCustomFieldsInner.md) | Additional fields for the invoices. | 

## Example

```python
from ls_zoho_billing_invoices.models.update_custom_fields_request import UpdateCustomFieldsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateCustomFieldsRequest from a JSON string
update_custom_fields_request_instance = UpdateCustomFieldsRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateCustomFieldsRequest.to_json())

# convert the object into a dict
update_custom_fields_request_dict = update_custom_fields_request_instance.to_dict()
# create an instance of UpdateCustomFieldsRequest from a dict
update_custom_fields_request_from_dict = UpdateCustomFieldsRequest.from_dict(update_custom_fields_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


