# DisablePaymentReminderResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] [readonly] 
**message** | **str** |  | [optional] [readonly] 

## Example

```python
from ls_zoho_billing_invoices.models.disable_payment_reminder_response import DisablePaymentReminderResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DisablePaymentReminderResponse from a JSON string
disable_payment_reminder_response_instance = DisablePaymentReminderResponse.from_json(json)
# print the JSON string representation of the object
print(DisablePaymentReminderResponse.to_json())

# convert the object into a dict
disable_payment_reminder_response_dict = disable_payment_reminder_response_instance.to_dict()
# create an instance of DisablePaymentReminderResponse from a dict
disable_payment_reminder_response_from_dict = DisablePaymentReminderResponse.from_dict(disable_payment_reminder_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


