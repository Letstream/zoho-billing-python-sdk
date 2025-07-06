# DeleteUnbilledChargeResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] [readonly] 
**message** | **str** |  | [optional] [readonly] 

## Example

```python
from ls_zoho_billing_unbilled_charges.models.delete_unbilled_charge_response import DeleteUnbilledChargeResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteUnbilledChargeResponse from a JSON string
delete_unbilled_charge_response_instance = DeleteUnbilledChargeResponse.from_json(json)
# print the JSON string representation of the object
print(DeleteUnbilledChargeResponse.to_json())

# convert the object into a dict
delete_unbilled_charge_response_dict = delete_unbilled_charge_response_instance.to_dict()
# create an instance of DeleteUnbilledChargeResponse from a dict
delete_unbilled_charge_response_from_dict = DeleteUnbilledChargeResponse.from_dict(delete_unbilled_charge_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


