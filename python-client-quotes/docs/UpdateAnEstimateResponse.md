# UpdateAnEstimateResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] [readonly] 
**message** | **str** |  | [optional] [readonly] 
**estimate** | [**UpdateAnEstimateResponseEstimate**](UpdateAnEstimateResponseEstimate.md) |  | [optional] 

## Example

```python
from ls_zoho_billing_quotes.models.update_an_estimate_response import UpdateAnEstimateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateAnEstimateResponse from a JSON string
update_an_estimate_response_instance = UpdateAnEstimateResponse.from_json(json)
# print the JSON string representation of the object
print(UpdateAnEstimateResponse.to_json())

# convert the object into a dict
update_an_estimate_response_dict = update_an_estimate_response_instance.to_dict()
# create an instance of UpdateAnEstimateResponse from a dict
update_an_estimate_response_from_dict = UpdateAnEstimateResponse.from_dict(update_an_estimate_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


