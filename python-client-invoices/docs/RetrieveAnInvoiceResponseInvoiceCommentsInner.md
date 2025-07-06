# RetrieveAnInvoiceResponseInvoiceCommentsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comment_id** | **str** | Unique Id to denote the comment fro the particular invoice. | [optional] 
**description** | **object** | Small description about the comment. | [optional] 
**commented_by_id** | **str** | Unique Id to denote who has commented. | [optional] 
**commented_by** | **str** | It denotes the name of the user who has commented or the system. | [optional] 
**comment_type** | **str** | It denotes whether user comment or system comment. | [optional] 
**var_date** | **object** | Date on which the comment was created. | [optional] 
**time** | **str** | Denotes the time at which the comment was created. | [optional] 
**operation_type** | **str** | It denotes the type of operation performed on invoice. | [optional] 
**transaction_id** | **str** | Unique which denotes the type of transaction. | [optional] 
**transaction_type** | **object** | Small description about the type of transaction. | [optional] 

## Example

```python
from ls_zoho_billing_invoices.models.retrieve_an_invoice_response_invoice_comments_inner import RetrieveAnInvoiceResponseInvoiceCommentsInner

# TODO update the JSON string below
json = "{}"
# create an instance of RetrieveAnInvoiceResponseInvoiceCommentsInner from a JSON string
retrieve_an_invoice_response_invoice_comments_inner_instance = RetrieveAnInvoiceResponseInvoiceCommentsInner.from_json(json)
# print the JSON string representation of the object
print(RetrieveAnInvoiceResponseInvoiceCommentsInner.to_json())

# convert the object into a dict
retrieve_an_invoice_response_invoice_comments_inner_dict = retrieve_an_invoice_response_invoice_comments_inner_instance.to_dict()
# create an instance of RetrieveAnInvoiceResponseInvoiceCommentsInner from a dict
retrieve_an_invoice_response_invoice_comments_inner_from_dict = RetrieveAnInvoiceResponseInvoiceCommentsInner.from_dict(retrieve_an_invoice_response_invoice_comments_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


