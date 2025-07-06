# AddChargeRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** | The amount that needs to be charged for the subscription. | 
**description** | **object** | Make a note of why the customer was charged so that if can be used for any future reference. | [optional] 
**tags** | [**List[TagsInner]**](TagsInner.md) |  | [optional] 
**item_custom_fields** | [**List[ItemCustomFieldsInner]**](ItemCustomFieldsInner.md) | Custom fields for a item. | [optional] 
**account_id** | **str** | Account ID which the add charge is associated. | [optional] 
**add_to_unbilled_charges** | **bool** | When the value is given as true, the charges will be put as unbilled. If the subscription already has unbilled-charges, this will be added as another line item to it. The unbilled charge can be converted to invoice at any later point of time. | [optional] 

## Example

```python
from ls_zoho_billing_subscription.models.add_charge_request import AddChargeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AddChargeRequest from a JSON string
add_charge_request_instance = AddChargeRequest.from_json(json)
# print the JSON string representation of the object
print(AddChargeRequest.to_json())

# convert the object into a dict
add_charge_request_dict = add_charge_request_instance.to_dict()
# create an instance of AddChargeRequest from a dict
add_charge_request_from_dict = AddChargeRequest.from_dict(add_charge_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


