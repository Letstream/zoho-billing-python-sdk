# MarkAnEstimateAsSentResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] [readonly] 
**message** | **str** |  | [optional] [readonly] 

## Example

```python
from ls_zoho_billing_quotes.models.mark_an_estimate_as_sent_response import MarkAnEstimateAsSentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MarkAnEstimateAsSentResponse from a JSON string
mark_an_estimate_as_sent_response_instance = MarkAnEstimateAsSentResponse.from_json(json)
# print the JSON string representation of the object
print(MarkAnEstimateAsSentResponse.to_json())

# convert the object into a dict
mark_an_estimate_as_sent_response_dict = mark_an_estimate_as_sent_response_instance.to_dict()
# create an instance of MarkAnEstimateAsSentResponse from a dict
mark_an_estimate_as_sent_response_from_dict = MarkAnEstimateAsSentResponse.from_dict(mark_an_estimate_as_sent_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


