# GetPaymentReminderMailContentResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] [readonly] 
**message** | **str** |  | [optional] [readonly] 
**data** | [**GetPaymentReminderMailContentResponseData**](GetPaymentReminderMailContentResponseData.md) |  | [optional] 

## Example

```python
from ls_zoho_billing_invoices.models.get_payment_reminder_mail_content_response import GetPaymentReminderMailContentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetPaymentReminderMailContentResponse from a JSON string
get_payment_reminder_mail_content_response_instance = GetPaymentReminderMailContentResponse.from_json(json)
# print the JSON string representation of the object
print(GetPaymentReminderMailContentResponse.to_json())

# convert the object into a dict
get_payment_reminder_mail_content_response_dict = get_payment_reminder_mail_content_response_instance.to_dict()
# create an instance of GetPaymentReminderMailContentResponse from a dict
get_payment_reminder_mail_content_response_from_dict = GetPaymentReminderMailContentResponse.from_dict(get_payment_reminder_mail_content_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


