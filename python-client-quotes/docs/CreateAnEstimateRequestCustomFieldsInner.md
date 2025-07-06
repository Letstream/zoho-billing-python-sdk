# CreateAnEstimateRequestCustomFieldsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** | Label for the quote | [optional] 
**value** | **str** | Value for the custom field | [optional] 

## Example

```python
from ls_zoho_billing_quotes.models.create_an_estimate_request_custom_fields_inner import CreateAnEstimateRequestCustomFieldsInner

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAnEstimateRequestCustomFieldsInner from a JSON string
create_an_estimate_request_custom_fields_inner_instance = CreateAnEstimateRequestCustomFieldsInner.from_json(json)
# print the JSON string representation of the object
print(CreateAnEstimateRequestCustomFieldsInner.to_json())

# convert the object into a dict
create_an_estimate_request_custom_fields_inner_dict = create_an_estimate_request_custom_fields_inner_instance.to_dict()
# create an instance of CreateAnEstimateRequestCustomFieldsInner from a dict
create_an_estimate_request_custom_fields_inner_from_dict = CreateAnEstimateRequestCustomFieldsInner.from_dict(create_an_estimate_request_custom_fields_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


