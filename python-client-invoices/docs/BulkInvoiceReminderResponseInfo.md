# BulkInvoiceReminderResponseInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email_success_info** | [**BulkInvoiceReminderResponseInfoEmailSuccessInfo**](BulkInvoiceReminderResponseInfoEmailSuccessInfo.md) |  | [optional] 
**email_errors_info** | [**List[BulkInvoiceReminderResponseInfoEmailErrorsInfoInner]**](BulkInvoiceReminderResponseInfoEmailErrorsInfoInner.md) | error info | [optional] 
**code** | **int** | Code | [optional] 

## Example

```python
from ls_zoho_billing_invoices.models.bulk_invoice_reminder_response_info import BulkInvoiceReminderResponseInfo

# TODO update the JSON string below
json = "{}"
# create an instance of BulkInvoiceReminderResponseInfo from a JSON string
bulk_invoice_reminder_response_info_instance = BulkInvoiceReminderResponseInfo.from_json(json)
# print the JSON string representation of the object
print(BulkInvoiceReminderResponseInfo.to_json())

# convert the object into a dict
bulk_invoice_reminder_response_info_dict = bulk_invoice_reminder_response_info_instance.to_dict()
# create an instance of BulkInvoiceReminderResponseInfo from a dict
bulk_invoice_reminder_response_info_from_dict = BulkInvoiceReminderResponseInfo.from_dict(bulk_invoice_reminder_response_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


