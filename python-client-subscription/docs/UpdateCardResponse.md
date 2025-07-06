# UpdateCardResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] [readonly] 
**message** | **str** |  | [optional] [readonly] 
**subscription** | [**UpdateCardResponseSubscription**](UpdateCardResponseSubscription.md) |  | [optional] 

## Example

```python
from ls_zoho_billing_subscription.models.update_card_response import UpdateCardResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateCardResponse from a JSON string
update_card_response_instance = UpdateCardResponse.from_json(json)
# print the JSON string representation of the object
print(UpdateCardResponse.to_json())

# convert the object into a dict
update_card_response_dict = update_card_response_instance.to_dict()
# create an instance of UpdateCardResponse from a dict
update_card_response_from_dict = UpdateCardResponse.from_dict(update_card_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


