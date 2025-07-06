# CreateAPaymentResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] [readonly] 
**message** | **str** |  | [optional] [readonly] 
**payment** | [**PaymentResponse**](PaymentResponse.md) |  | [optional] 

## Example

```python
from ls_zoho_billing_payments.models.create_a_payment_response import CreateAPaymentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAPaymentResponse from a JSON string
create_a_payment_response_instance = CreateAPaymentResponse.from_json(json)
# print the JSON string representation of the object
print(CreateAPaymentResponse.to_json())

# convert the object into a dict
create_a_payment_response_dict = create_a_payment_response_instance.to_dict()
# create an instance of CreateAPaymentResponse from a dict
create_a_payment_response_from_dict = CreateAPaymentResponse.from_dict(create_a_payment_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


