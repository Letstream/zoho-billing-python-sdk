# ListOfTransactionsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] [readonly] 
**message** | **str** |  | [optional] [readonly] 
**transactions** | [**List[ListOfTransactionsResponseTransactionsInner]**](ListOfTransactionsResponseTransactionsInner.md) |  | [optional] 

## Example

```python
from ls_zoho_billing_customers.models.list_of_transactions_response import ListOfTransactionsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListOfTransactionsResponse from a JSON string
list_of_transactions_response_instance = ListOfTransactionsResponse.from_json(json)
# print the JSON string representation of the object
print(ListOfTransactionsResponse.to_json())

# convert the object into a dict
list_of_transactions_response_dict = list_of_transactions_response_instance.to_dict()
# create an instance of ListOfTransactionsResponse from a dict
list_of_transactions_response_from_dict = ListOfTransactionsResponse.from_dict(list_of_transactions_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


