# UpdateSalesPersonResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] [readonly] 
**message** | **str** |  | [optional] [readonly] 
**subscription** | [**ChangeToOnlineofflineModeResponseSubscription**](ChangeToOnlineofflineModeResponseSubscription.md) |  | [optional] 

## Example

```python
from ls_zoho_billing_subscription.models.update_sales_person_response import UpdateSalesPersonResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateSalesPersonResponse from a JSON string
update_sales_person_response_instance = UpdateSalesPersonResponse.from_json(json)
# print the JSON string representation of the object
print(UpdateSalesPersonResponse.to_json())

# convert the object into a dict
update_sales_person_response_dict = update_sales_person_response_instance.to_dict()
# create an instance of UpdateSalesPersonResponse from a dict
update_sales_person_response_from_dict = UpdateSalesPersonResponse.from_dict(update_sales_person_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


