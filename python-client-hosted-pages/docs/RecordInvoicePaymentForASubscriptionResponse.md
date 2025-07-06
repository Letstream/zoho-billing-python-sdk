# RecordInvoicePaymentForASubscriptionResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] [readonly] 
**message** | **str** |  | [optional] [readonly] 
**hostedpage** | [**RecordInvoicePaymentForASubscriptionResponseHostedpage**](RecordInvoicePaymentForASubscriptionResponseHostedpage.md) |  | [optional] 

## Example

```python
from ls_zoho_billing_hosted_pages.models.record_invoice_payment_for_a_subscription_response import RecordInvoicePaymentForASubscriptionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RecordInvoicePaymentForASubscriptionResponse from a JSON string
record_invoice_payment_for_a_subscription_response_instance = RecordInvoicePaymentForASubscriptionResponse.from_json(json)
# print the JSON string representation of the object
print(RecordInvoicePaymentForASubscriptionResponse.to_json())

# convert the object into a dict
record_invoice_payment_for_a_subscription_response_dict = record_invoice_payment_for_a_subscription_response_instance.to_dict()
# create an instance of RecordInvoicePaymentForASubscriptionResponse from a dict
record_invoice_payment_for_a_subscription_response_from_dict = RecordInvoicePaymentForASubscriptionResponse.from_dict(record_invoice_payment_for_a_subscription_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


