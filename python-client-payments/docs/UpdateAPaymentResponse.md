# UpdateAPaymentResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] [readonly] 
**message** | **str** |  | [optional] [readonly] 
**payment** | [**RetrieveAPaymentResponsePayment**](RetrieveAPaymentResponsePayment.md) |  | [optional] 

## Example

```python
from ls_zoho_billing_payments.models.update_a_payment_response import UpdateAPaymentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateAPaymentResponse from a JSON string
update_a_payment_response_instance = UpdateAPaymentResponse.from_json(json)
# print the JSON string representation of the object
print(UpdateAPaymentResponse.to_json())

# convert the object into a dict
update_a_payment_response_dict = update_a_payment_response_instance.to_dict()
# create an instance of UpdateAPaymentResponse from a dict
update_a_payment_response_from_dict = UpdateAPaymentResponse.from_dict(update_a_payment_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


