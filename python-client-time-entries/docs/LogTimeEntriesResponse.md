# LogTimeEntriesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] [readonly] 
**message** | **str** |  | [optional] [readonly] 
**time_entry** | [**TimeEntryResponse**](TimeEntryResponse.md) |  | [optional] 

## Example

```python
from ls_zoho_billing_time_entries.models.log_time_entries_response import LogTimeEntriesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of LogTimeEntriesResponse from a JSON string
log_time_entries_response_instance = LogTimeEntriesResponse.from_json(json)
# print the JSON string representation of the object
print(LogTimeEntriesResponse.to_json())

# convert the object into a dict
log_time_entries_response_dict = log_time_entries_response_instance.to_dict()
# create an instance of LogTimeEntriesResponse from a dict
log_time_entries_response_from_dict = LogTimeEntriesResponse.from_dict(log_time_entries_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


