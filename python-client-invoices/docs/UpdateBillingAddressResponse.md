# UpdateBillingAddressResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] [readonly] 
**message** | **str** |  | [optional] [readonly] 

## Example

```python
from ls_zoho_billing_invoices.models.update_billing_address_response import UpdateBillingAddressResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateBillingAddressResponse from a JSON string
update_billing_address_response_instance = UpdateBillingAddressResponse.from_json(json)
# print the JSON string representation of the object
print(UpdateBillingAddressResponse.to_json())

# convert the object into a dict
update_billing_address_response_dict = update_billing_address_response_instance.to_dict()
# create an instance of UpdateBillingAddressResponse from a dict
update_billing_address_response_from_dict = UpdateBillingAddressResponse.from_dict(update_billing_address_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


