# CustomFieldsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customfield_id** | **int** | Unique ID of the custom field | [optional] 
**data_type** | **str** | Data type of the custom field | [optional] 
**index** | **int** | An index for the custom field. | [optional] 
**label** | **str** | Label for the quote | [optional] 
**show_on_pdf** | **bool** | Show exported file in PDF format | [optional] 
**show_in_all_pdf** | **object** | Enable/Disable show this custom field on all the pdf | [optional] 
**value** | **str** | Value for the custom field | [optional] 

## Example

```python
from ls_zoho_billing_quotes.models.custom_fields_inner import CustomFieldsInner

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


