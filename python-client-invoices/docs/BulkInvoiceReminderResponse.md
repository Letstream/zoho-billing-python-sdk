# BulkInvoiceReminderResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] [readonly] 
**message** | **str** |  | [optional] [readonly] 
**info** | [**BulkInvoiceReminderResponseInfo**](BulkInvoiceReminderResponseInfo.md) |  | [optional] 

## Example

```python
from ls_zoho_billing_invoices.models.bulk_invoice_reminder_response import BulkInvoiceReminderResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BulkInvoiceReminderResponse from a JSON string
bulk_invoice_reminder_response_instance = BulkInvoiceReminderResponse.from_json(json)
# print the JSON string representation of the object
print(BulkInvoiceReminderResponse.to_json())

# convert the object into a dict
bulk_invoice_reminder_response_dict = bulk_invoice_reminder_response_instance.to_dict()
# create an instance of BulkInvoiceReminderResponse from a dict
bulk_invoice_reminder_response_from_dict = BulkInvoiceReminderResponse.from_dict(bulk_invoice_reminder_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


