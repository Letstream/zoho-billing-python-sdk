# CreateAnItemResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] [readonly] 
**message** | **str** |  | [optional] [readonly] 
**item** | [**ItemResponse**](ItemResponse.md) |  | [optional] 

## Example

```python
from ls_zoho_billing_items.models.create_an_item_response import CreateAnItemResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAnItemResponse from a JSON string
create_an_item_response_instance = CreateAnItemResponse.from_json(json)
# print the JSON string representation of the object
print(CreateAnItemResponse.to_json())

# convert the object into a dict
create_an_item_response_dict = create_an_item_response_instance.to_dict()
# create an instance of CreateAnItemResponse from a dict
create_an_item_response_from_dict = CreateAnItemResponse.from_dict(create_an_item_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


