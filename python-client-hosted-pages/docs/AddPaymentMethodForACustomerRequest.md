# AddPaymentMethodForACustomerRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer_id** | **str** | Customer ID of the customer for whom a subscription needs to be created | 
**redirect_url** | **str** | It specifies the url to which the customer will be redirected after successful transaction. | [optional] 
**payment_gateways** | [**List[PaymentGatewaysInner]**](PaymentGatewaysInner.md) | List of payment gateways configured for the customer. | [optional] 

## Example

```python
from ls_zoho_billing_hosted_pages.models.add_payment_method_for_a_customer_request import AddPaymentMethodForACustomerRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AddPaymentMethodForACustomerRequest from a JSON string
add_payment_method_for_a_customer_request_instance = AddPaymentMethodForACustomerRequest.from_json(json)
# print the JSON string representation of the object
print(AddPaymentMethodForACustomerRequest.to_json())

# convert the object into a dict
add_payment_method_for_a_customer_request_dict = add_payment_method_for_a_customer_request_instance.to_dict()
# create an instance of AddPaymentMethodForACustomerRequest from a dict
add_payment_method_for_a_customer_request_from_dict = AddPaymentMethodForACustomerRequest.from_dict(add_payment_method_for_a_customer_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


