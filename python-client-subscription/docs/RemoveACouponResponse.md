# RemoveACouponResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] [readonly] 
**message** | **str** |  | [optional] [readonly] 

## Example

```python
from ls_zoho_billing_subscription.models.remove_a_coupon_response import RemoveACouponResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RemoveACouponResponse from a JSON string
remove_a_coupon_response_instance = RemoveACouponResponse.from_json(json)
# print the JSON string representation of the object
print(RemoveACouponResponse.to_json())

# convert the object into a dict
remove_a_coupon_response_dict = remove_a_coupon_response_instance.to_dict()
# create an instance of RemoveACouponResponse from a dict
remove_a_coupon_response_from_dict = RemoveACouponResponse.from_dict(remove_a_coupon_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


