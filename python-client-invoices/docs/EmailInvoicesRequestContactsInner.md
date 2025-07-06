# EmailInvoicesRequestContactsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contact_id** | **str** | ID of the contact. Can specify if email or snail mail has to be sent for each contact. | 
**email** | **bool** | The boolean check for email | 
**snail_mail** | **bool** | The boolean check for snail mail | 

## Example

```python
from ls_zoho_billing_invoices.models.email_invoices_request_contacts_inner import EmailInvoicesRequestContactsInner

# TODO update the JSON string below
json = "{}"
# create an instance of EmailInvoicesRequestContactsInner from a JSON string
email_invoices_request_contacts_inner_instance = EmailInvoicesRequestContactsInner.from_json(json)
# print the JSON string representation of the object
print(EmailInvoicesRequestContactsInner.to_json())

# convert the object into a dict
email_invoices_request_contacts_inner_dict = email_invoices_request_contacts_inner_instance.to_dict()
# create an instance of EmailInvoicesRequestContactsInner from a dict
email_invoices_request_contacts_inner_from_dict = EmailInvoicesRequestContactsInner.from_dict(email_invoices_request_contacts_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


