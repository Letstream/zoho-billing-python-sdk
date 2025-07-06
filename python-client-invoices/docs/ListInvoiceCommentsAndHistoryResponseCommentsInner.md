# ListInvoiceCommentsAndHistoryResponseCommentsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comment_id** | **str** | The ID of the comment | [optional] 
**invoice_id** | **str** | Unique ID generated for an invoice. | [optional] 
**description** | **str** | Small description of the payment made for the invoice. | [optional] 
**commented_by_id** | **str** | ID of comment made | [optional] 
**commented_by** | **str** | User who added comment | [optional] 
**comment_type** | **str** | type of comment made | [optional] 
**operation_type** | **str** | Tyoe of operation done on invoice | [optional] 
**var_date** | **str** | Date of transaction | [optional] 
**date_description** | **str** | Date of description | [optional] 
**time** | **str** | Time of comment | [optional] 
**transaction_id** | **str** | Unique ID of transaction made | [optional] 
**transaction_type** | **str** | Type of transaction | [optional] 

## Example

```python
from ls_zoho_billing_invoices.models.list_invoice_comments_and_history_response_comments_inner import ListInvoiceCommentsAndHistoryResponseCommentsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ListInvoiceCommentsAndHistoryResponseCommentsInner from a JSON string
list_invoice_comments_and_history_response_comments_inner_instance = ListInvoiceCommentsAndHistoryResponseCommentsInner.from_json(json)
# print the JSON string representation of the object
print(ListInvoiceCommentsAndHistoryResponseCommentsInner.to_json())

# convert the object into a dict
list_invoice_comments_and_history_response_comments_inner_dict = list_invoice_comments_and_history_response_comments_inner_instance.to_dict()
# create an instance of ListInvoiceCommentsAndHistoryResponseCommentsInner from a dict
list_invoice_comments_and_history_response_comments_inner_from_dict = ListInvoiceCommentsAndHistoryResponseCommentsInner.from_dict(list_invoice_comments_and_history_response_comments_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


