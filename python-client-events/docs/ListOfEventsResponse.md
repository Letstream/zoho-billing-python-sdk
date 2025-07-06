# ListOfEventsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] [readonly] 
**message** | **str** |  | [optional] [readonly] 
**events** | [**List[ListOfEventsResponseEventsInner]**](ListOfEventsResponseEventsInner.md) |  | [optional] 

## Example

```python
from ls_zoho_billing_events.models.list_of_events_response import ListOfEventsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListOfEventsResponse from a JSON string
list_of_events_response_instance = ListOfEventsResponse.from_json(json)
# print the JSON string representation of the object
print(ListOfEventsResponse.to_json())

# convert the object into a dict
list_of_events_response_dict = list_of_events_response_instance.to_dict()
# create an instance of ListOfEventsResponse from a dict
list_of_events_response_from_dict = ListOfEventsResponse.from_dict(list_of_events_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


