# RefundAPaymentRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** | The amount to be refund. | 
**description** | **str** | A small description about the refund. | [optional] 

## Example

```python
from ls_zoho_billing_refunds.models.refund_a_payment_request import RefundAPaymentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RefundAPaymentRequest from a JSON string
refund_a_payment_request_instance = RefundAPaymentRequest.from_json(json)
# print the JSON string representation of the object
print(RefundAPaymentRequest.to_json())

# convert the object into a dict
refund_a_payment_request_dict = refund_a_payment_request_instance.to_dict()
# create an instance of RefundAPaymentRequest from a dict
refund_a_payment_request_from_dict = RefundAPaymentRequest.from_dict(refund_a_payment_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


