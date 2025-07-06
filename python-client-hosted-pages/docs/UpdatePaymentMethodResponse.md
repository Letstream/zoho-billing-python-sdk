# UpdatePaymentMethodResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] [readonly] 
**message** | **str** |  | [optional] [readonly] 
**hostedpage** | [**UpdatePaymentMethodResponseHostedpage**](UpdatePaymentMethodResponseHostedpage.md) |  | [optional] 

## Example

```python
from ls_zoho_billing_hosted_pages.models.update_payment_method_response import UpdatePaymentMethodResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UpdatePaymentMethodResponse from a JSON string
update_payment_method_response_instance = UpdatePaymentMethodResponse.from_json(json)
# print the JSON string representation of the object
print(UpdatePaymentMethodResponse.to_json())

# convert the object into a dict
update_payment_method_response_dict = update_payment_method_response_instance.to_dict()
# create an instance of UpdatePaymentMethodResponse from a dict
update_payment_method_response_from_dict = UpdatePaymentMethodResponse.from_dict(update_payment_method_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


