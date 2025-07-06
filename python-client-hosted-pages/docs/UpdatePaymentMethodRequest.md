# UpdatePaymentMethodRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**card_id** | **str** | Card number associated to the customer. | 
**account_id** | **str** | Bank account number associated to the customer for ACH payments. | 
**paypal_id** | **str** | PayPal account number associated to the customer. | 

## Example

```python
from ls_zoho_billing_hosted_pages.models.update_payment_method_request import UpdatePaymentMethodRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdatePaymentMethodRequest from a JSON string
update_payment_method_request_instance = UpdatePaymentMethodRequest.from_json(json)
# print the JSON string representation of the object
print(UpdatePaymentMethodRequest.to_json())

# convert the object into a dict
update_payment_method_request_dict = update_payment_method_request_instance.to_dict()
# create an instance of UpdatePaymentMethodRequest from a dict
update_payment_method_request_from_dict = UpdatePaymentMethodRequest.from_dict(update_payment_method_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


