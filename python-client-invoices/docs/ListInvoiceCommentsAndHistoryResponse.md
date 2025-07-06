# ListInvoiceCommentsAndHistoryResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] [readonly] 
**message** | **str** |  | [optional] [readonly] 
**comments** | [**List[ListInvoiceCommentsAndHistoryResponseCommentsInner]**](ListInvoiceCommentsAndHistoryResponseCommentsInner.md) | Comments made | [optional] 

## Example

```python
from ls_zoho_billing_invoices.models.list_invoice_comments_and_history_response import ListInvoiceCommentsAndHistoryResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListInvoiceCommentsAndHistoryResponse from a JSON string
list_invoice_comments_and_history_response_instance = ListInvoiceCommentsAndHistoryResponse.from_json(json)
# print the JSON string representation of the object
print(ListInvoiceCommentsAndHistoryResponse.to_json())

# convert the object into a dict
list_invoice_comments_and_history_response_dict = list_invoice_comments_and_history_response_instance.to_dict()
# create an instance of ListInvoiceCommentsAndHistoryResponse from a dict
list_invoice_comments_and_history_response_from_dict = ListInvoiceCommentsAndHistoryResponse.from_dict(list_invoice_comments_and_history_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


