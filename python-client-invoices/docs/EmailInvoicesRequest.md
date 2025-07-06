# EmailInvoicesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contacts** | [**List[EmailInvoicesRequestContactsInner]**](EmailInvoicesRequestContactsInner.md) | Contacts to whom email or snail mail has to be sent. | 

## Example

```python
from ls_zoho_billing_invoices.models.email_invoices_request import EmailInvoicesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EmailInvoicesRequest from a JSON string
email_invoices_request_instance = EmailInvoicesRequest.from_json(json)
# print the JSON string representation of the object
print(EmailInvoicesRequest.to_json())

# convert the object into a dict
email_invoices_request_dict = email_invoices_request_instance.to_dict()
# create an instance of EmailInvoicesRequest from a dict
email_invoices_request_from_dict = EmailInvoicesRequest.from_dict(email_invoices_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


