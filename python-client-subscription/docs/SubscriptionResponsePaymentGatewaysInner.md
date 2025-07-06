# SubscriptionResponsePaymentGatewaysInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payment_gateway** | **object** | Payment gateway associated with the subscription.Supported payment gateway values &lt;code&gt;test_gateway&lt;/code&gt;, &lt;code&gt;payflow_pro&lt;/code&gt;, &lt;code&gt;stripe&lt;/code&gt;, &lt;code&gt;2checkout&lt;/code&gt;, &lt;code&gt;authorize_net&lt;/code&gt;, &lt;code&gt;payments_pro&lt;/code&gt;, &lt;code&gt;forte&lt;/code&gt;, &lt;code&gt;worldpay&lt;/code&gt;, &lt;code&gt;wepay&lt;/code&gt;. | [optional] 

## Example

```python
from ls_zoho_billing_subscription.models.subscription_response_payment_gateways_inner import SubscriptionResponsePaymentGatewaysInner

# TODO update the JSON string below
json = "{}"
# create an instance of SubscriptionResponsePaymentGatewaysInner from a JSON string
subscription_response_payment_gateways_inner_instance = SubscriptionResponsePaymentGatewaysInner.from_json(json)
# print the JSON string representation of the object
print(SubscriptionResponsePaymentGatewaysInner.to_json())

# convert the object into a dict
subscription_response_payment_gateways_inner_dict = subscription_response_payment_gateways_inner_instance.to_dict()
# create an instance of SubscriptionResponsePaymentGatewaysInner from a dict
subscription_response_payment_gateways_inner_from_dict = SubscriptionResponsePaymentGatewaysInner.from_dict(subscription_response_payment_gateways_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


