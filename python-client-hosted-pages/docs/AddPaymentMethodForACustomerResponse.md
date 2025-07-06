# AddPaymentMethodForACustomerResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] [readonly] 
**message** | **str** |  | [optional] [readonly] 
**hostedpage** | [**AddPaymentMethodForACustomerResponseHostedpage**](AddPaymentMethodForACustomerResponseHostedpage.md) |  | [optional] 

## Example

```python
from ls_zoho_billing_hosted_pages.models.add_payment_method_for_a_customer_response import AddPaymentMethodForACustomerResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AddPaymentMethodForACustomerResponse from a JSON string
add_payment_method_for_a_customer_response_instance = AddPaymentMethodForACustomerResponse.from_json(json)
# print the JSON string representation of the object
print(AddPaymentMethodForACustomerResponse.to_json())

# convert the object into a dict
add_payment_method_for_a_customer_response_dict = add_payment_method_for_a_customer_response_instance.to_dict()
# create an instance of AddPaymentMethodForACustomerResponse from a dict
add_payment_method_for_a_customer_response_from_dict = AddPaymentMethodForACustomerResponse.from_dict(add_payment_method_for_a_customer_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


