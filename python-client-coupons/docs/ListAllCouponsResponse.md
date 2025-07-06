# ListAllCouponsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] [readonly] 
**message** | **str** |  | [optional] [readonly] 
**coupons** | [**List[ListAllCouponsResponseCouponsInner]**](ListAllCouponsResponseCouponsInner.md) |  | [optional] 

## Example

```python
from ls_zoho_billing_coupons.models.list_all_coupons_response import ListAllCouponsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListAllCouponsResponse from a JSON string
list_all_coupons_response_instance = ListAllCouponsResponse.from_json(json)
# print the JSON string representation of the object
print(ListAllCouponsResponse.to_json())

# convert the object into a dict
list_all_coupons_response_dict = list_all_coupons_response_instance.to_dict()
# create an instance of ListAllCouponsResponse from a dict
list_all_coupons_response_from_dict = ListAllCouponsResponse.from_dict(list_all_coupons_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


