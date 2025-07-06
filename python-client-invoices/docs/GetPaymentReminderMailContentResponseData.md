# GetPaymentReminderMailContentResponseData

Date of the email

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bcc_mails** | **List[str]** | Bcc mail details | [optional] 
**gateways_configured** | **bool** | List of payment gateways configured | [optional] 
**gateways_associated** | **bool** | List of Payment gateways associated | [optional] 
**bcc_mails_str** | **str** | Bcc mails content | [optional] 
**body** | **str** | content of email sent | [optional] 
**documents** | [**List[DocumentsInner]**](DocumentsInner.md) | List of files attached to a particular customer. | [optional] 
**customer_name** | **str** | Name of the customer to whom the invoice is raised. | [optional] 
**attach_pdf** | **bool** | check if PDF attachment | [optional] 
**entity_id** | **str** | Unique ID of the entity associated | [optional] 
**cc_mails_list** | [**List[GetInvoiceEmailContentResponseDataCcMailsListInner]**](GetInvoiceEmailContentResponseDataCcMailsListInner.md) | CC&#39;d mail recepients | [optional] 
**file_name_without_extension** | **str** | Name of file included | [optional] 
**to_mails_str** | **str** | Mail recepients | [optional] 
**cc_mails_str** | **str** | Mail recepients who need to be CC&#39;d | [optional] 
**from_email** | **str** | Mail sender | [optional] 
**from_address** | **str** | Sender&#39;s email address | [optional] 
**deprecated_placeholders_used** | **List[str]** | List of placeholders used in invoice | [optional] 
**error_list** | **List[str]** | Error List | [optional] 
**subject** | **str** | The subject of the email. | [optional] 
**emailtemplates** | [**List[GetPaymentReminderMailContentResponseDataEmailtemplatesInner]**](GetPaymentReminderMailContentResponseDataEmailtemplatesInner.md) | Email templates used | [optional] 
**emailtemplate_documents** | **List[str]** | Email templates used | [optional] 
**to_contacts** | [**List[GetInvoiceEmailContentResponseDataToContactsInner]**](GetInvoiceEmailContentResponseDataToContactsInner.md) | Recepienyts pf the mail | [optional] 
**attachment_name** | **str** | Name of the file attached | [optional] 
**file_name** | **object** | Name of the attached file. | [optional] 
**from_emails** | [**List[GetInvoiceEmailContentResponseDataFromEmailsInner]**](GetInvoiceEmailContentResponseDataFromEmailsInner.md) | senders email address | [optional] 
**customer_id** | **str** | Customer ID of the customer to whom the invoice is raised. | [optional] 

## Example

```python
from ls_zoho_billing_invoices.models.get_payment_reminder_mail_content_response_data import GetPaymentReminderMailContentResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of GetPaymentReminderMailContentResponseData from a JSON string
get_payment_reminder_mail_content_response_data_instance = GetPaymentReminderMailContentResponseData.from_json(json)
# print the JSON string representation of the object
print(GetPaymentReminderMailContentResponseData.to_json())

# convert the object into a dict
get_payment_reminder_mail_content_response_data_dict = get_payment_reminder_mail_content_response_data_instance.to_dict()
# create an instance of GetPaymentReminderMailContentResponseData from a dict
get_payment_reminder_mail_content_response_data_from_dict = GetPaymentReminderMailContentResponseData.from_dict(get_payment_reminder_mail_content_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


