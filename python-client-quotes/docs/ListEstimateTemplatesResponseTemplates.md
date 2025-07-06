# ListEstimateTemplatesResponseTemplates

Template used for the quote

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**template_name** | **str** | Name of the template used | [optional] 
**template_id** | **str** | ID of the template used for the quote | [optional] 
**template_type** | **str** | The type of template used | [optional] 

## Example

```python
from ls_zoho_billing_quotes.models.list_estimate_templates_response_templates import ListEstimateTemplatesResponseTemplates

# TODO update the JSON string below
json = "{}"
# create an instance of ListEstimateTemplatesResponseTemplates from a JSON string
list_estimate_templates_response_templates_instance = ListEstimateTemplatesResponseTemplates.from_json(json)
# print the JSON string representation of the object
print(ListEstimateTemplatesResponseTemplates.to_json())

# convert the object into a dict
list_estimate_templates_response_templates_dict = list_estimate_templates_response_templates_instance.to_dict()
# create an instance of ListEstimateTemplatesResponseTemplates from a dict
list_estimate_templates_response_templates_from_dict = ListEstimateTemplatesResponseTemplates.from_dict(list_estimate_templates_response_templates_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


