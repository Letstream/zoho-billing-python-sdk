# PaymentGatewaysInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payment_gateway** | **str** | Payment gateway through which payment needs to be made. | [optional] 

## Example

```python
from ls_zoho_billing_hosted_pages.models.payment_gateways_inner import PaymentGatewaysInner

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


