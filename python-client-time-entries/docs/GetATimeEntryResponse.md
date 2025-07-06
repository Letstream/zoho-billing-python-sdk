# GetATimeEntryResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] [readonly] 
**message** | **str** |  | [optional] [readonly] 
**time_entry** | [**UpdateTimeEntryResponseTimeEntry**](UpdateTimeEntryResponseTimeEntry.md) |  | [optional] 

## Example

```python
from ls_zoho_billing_time_entries.models.get_a_time_entry_response import GetATimeEntryResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetATimeEntryResponse from a JSON string
get_a_time_entry_response_instance = GetATimeEntryResponse.from_json(json)
# print the JSON string representation of the object
print(GetATimeEntryResponse.to_json())

# convert the object into a dict
get_a_time_entry_response_dict = get_a_time_entry_response_instance.to_dict()
# create an instance of GetATimeEntryResponse from a dict
get_a_time_entry_response_from_dict = GetATimeEntryResponse.from_dict(get_a_time_entry_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


