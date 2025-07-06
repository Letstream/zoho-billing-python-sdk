# RefundAPaymentResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] [readonly] 
**message** | **str** |  | [optional] [readonly] 
**refund** | [**RefundAPaymentResponseRefund**](RefundAPaymentResponseRefund.md) |  | [optional] 

## Example

```python
from ls_zoho_billing_refunds.models.refund_a_payment_response import RefundAPaymentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RefundAPaymentResponse from a JSON string
refund_a_payment_response_instance = RefundAPaymentResponse.from_json(json)
# print the JSON string representation of the object
print(RefundAPaymentResponse.to_json())

# convert the object into a dict
refund_a_payment_response_dict = refund_a_payment_response_instance.to_dict()
# create an instance of RefundAPaymentResponse from a dict
refund_a_payment_response_from_dict = RefundAPaymentResponse.from_dict(refund_a_payment_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


