# StartTimerResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] [readonly] 
**message** | **str** |  | [optional] [readonly] 
**time_entry** | [**UpdateTimeEntryResponseTimeEntry**](UpdateTimeEntryResponseTimeEntry.md) |  | [optional] 

## Example

```python
from ls_zoho_billing_time_entries.models.start_timer_response import StartTimerResponse

# TODO update the JSON string below
json = "{}"
# create an instance of StartTimerResponse from a JSON string
start_timer_response_instance = StartTimerResponse.from_json(json)
# print the JSON string representation of the object
print(StartTimerResponse.to_json())

# convert the object into a dict
start_timer_response_dict = start_timer_response_instance.to_dict()
# create an instance of StartTimerResponse from a dict
start_timer_response_from_dict = StartTimerResponse.from_dict(start_timer_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


