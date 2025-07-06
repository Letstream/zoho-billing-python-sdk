# ListEstimateTemplatesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] [readonly] 
**message** | **str** |  | [optional] [readonly] 
**templates** | [**ListEstimateTemplatesResponseTemplates**](ListEstimateTemplatesResponseTemplates.md) |  | [optional] 

## Example

```python
from ls_zoho_billing_quotes.models.list_estimate_templates_response import ListEstimateTemplatesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListEstimateTemplatesResponse from a JSON string
list_estimate_templates_response_instance = ListEstimateTemplatesResponse.from_json(json)
# print the JSON string representation of the object
print(ListEstimateTemplatesResponse.to_json())

# convert the object into a dict
list_estimate_templates_response_dict = list_estimate_templates_response_instance.to_dict()
# create an instance of ListEstimateTemplatesResponse from a dict
list_estimate_templates_response_from_dict = ListEstimateTemplatesResponse.from_dict(list_estimate_templates_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


