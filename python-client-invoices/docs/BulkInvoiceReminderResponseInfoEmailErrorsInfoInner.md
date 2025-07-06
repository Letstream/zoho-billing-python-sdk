# BulkInvoiceReminderResponseInfoEmailErrorsInfoInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Alert Message | [optional] 
**ids** | **List[str]** | ID&#39;s of mails sent | [optional] 

## Example

```python
from ls_zoho_billing_invoices.models.bulk_invoice_reminder_response_info_email_errors_info_inner import BulkInvoiceReminderResponseInfoEmailErrorsInfoInner

# TODO update the JSON string below
json = "{}"
# create an instance of BulkInvoiceReminderResponseInfoEmailErrorsInfoInner from a JSON string
bulk_invoice_reminder_response_info_email_errors_info_inner_instance = BulkInvoiceReminderResponseInfoEmailErrorsInfoInner.from_json(json)
# print the JSON string representation of the object
print(BulkInvoiceReminderResponseInfoEmailErrorsInfoInner.to_json())

# convert the object into a dict
bulk_invoice_reminder_response_info_email_errors_info_inner_dict = bulk_invoice_reminder_response_info_email_errors_info_inner_instance.to_dict()
# create an instance of BulkInvoiceReminderResponseInfoEmailErrorsInfoInner from a dict
bulk_invoice_reminder_response_info_email_errors_info_inner_from_dict = BulkInvoiceReminderResponseInfoEmailErrorsInfoInner.from_dict(bulk_invoice_reminder_response_info_email_errors_info_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


