# ListTasksResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] [readonly] 
**message** | **str** |  | [optional] [readonly] 
**tasks** | [**List[ListTasksResponseTasksInner]**](ListTasksResponseTasksInner.md) |  | [optional] 

## Example

```python
from ls_zoho_billing_tasks.models.list_tasks_response import ListTasksResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListTasksResponse from a JSON string
list_tasks_response_instance = ListTasksResponse.from_json(json)
# print the JSON string representation of the object
print(ListTasksResponse.to_json())

# convert the object into a dict
list_tasks_response_dict = list_tasks_response_instance.to_dict()
# create an instance of ListTasksResponse from a dict
list_tasks_response_from_dict = ListTasksResponse.from_dict(list_tasks_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


