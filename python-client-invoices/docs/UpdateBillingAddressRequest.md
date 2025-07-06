# UpdateBillingAddressRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | Billing address of the customer | [optional] 
**city** | **str** | City of the customer&#39;s billing address | [optional] 
**state** | **str** | State of the customer&#39;s billing address | [optional] 
**zip** | **str** | ZIP code of the contact&#39;s billing address | [optional] 
**country** | **str** | Country of the contact&#39;s billing address | [optional] 
**fax** | **str** | FAX number of the customer | [optional] 

## Example

```python
from ls_zoho_billing_invoices.models.update_billing_address_request import UpdateBillingAddressRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateBillingAddressRequest from a JSON string
update_billing_address_request_instance = UpdateBillingAddressRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateBillingAddressRequest.to_json())

# convert the object into a dict
update_billing_address_request_dict = update_billing_address_request_instance.to_dict()
# create an instance of UpdateBillingAddressRequest from a dict
update_billing_address_request_from_dict = UpdateBillingAddressRequest.from_dict(update_billing_address_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


