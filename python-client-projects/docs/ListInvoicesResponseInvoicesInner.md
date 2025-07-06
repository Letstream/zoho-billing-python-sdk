# ListInvoicesResponseInvoicesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**invoice_id** | **str** | ID of the invoice generated for the project | [optional] 
**customer_name** | **str** | Name of the client of the project | [optional] 
**status** | **str** | Project Status | [optional] 
**invoice_number** | **str** | Serial Number of the invoice | [optional] 
**reference_number** | **str** | Refernce number of a transaction | [optional] 
**var_date** | **str** | Date of the comment | [optional] 
**due_date** | **str** | Due date for project completion | [optional] 
**total** | **str** | Total invoice amount | [optional] 
**balance** | **str** | Balance, in case invoice is partially paid | [optional] 
**created_time** | **str** | Time of project creation | [optional] 

## Example

```python
from ls_zoho_billing_projects.models.list_invoices_response_invoices_inner import ListInvoicesResponseInvoicesInner

# TODO update the JSON string below
json = "{}"
# create an instance of ListInvoicesResponseInvoicesInner from a JSON string
list_invoices_response_invoices_inner_instance = ListInvoicesResponseInvoicesInner.from_json(json)
# print the JSON string representation of the object
print(ListInvoicesResponseInvoicesInner.to_json())

# convert the object into a dict
list_invoices_response_invoices_inner_dict = list_invoices_response_invoices_inner_instance.to_dict()
# create an instance of ListInvoicesResponseInvoicesInner from a dict
list_invoices_response_invoices_inner_from_dict = ListInvoicesResponseInvoicesInner.from_dict(list_invoices_response_invoices_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


