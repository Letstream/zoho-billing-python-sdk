# RemoveCardResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] [readonly] 
**message** | **str** |  | [optional] [readonly] 

## Example

```python
from ls_zoho_billing_subscription.models.remove_card_response import RemoveCardResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RemoveCardResponse from a JSON string
remove_card_response_instance = RemoveCardResponse.from_json(json)
# print the JSON string representation of the object
print(RemoveCardResponse.to_json())

# convert the object into a dict
remove_card_response_dict = remove_card_response_instance.to_dict()
# create an instance of RemoveCardResponse from a dict
remove_card_response_from_dict = RemoveCardResponse.from_dict(remove_card_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


