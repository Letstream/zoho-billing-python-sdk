# RecordInvoicePaymentForASubscriptionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**invoice_id** | **str** | Unique ID generated for an invoice. | 
**redirect_url** | **str** | It specifies the url to which the customer will be redirected after successful transaction. | [optional] 
**hostedpage_settings_id** | **str** | Hostedpage Template ID for the Subscriptions | [optional] 
**payment_gateways** | [**List[PaymentGatewaysInner]**](PaymentGatewaysInner.md) | List of payment gateways configured for the customer. | [optional] 

## Example

```python
from ls_zoho_billing_hosted_pages.models.record_invoice_payment_for_a_subscription_request import RecordInvoicePaymentForASubscriptionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RecordInvoicePaymentForASubscriptionRequest from a JSON string
record_invoice_payment_for_a_subscription_request_instance = RecordInvoicePaymentForASubscriptionRequest.from_json(json)
# print the JSON string representation of the object
print(RecordInvoicePaymentForASubscriptionRequest.to_json())

# convert the object into a dict
record_invoice_payment_for_a_subscription_request_dict = record_invoice_payment_for_a_subscription_request_instance.to_dict()
# create an instance of RecordInvoicePaymentForASubscriptionRequest from a dict
record_invoice_payment_for_a_subscription_request_from_dict = RecordInvoicePaymentForASubscriptionRequest.from_dict(record_invoice_payment_for_a_subscription_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


