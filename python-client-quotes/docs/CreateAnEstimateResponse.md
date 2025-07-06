# CreateAnEstimateResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] [readonly] 
**message** | **str** |  | [optional] [readonly] 
**estimate** | [**EstimateResponse**](EstimateResponse.md) |  | [optional] 

## Example

```python
from ls_zoho_billing_quotes.models.create_an_estimate_response import CreateAnEstimateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAnEstimateResponse from a JSON string
create_an_estimate_response_instance = CreateAnEstimateResponse.from_json(json)
# print the JSON string representation of the object
print(CreateAnEstimateResponse.to_json())

# convert the object into a dict
create_an_estimate_response_dict = create_an_estimate_response_instance.to_dict()
# create an instance of CreateAnEstimateResponse from a dict
create_an_estimate_response_from_dict = CreateAnEstimateResponse.from_dict(create_an_estimate_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


