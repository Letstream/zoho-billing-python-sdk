# RetrieveACreditCardInformationResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] [readonly] 
**message** | **str** |  | [optional] [readonly] 
**card** | [**CardResponse**](CardResponse.md) |  | [optional] 

## Example

```python
from ls_zoho_billing_cards.models.retrieve_a_credit_card_information_response import RetrieveACreditCardInformationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RetrieveACreditCardInformationResponse from a JSON string
retrieve_a_credit_card_information_response_instance = RetrieveACreditCardInformationResponse.from_json(json)
# print the JSON string representation of the object
print(RetrieveACreditCardInformationResponse.to_json())

# convert the object into a dict
retrieve_a_credit_card_information_response_dict = retrieve_a_credit_card_information_response_instance.to_dict()
# create an instance of RetrieveACreditCardInformationResponse from a dict
retrieve_a_credit_card_information_response_from_dict = RetrieveACreditCardInformationResponse.from_dict(retrieve_a_credit_card_information_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


