# RetrieveAnUnbilledChargeResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] [readonly] 
**message** | **str** |  | [optional] [readonly] 
**unbilled_charge** | [**UnbilledChargeResponse**](UnbilledChargeResponse.md) |  | [optional] 

## Example

```python
from ls_zoho_billing_unbilled_charges.models.retrieve_an_unbilled_charge_response import RetrieveAnUnbilledChargeResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RetrieveAnUnbilledChargeResponse from a JSON string
retrieve_an_unbilled_charge_response_instance = RetrieveAnUnbilledChargeResponse.from_json(json)
# print the JSON string representation of the object
print(RetrieveAnUnbilledChargeResponse.to_json())

# convert the object into a dict
retrieve_an_unbilled_charge_response_dict = retrieve_an_unbilled_charge_response_instance.to_dict()
# create an instance of RetrieveAnUnbilledChargeResponse from a dict
retrieve_an_unbilled_charge_response_from_dict = RetrieveAnUnbilledChargeResponse.from_dict(retrieve_an_unbilled_charge_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


