# DeleteAnItemResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] [readonly] 
**message** | **str** |  | [optional] [readonly] 

## Example

```python
from ls_zoho_billing_items.models.delete_an_item_response import DeleteAnItemResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteAnItemResponse from a JSON string
delete_an_item_response_instance = DeleteAnItemResponse.from_json(json)
# print the JSON string representation of the object
print(DeleteAnItemResponse.to_json())

# convert the object into a dict
delete_an_item_response_dict = delete_an_item_response_instance.to_dict()
# create an instance of DeleteAnItemResponse from a dict
delete_an_item_response_from_dict = DeleteAnItemResponse.from_dict(delete_an_item_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


