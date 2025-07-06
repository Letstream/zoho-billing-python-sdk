# ListItemsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] [readonly] 
**message** | **str** |  | [optional] [readonly] 
**items** | [**List[ListItemsResponseItemsInner]**](ListItemsResponseItemsInner.md) |  | [optional] 

## Example

```python
from ls_zoho_billing_items.models.list_items_response import ListItemsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListItemsResponse from a JSON string
list_items_response_instance = ListItemsResponse.from_json(json)
# print the JSON string representation of the object
print(ListItemsResponse.to_json())

# convert the object into a dict
list_items_response_dict = list_items_response_instance.to_dict()
# create an instance of ListItemsResponse from a dict
list_items_response_from_dict = ListItemsResponse.from_dict(list_items_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


