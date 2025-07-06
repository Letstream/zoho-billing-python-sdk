# ListCommentsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] [readonly] 
**message** | **str** |  | [optional] [readonly] 
**comments** | [**List[ListCommentsResponseCommentsInner]**](ListCommentsResponseCommentsInner.md) |  | [optional] 

## Example

```python
from ls_zoho_billing_projects.models.list_comments_response import ListCommentsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListCommentsResponse from a JSON string
list_comments_response_instance = ListCommentsResponse.from_json(json)
# print the JSON string representation of the object
print(ListCommentsResponse.to_json())

# convert the object into a dict
list_comments_response_dict = list_comments_response_instance.to_dict()
# create an instance of ListCommentsResponse from a dict
list_comments_response_from_dict = ListCommentsResponse.from_dict(list_comments_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


