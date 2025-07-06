# ListInvoicesResponseInvoicesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**invoice_id** | **str** | Unique ID generated for an invoice. | [optional] 
**ach_payment_initiated** | **bool** | Set to true if ACH payment is initiated. | [optional] 
**customer_name** | **str** | Name of the customer to whom the invoice is raised. | [optional] 
**customer_id** | **str** | Customer ID of the customer to whom the invoice is raised. | [optional] 
**status** | **str** | Status of the invoice. It can be &lt;code&gt;paid&lt;/code&gt;, &lt;code&gt;sent&lt;/code&gt;, &lt;code&gt;overdue&lt;/code&gt;, &lt;code&gt;partially_paid&lt;/code&gt; or &lt;code&gt;void&lt;/code&gt;. | [optional] 
**invoice_number** | **str** | Unique ID (starts with INV) of an invoice. | [optional] 
**reference_number** | **str** | Reference number of the invoice for which payment is made. | [optional] 
**var_date** | **str** | Date on which the invoice is paid. | [optional] 
**due_date** | **str** | Date on which the invoice is due. If the invoice is not fully paid on or before this date, the status of the invoice will be changed to &lt;code&gt;overdue&lt;/code&gt;. If the invoice is only partially paid, its status will be &lt;code&gt;partially_paid&lt;/code&gt;. | [optional] 
**due_days** | **str** | Specifies the number of day in which the invoice would become overdue | [optional] 
**currency_id** | **str** | The currenct id of the currency | [optional] 
**schedule_time** | **str** | Schedule time for payment | [optional] 
**currency_code** | **str** | The customer&#39;s currency code. | [optional] 
**is_viewed_by_client** | **bool** | Check if invoice is viewed by client | [optional] 
**has_attachment** | **object** | Denotes whether a customer has any attachments associated with it. | [optional] 
**client_viewed_time** | **str** | Time when client viewed the statement | [optional] 
**total** | **float** | Total amount to be paid for the invoice. This would be the sum of individual costs of all items involved in the invoice. Total is determined only after customer credits (if any) are applied. | [optional] 
**balance** | **float** | The unpaid amount of an invoice. | [optional] 
**created_time** | **str** | Time when the invoice was created. | [optional] 
**last_modified_time** | **str** | Date of last modification of the invoice | [optional] 
**is_emailed** | **bool** | Boolean check to see if the mail has been sent | [optional] 
**reminders_sent** | **int** | The number of reminders sent | [optional] 
**last_reminder_sent_date** | **str** | The date the last email was sent | [optional] 
**payment_expected_date** | **str** | A date to specify the expected payment date. | [optional] 
**last_payment_date** | **str** | The last payment date of the invoice | [optional] 
**custom_fields** | **List[str]** | Additional fields for the invoices. | [optional] 
**documents** | [**List[DocumentsInner]**](DocumentsInner.md) | List of files attached to a particular customer. | [optional] 
**salesperson_id** | **str** | Unique Id to denote the sales person. | [optional] 
**salesperson_name** | **str** | Name of the sales person associated with the invoice for offline payments. | [optional] 
**shipping_charge** | **str** | Shipping charges applied to the invoice. &lt;code&gt;Maximum length [100]&lt;/code&gt; | [optional] 
**adjustment** | **float** | Adjustments made to the invoice. | [optional] 
**write_off_amount** | **float** | The unpaid amount of an invoice that is written off. | [optional] 
**exchange_rate** | **float** | Exchange-Rate for the currency. | [optional] 

## Example

```python
from ls_zoho_billing_invoices.models.list_invoices_response_invoices_inner import ListInvoicesResponseInvoicesInner

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


