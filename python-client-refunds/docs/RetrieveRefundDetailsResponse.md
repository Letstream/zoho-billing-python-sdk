# RetrieveRefundDetailsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] [readonly] 
**message** | **str** |  | [optional] [readonly] 
**refund** | [**RefundAPaymentResponseRefund**](RefundAPaymentResponseRefund.md) |  | [optional] 

## Example

```python
from ls_zoho_billing_refunds.models.retrieve_refund_details_response import RetrieveRefundDetailsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RetrieveRefundDetailsResponse from a JSON string
retrieve_refund_details_response_instance = RetrieveRefundDetailsResponse.from_json(json)
# print the JSON string representation of the object
print(RetrieveRefundDetailsResponse.to_json())

# convert the object into a dict
retrieve_refund_details_response_dict = retrieve_refund_details_response_instance.to_dict()
# create an instance of RetrieveRefundDetailsResponse from a dict
retrieve_refund_details_response_from_dict = RetrieveRefundDetailsResponse.from_dict(retrieve_refund_details_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


