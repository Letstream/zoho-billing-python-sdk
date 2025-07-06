# AddChargeResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] [readonly] 
**message** | **str** |  | [optional] [readonly] 
**invoice** | [**AddChargeResponseInvoice**](AddChargeResponseInvoice.md) |  | [optional] 

## Example

```python
from ls_zoho_billing_subscription.models.add_charge_response import AddChargeResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AddChargeResponse from a JSON string
add_charge_response_instance = AddChargeResponse.from_json(json)
# print the JSON string representation of the object
print(AddChargeResponse.to_json())

# convert the object into a dict
add_charge_response_dict = add_charge_response_instance.to_dict()
# create an instance of AddChargeResponse from a dict
add_charge_response_from_dict = AddChargeResponse.from_dict(add_charge_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


