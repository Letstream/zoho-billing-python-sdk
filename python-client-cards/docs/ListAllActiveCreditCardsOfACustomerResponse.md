# ListAllActiveCreditCardsOfACustomerResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] [readonly] 
**message** | **str** |  | [optional] [readonly] 
**cards** | [**List[ListAllActiveCreditCardsOfACustomerResponseCardsInner]**](ListAllActiveCreditCardsOfACustomerResponseCardsInner.md) |  | [optional] 

## Example

```python
from ls_zoho_billing_cards.models.list_all_active_credit_cards_of_a_customer_response import ListAllActiveCreditCardsOfACustomerResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListAllActiveCreditCardsOfACustomerResponse from a JSON string
list_all_active_credit_cards_of_a_customer_response_instance = ListAllActiveCreditCardsOfACustomerResponse.from_json(json)
# print the JSON string representation of the object
print(ListAllActiveCreditCardsOfACustomerResponse.to_json())

# convert the object into a dict
list_all_active_credit_cards_of_a_customer_response_dict = list_all_active_credit_cards_of_a_customer_response_instance.to_dict()
# create an instance of ListAllActiveCreditCardsOfACustomerResponse from a dict
list_all_active_credit_cards_of_a_customer_response_from_dict = ListAllActiveCreditCardsOfACustomerResponse.from_dict(list_all_active_credit_cards_of_a_customer_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


