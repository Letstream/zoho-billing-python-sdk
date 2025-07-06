# UpdateEstimateTemplateResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] [readonly] 
**message** | **str** |  | [optional] [readonly] 

## Example

```python
from ls_zoho_billing_quotes.models.update_estimate_template_response import UpdateEstimateTemplateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateEstimateTemplateResponse from a JSON string
update_estimate_template_response_instance = UpdateEstimateTemplateResponse.from_json(json)
# print the JSON string representation of the object
print(UpdateEstimateTemplateResponse.to_json())

# convert the object into a dict
update_estimate_template_response_dict = update_estimate_template_response_instance.to_dict()
# create an instance of UpdateEstimateTemplateResponse from a dict
update_estimate_template_response_from_dict = UpdateEstimateTemplateResponse.from_dict(update_estimate_template_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


