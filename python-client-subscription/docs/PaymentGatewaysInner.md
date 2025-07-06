# PaymentGatewaysInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payment_gateway** | **str** | Payment gateway associated with the subscription.Supported payment gateway values &lt;code&gt;test_gateway&lt;/code&gt;, &lt;code&gt;payflow_pro&lt;/code&gt;, &lt;code&gt;stripe&lt;/code&gt;, &lt;code&gt;2checkout&lt;/code&gt;, &lt;code&gt;authorize_net&lt;/code&gt;, &lt;code&gt;payments_pro&lt;/code&gt;, &lt;code&gt;forte&lt;/code&gt;, &lt;code&gt;worldpay&lt;/code&gt;, &lt;code&gt;wepay&lt;/code&gt;. | [optional] 

## Example

```python
from ls_zoho_billing_subscription.models.payment_gateways_inner import PaymentGatewaysInner

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentGatewaysInner from a JSON string
payment_gateways_inner_instance = PaymentGatewaysInner.from_json(json)
# print the JSON string representation of the object
print(PaymentGatewaysInner.to_json())

# convert the object into a dict
payment_gateways_inner_dict = payment_gateways_inner_instance.to_dict()
# create an instance of PaymentGatewaysInner from a dict
payment_gateways_inner_from_dict = PaymentGatewaysInner.from_dict(payment_gateways_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


