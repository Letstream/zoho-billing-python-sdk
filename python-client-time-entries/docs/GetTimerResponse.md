# GetTimerResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] [readonly] 
**message** | **str** |  | [optional] [readonly] 
**time_entry** | [**UpdateTimeEntryResponseTimeEntry**](UpdateTimeEntryResponseTimeEntry.md) |  | [optional] 

## Example

```python
from ls_zoho_billing_time_entries.models.get_timer_response import GetTimerResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetTimerResponse from a JSON string
get_timer_response_instance = GetTimerResponse.from_json(json)
# print the JSON string representation of the object
print(GetTimerResponse.to_json())

# convert the object into a dict
get_timer_response_dict = get_timer_response_instance.to_dict()
# create an instance of GetTimerResponse from a dict
get_timer_response_from_dict = GetTimerResponse.from_dict(get_timer_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


