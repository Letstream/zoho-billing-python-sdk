# ListOfTransactionsResponseTransactionsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction_id** | **str** | Unique ID to denote the transaction. | [optional] 
**reference_id** | **str** | Unique reference number to denote the transaction. | [optional] 
**var_date** | **str** | Date when the transaction was recorded. | [optional] 
**type** | **str** | Type of the transaction. | [optional] 
**status** | **str** | Status of the customer. It can either be &lt;code&gt;active&lt;/code&gt; or &lt;code&gt;inactive&lt;/code&gt;. | [optional] 
**amount** | **str** | Amount involved in the transaction. | [optional] 

## Example

```python
from ls_zoho_billing_customers.models.list_of_transactions_response_transactions_inner import ListOfTransactionsResponseTransactionsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ListOfTransactionsResponseTransactionsInner from a JSON string
list_of_transactions_response_transactions_inner_instance = ListOfTransactionsResponseTransactionsInner.from_json(json)
# print the JSON string representation of the object
print(ListOfTransactionsResponseTransactionsInner.to_json())

# convert the object into a dict
list_of_transactions_response_transactions_inner_dict = list_of_transactions_response_transactions_inner_instance.to_dict()
# create an instance of ListOfTransactionsResponseTransactionsInner from a dict
list_of_transactions_response_transactions_inner_from_dict = ListOfTransactionsResponseTransactionsInner.from_dict(list_of_transactions_response_transactions_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


