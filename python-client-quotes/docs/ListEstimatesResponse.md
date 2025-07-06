# ListEstimatesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] [readonly] 
**message** | **str** |  | [optional] [readonly] 
**estimates** | [**List[ListEstimatesResponseEstimatesInner]**](ListEstimatesResponseEstimatesInner.md) |  | [optional] 

## Example

```python
from ls_zoho_billing_quotes.models.list_estimates_response import ListEstimatesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListEstimatesResponse from a JSON string
list_estimates_response_instance = ListEstimatesResponse.from_json(json)
# print the JSON string representation of the object
print(ListEstimatesResponse.to_json())

# convert the object into a dict
list_estimates_response_dict = list_estimates_response_instance.to_dict()
# create an instance of ListEstimatesResponse from a dict
list_estimates_response_from_dict = ListEstimatesResponse.from_dict(list_estimates_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


