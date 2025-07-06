# BulkInvoiceReminderResponseInfoEmailSuccessInfo

Information on success of email delivery

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Alert Message | [optional] 
**sent_count** | **int** | Number of email s sent | [optional] 

## Example

```python
from ls_zoho_billing_invoices.models.bulk_invoice_reminder_response_info_email_success_info import BulkInvoiceReminderResponseInfoEmailSuccessInfo

# TODO update the JSON string below
json = "{}"
# create an instance of BulkInvoiceReminderResponseInfoEmailSuccessInfo from a JSON string
bulk_invoice_reminder_response_info_email_success_info_instance = BulkInvoiceReminderResponseInfoEmailSuccessInfo.from_json(json)
# print the JSON string representation of the object
print(BulkInvoiceReminderResponseInfoEmailSuccessInfo.to_json())

# convert the object into a dict
bulk_invoice_reminder_response_info_email_success_info_dict = bulk_invoice_reminder_response_info_email_success_info_instance.to_dict()
# create an instance of BulkInvoiceReminderResponseInfoEmailSuccessInfo from a dict
bulk_invoice_reminder_response_info_email_success_info_from_dict = BulkInvoiceReminderResponseInfoEmailSuccessInfo.from_dict(bulk_invoice_reminder_response_info_email_success_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


