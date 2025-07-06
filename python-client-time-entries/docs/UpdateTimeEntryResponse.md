# UpdateTimeEntryResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] [readonly] 
**message** | **str** |  | [optional] [readonly] 
**time_entry** | [**UpdateTimeEntryResponseTimeEntry**](UpdateTimeEntryResponseTimeEntry.md) |  | [optional] 

## Example

```python
from ls_zoho_billing_time_entries.models.update_time_entry_response import UpdateTimeEntryResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateTimeEntryResponse from a JSON string
update_time_entry_response_instance = UpdateTimeEntryResponse.from_json(json)
# print the JSON string representation of the object
print(UpdateTimeEntryResponse.to_json())

# convert the object into a dict
update_time_entry_response_dict = update_time_entry_response_instance.to_dict()
# create an instance of UpdateTimeEntryResponse from a dict
update_time_entry_response_from_dict = UpdateTimeEntryResponse.from_dict(update_time_entry_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


