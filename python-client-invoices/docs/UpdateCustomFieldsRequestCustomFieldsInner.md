# UpdateCustomFieldsRequestCustomFieldsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** | Label of the Custom Field | 
**value** | **str** | Value of the Custom Field | 

## Example

```python
from ls_zoho_billing_invoices.models.update_custom_fields_request_custom_fields_inner import UpdateCustomFieldsRequestCustomFieldsInner

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateCustomFieldsRequestCustomFieldsInner from a JSON string
update_custom_fields_request_custom_fields_inner_instance = UpdateCustomFieldsRequestCustomFieldsInner.from_json(json)
# print the JSON string representation of the object
print(UpdateCustomFieldsRequestCustomFieldsInner.to_json())

# convert the object into a dict
update_custom_fields_request_custom_fields_inner_dict = update_custom_fields_request_custom_fields_inner_instance.to_dict()
# create an instance of UpdateCustomFieldsRequestCustomFieldsInner from a dict
update_custom_fields_request_custom_fields_inner_from_dict = UpdateCustomFieldsRequestCustomFieldsInner.from_dict(update_custom_fields_request_custom_fields_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


