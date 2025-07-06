# PaymentGatewaysInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**configured** | **bool** | Boolean check to see if a payment gateway has been configured | [optional] 
**additional_field1** | **str** | Paypal payment method. Allowed Values: &lt;code&gt;standard&lt;/code&gt; and &lt;code&gt;adaptive&lt;/code&gt; | [optional] 
**gateway_name** | **str** | Name of the payment gateway associated with the invoice. E.g. paypal, stripe.Allowed Values: &lt;code&gt;paypal&lt;/code&gt;, &lt;code&gt;authorize_net&lt;/code&gt;, &lt;code&gt;payflow_pro&lt;/code&gt;, &lt;code&gt;stripe&lt;/code&gt;, &lt;code&gt;2checkout&lt;/code&gt; and &lt;code&gt;braintree&lt;/code&gt; | [optional] 

## Example

```python
from ls_zoho_billing_invoices.models.payment_gateways_inner import PaymentGatewaysInner

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


