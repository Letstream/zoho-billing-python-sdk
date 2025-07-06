# UpdateAnItemResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] [readonly] 
**message** | **str** |  | [optional] [readonly] 
**item** | [**UpdateAnItemResponseItem**](UpdateAnItemResponseItem.md) |  | [optional] 

## Example

```python
from ls_zoho_billing_items.models.update_an_item_response import UpdateAnItemResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateAnItemResponse from a JSON string
update_an_item_response_instance = UpdateAnItemResponse.from_json(json)
# print the JSON string representation of the object
print(UpdateAnItemResponse.to_json())

# convert the object into a dict
update_an_item_response_dict = update_an_item_response_instance.to_dict()
# create an instance of UpdateAnItemResponse from a dict
update_an_item_response_from_dict = UpdateAnItemResponse.from_dict(update_an_item_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


