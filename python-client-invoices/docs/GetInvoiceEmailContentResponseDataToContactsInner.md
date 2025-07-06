# GetInvoiceEmailContentResponseDataToContactsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first_name** | **str** | First name of the contact | [optional] 
**selected** | **bool** | To check if invoice is selected or not | [optional] 
**phone** | **str** | Phone number of the contact | [optional] 
**email** | **str** | Email address of the customer. | [optional] 
**last_name** | **str** | Last name of the contact | [optional] 
**salutation** | **str** | Salutation to the contact | [optional] 
**contact_person_id** | **str** | Unique ID of the contact person. | [optional] 
**mobile** | **str** | Mobile number of the contact person | [optional] 

## Example

```python
from ls_zoho_billing_invoices.models.get_invoice_email_content_response_data_to_contacts_inner import GetInvoiceEmailContentResponseDataToContactsInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetInvoiceEmailContentResponseDataToContactsInner from a JSON string
get_invoice_email_content_response_data_to_contacts_inner_instance = GetInvoiceEmailContentResponseDataToContactsInner.from_json(json)
# print the JSON string representation of the object
print(GetInvoiceEmailContentResponseDataToContactsInner.to_json())

# convert the object into a dict
get_invoice_email_content_response_data_to_contacts_inner_dict = get_invoice_email_content_response_data_to_contacts_inner_instance.to_dict()
# create an instance of GetInvoiceEmailContentResponseDataToContactsInner from a dict
get_invoice_email_content_response_data_to_contacts_inner_from_dict = GetInvoiceEmailContentResponseDataToContactsInner.from_dict(get_invoice_email_content_response_data_to_contacts_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


