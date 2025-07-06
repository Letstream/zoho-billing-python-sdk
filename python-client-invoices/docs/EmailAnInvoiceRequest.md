# EmailAnInvoiceRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**to_mail_ids** | **List[str]** | The email IDs to which the invoice is to be mailed. | 
**cc_mail_ids** | **List[str]** | The email IDs that have to be copied when the credit note is to be mailed. | [optional] 
**subject** | **str** | The subject of the email. | 
**body** | **str** | The body of the email. | 

## Example

```python
from ls_zoho_billing_invoices.models.email_an_invoice_request import EmailAnInvoiceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EmailAnInvoiceRequest from a JSON string
email_an_invoice_request_instance = EmailAnInvoiceRequest.from_json(json)
# print the JSON string representation of the object
print(EmailAnInvoiceRequest.to_json())

# convert the object into a dict
email_an_invoice_request_dict = email_an_invoice_request_instance.to_dict()
# create an instance of EmailAnInvoiceRequest from a dict
email_an_invoice_request_from_dict = EmailAnInvoiceRequest.from_dict(email_an_invoice_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


