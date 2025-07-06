# GetPaymentReminderMailContentResponseDataEmailtemplatesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**selected** | **bool** | Selected or not | [optional] 
**name** | **str** | Name of the sender | [optional] 
**email_template_id** | **str** | ID of the email template used | [optional] 

## Example

```python
from ls_zoho_billing_invoices.models.get_payment_reminder_mail_content_response_data_emailtemplates_inner import GetPaymentReminderMailContentResponseDataEmailtemplatesInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetPaymentReminderMailContentResponseDataEmailtemplatesInner from a JSON string
get_payment_reminder_mail_content_response_data_emailtemplates_inner_instance = GetPaymentReminderMailContentResponseDataEmailtemplatesInner.from_json(json)
# print the JSON string representation of the object
print(GetPaymentReminderMailContentResponseDataEmailtemplatesInner.to_json())

# convert the object into a dict
get_payment_reminder_mail_content_response_data_emailtemplates_inner_dict = get_payment_reminder_mail_content_response_data_emailtemplates_inner_instance.to_dict()
# create an instance of GetPaymentReminderMailContentResponseDataEmailtemplatesInner from a dict
get_payment_reminder_mail_content_response_data_emailtemplates_inner_from_dict = GetPaymentReminderMailContentResponseDataEmailtemplatesInner.from_dict(get_payment_reminder_mail_content_response_data_emailtemplates_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


