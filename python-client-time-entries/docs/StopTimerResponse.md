# StopTimerResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] [readonly] 
**message** | **str** |  | [optional] [readonly] 
**time_entry** | [**UpdateTimeEntryResponseTimeEntry**](UpdateTimeEntryResponseTimeEntry.md) |  | [optional] 

## Example

```python
from ls_zoho_billing_time_entries.models.stop_timer_response import StopTimerResponse

# TODO update the JSON string below
json = "{}"
# create an instance of StopTimerResponse from a JSON string
stop_timer_response_instance = StopTimerResponse.from_json(json)
# print the JSON string representation of the object
print(StopTimerResponse.to_json())

# convert the object into a dict
stop_timer_response_dict = stop_timer_response_instance.to_dict()
# create an instance of StopTimerResponse from a dict
stop_timer_response_from_dict = StopTimerResponse.from_dict(stop_timer_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


