# AssociateACouponResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] [readonly] 
**message** | **str** |  | [optional] [readonly] 

## Example

```python
from ls_zoho_billing_subscription.models.associate_a_coupon_response import AssociateACouponResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AssociateACouponResponse from a JSON string
associate_a_coupon_response_instance = AssociateACouponResponse.from_json(json)
# print the JSON string representation of the object
print(AssociateACouponResponse.to_json())

# convert the object into a dict
associate_a_coupon_response_dict = associate_a_coupon_response_instance.to_dict()
# create an instance of AssociateACouponResponse from a dict
associate_a_coupon_response_from_dict = AssociateACouponResponse.from_dict(associate_a_coupon_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


