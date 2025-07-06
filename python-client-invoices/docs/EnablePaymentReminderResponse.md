# EnablePaymentReminderResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] [readonly] 
**message** | **str** |  | [optional] [readonly] 

## Example

```python
from ls_zoho_billing_invoices.models.enable_payment_reminder_response import EnablePaymentReminderResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EnablePaymentReminderResponse from a JSON string
enable_payment_reminder_response_instance = EnablePaymentReminderResponse.from_json(json)
# print the JSON string representation of the object
print(EnablePaymentReminderResponse.to_json())

# convert the object into a dict
enable_payment_reminder_response_dict = enable_payment_reminder_response_instance.to_dict()
# create an instance of EnablePaymentReminderResponse from a dict
enable_payment_reminder_response_from_dict = EnablePaymentReminderResponse.from_dict(enable_payment_reminder_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


