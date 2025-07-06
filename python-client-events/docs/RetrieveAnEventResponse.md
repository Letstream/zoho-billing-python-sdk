# RetrieveAnEventResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] [readonly] 
**message** | **str** |  | [optional] [readonly] 
**event** | [**EventResponse**](EventResponse.md) |  | [optional] 

## Example

```python
from ls_zoho_billing_events.models.retrieve_an_event_response import RetrieveAnEventResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RetrieveAnEventResponse from a JSON string
retrieve_an_event_response_instance = RetrieveAnEventResponse.from_json(json)
# print the JSON string representation of the object
print(RetrieveAnEventResponse.to_json())

# convert the object into a dict
retrieve_an_event_response_dict = retrieve_an_event_response_instance.to_dict()
# create an instance of RetrieveAnEventResponse from a dict
retrieve_an_event_response_from_dict = RetrieveAnEventResponse.from_dict(retrieve_an_event_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


