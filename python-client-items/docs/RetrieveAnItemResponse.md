# RetrieveAnItemResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] [readonly] 
**message** | **str** |  | [optional] [readonly] 
**item** | [**UpdateAnItemResponseItem**](UpdateAnItemResponseItem.md) |  | [optional] 

## Example

```python
from ls_zoho_billing_items.models.retrieve_an_item_response import RetrieveAnItemResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RetrieveAnItemResponse from a JSON string
retrieve_an_item_response_instance = RetrieveAnItemResponse.from_json(json)
# print the JSON string representation of the object
print(RetrieveAnItemResponse.to_json())

# convert the object into a dict
retrieve_an_item_response_dict = retrieve_an_item_response_instance.to_dict()
# create an instance of RetrieveAnItemResponse from a dict
retrieve_an_item_response_from_dict = RetrieveAnItemResponse.from_dict(retrieve_an_item_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


