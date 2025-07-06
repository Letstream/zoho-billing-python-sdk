# ListTimeEntriesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] [readonly] 
**message** | **str** |  | [optional] [readonly] 
**time_entries** | [**List[ListTimeEntriesResponseTimeEntriesInner]**](ListTimeEntriesResponseTimeEntriesInner.md) |  | [optional] 

## Example

```python
from ls_zoho_billing_time_entries.models.list_time_entries_response import ListTimeEntriesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListTimeEntriesResponse from a JSON string
list_time_entries_response_instance = ListTimeEntriesResponse.from_json(json)
# print the JSON string representation of the object
print(ListTimeEntriesResponse.to_json())

# convert the object into a dict
list_time_entries_response_dict = list_time_entries_response_instance.to_dict()
# create an instance of ListTimeEntriesResponse from a dict
list_time_entries_response_from_dict = ListTimeEntriesResponse.from_dict(list_time_entries_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


