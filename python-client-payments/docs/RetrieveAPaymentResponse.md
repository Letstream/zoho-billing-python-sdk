# RetrieveAPaymentResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] [readonly] 
**message** | **str** |  | [optional] [readonly] 
**payment** | [**RetrieveAPaymentResponsePayment**](RetrieveAPaymentResponsePayment.md) |  | [optional] 

## Example

```python
from ls_zoho_billing_payments.models.retrieve_a_payment_response import RetrieveAPaymentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RetrieveAPaymentResponse from a JSON string
retrieve_a_payment_response_instance = RetrieveAPaymentResponse.from_json(json)
# print the JSON string representation of the object
print(RetrieveAPaymentResponse.to_json())

# convert the object into a dict
retrieve_a_payment_response_dict = retrieve_a_payment_response_instance.to_dict()
# create an instance of RetrieveAPaymentResponse from a dict
retrieve_a_payment_response_from_dict = RetrieveAPaymentResponse.from_dict(retrieve_a_payment_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


