# ListOfEventsResponseEventsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event_id** | **str** | Unique ID generated for a particular event | [optional] 
**event_type** | **str** | The type of event. | [optional] 
**event_time** | **str** | The time at which the event is created. | [optional] 

## Example

```python
from ls_zoho_billing_events.models.list_of_events_response_events_inner import ListOfEventsResponseEventsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ListOfEventsResponseEventsInner from a JSON string
list_of_events_response_events_inner_instance = ListOfEventsResponseEventsInner.from_json(json)
# print the JSON string representation of the object
print(ListOfEventsResponseEventsInner.to_json())

# convert the object into a dict
list_of_events_response_events_inner_dict = list_of_events_response_events_inner_instance.to_dict()
# create an instance of ListOfEventsResponseEventsInner from a dict
list_of_events_response_events_inner_from_dict = ListOfEventsResponseEventsInner.from_dict(list_of_events_response_events_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


