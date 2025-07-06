# ListAllInvoicesResponseInvoicesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**invoice_id** | **str** | Unique ID generated for an invoice. | [optional] 
**number** | **str** | Unique invoice number (starts with INV) generated for an invoice which will be used to display in interface and invoices. | [optional] 
**status** | **str** | Status of the invoice. It can be &lt;code&gt;paid&lt;/code&gt;, &lt;code&gt;sent&lt;/code&gt;, &lt;code&gt;overdue&lt;/code&gt;, &lt;code&gt;partially_paid&lt;/code&gt; or &lt;code&gt;void&lt;/code&gt;. | [optional] 
**invoice_date** | **str** | The date on which the invoice is raised. | [optional] 
**due_date** | **str** | Date on which the invoice is due. If the invoice is not fully paid on or before this date, the status of the invoice will be changed to &lt;code&gt;overdue&lt;/code&gt;. If the invoice is only partially paid, its status will be &lt;code&gt;partially_paid&lt;/code&gt;. | [optional] 
**customer_id** | **str** | Customer ID of the customer to whom the invoice is raised. | [optional] 
**customer_name** | **str** | Name of the customer to whom the invoice is raised. | [optional] 
**email** | **str** | Email address of the customer. | [optional] 
**balance** | **float** | The unpaid amount of an invoice. | [optional] 
**total** | **float** | Total amount to be paid for the invoice. This would be the sum of individual costs of all items involved in the invoice. Total is determined only after customer credits (if any) are applied. | [optional] 
**currency_code** | **str** | The customer&#39;s currency code. | [optional] 
**currency_symbol** | **str** | The customer&#39;s currency symbol. | [optional] 
**has_attachment** | **object** | Denotes whether a customer has any attachments associated with it. | [optional] 
**created_time** | **str** | Time when the invoice was created. | [optional] 
**updated_time** | **str** | Time when the invoice details were last updated. | [optional] 

## Example

```python
from ls_zoho_billing_invoices.models.list_all_invoices_response_invoices_inner import ListAllInvoicesResponseInvoicesInner

# TODO update the JSON string below
json = "{}"
# create an instance of ListAllInvoicesResponseInvoicesInner from a JSON string
list_all_invoices_response_invoices_inner_instance = ListAllInvoicesResponseInvoicesInner.from_json(json)
# print the JSON string representation of the object
print(ListAllInvoicesResponseInvoicesInner.to_json())

# convert the object into a dict
list_all_invoices_response_invoices_inner_dict = list_all_invoices_response_invoices_inner_instance.to_dict()
# create an instance of ListAllInvoicesResponseInvoicesInner from a dict
list_all_invoices_response_invoices_inner_from_dict = ListAllInvoicesResponseInvoicesInner.from_dict(list_all_invoices_response_invoices_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


