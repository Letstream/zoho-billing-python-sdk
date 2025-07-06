# DeleteACreditCardResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] [readonly] 
**message** | **str** |  | [optional] [readonly] 

## Example

```python
from ls_zoho_billing_cards.models.delete_a_credit_card_response import DeleteACreditCardResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteACreditCardResponse from a JSON string
delete_a_credit_card_response_instance = DeleteACreditCardResponse.from_json(json)
# print the JSON string representation of the object
print(DeleteACreditCardResponse.to_json())

# convert the object into a dict
delete_a_credit_card_response_dict = delete_a_credit_card_response_instance.to_dict()
# create an instance of DeleteACreditCardResponse from a dict
delete_a_credit_card_response_from_dict = DeleteACreditCardResponse.from_dict(delete_a_credit_card_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


