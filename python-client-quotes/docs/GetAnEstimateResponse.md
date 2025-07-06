# GetAnEstimateResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] [readonly] 
**message** | **str** |  | [optional] [readonly] 
**estimate** | [**GetAnEstimateResponseEstimate**](GetAnEstimateResponseEstimate.md) |  | [optional] 

## Example

```python
from ls_zoho_billing_quotes.models.get_an_estimate_response import GetAnEstimateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetAnEstimateResponse from a JSON string
get_an_estimate_response_instance = GetAnEstimateResponse.from_json(json)
# print the JSON string representation of the object
print(GetAnEstimateResponse.to_json())

# convert the object into a dict
get_an_estimate_response_dict = get_an_estimate_response_instance.to_dict()
# create an instance of GetAnEstimateResponse from a dict
get_an_estimate_response_from_dict = GetAnEstimateResponse.from_dict(get_an_estimate_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


