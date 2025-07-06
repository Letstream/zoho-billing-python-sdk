# GetInvoiceEmailContentResponseDataFromEmailsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_name** | **str** | User name of the contact | [optional] 
**selected** | **bool** | To check if invoice is selected or not | [optional] 
**email** | **str** | Email address of the customer. | [optional] 
**organization_contact_id** | **str** | ID of the contact&#39;s organisation | [optional] 
**is_org_email_id** | **bool** | To check if the email ID belongs to the organisation | [optional] 

## Example

```python
from ls_zoho_billing_invoices.models.get_invoice_email_content_response_data_from_emails_inner import GetInvoiceEmailContentResponseDataFromEmailsInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetInvoiceEmailContentResponseDataFromEmailsInner from a JSON string
get_invoice_email_content_response_data_from_emails_inner_instance = GetInvoiceEmailContentResponseDataFromEmailsInner.from_json(json)
# print the JSON string representation of the object
print(GetInvoiceEmailContentResponseDataFromEmailsInner.to_json())

# convert the object into a dict
get_invoice_email_content_response_data_from_emails_inner_dict = get_invoice_email_content_response_data_from_emails_inner_instance.to_dict()
# create an instance of GetInvoiceEmailContentResponseDataFromEmailsInner from a dict
get_invoice_email_content_response_data_from_emails_inner_from_dict = GetInvoiceEmailContentResponseDataFromEmailsInner.from_dict(get_invoice_email_content_response_data_from_emails_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


