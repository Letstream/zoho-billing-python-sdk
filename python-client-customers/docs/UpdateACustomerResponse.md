# UpdateACustomerResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] [readonly] 
**message** | **str** |  | [optional] [readonly] 
**customer** | [**UpdateACustomerResponseCustomer**](UpdateACustomerResponseCustomer.md) |  | [optional] 

## Example

```python
from ls_zoho_billing_customers.models.update_a_customer_response import UpdateACustomerResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateACustomerResponse from a JSON string
update_a_customer_response_instance = UpdateACustomerResponse.from_json(json)
# print the JSON string representation of the object
print(UpdateACustomerResponse.to_json())

# convert the object into a dict
update_a_customer_response_dict = update_a_customer_response_instance.to_dict()
# create an instance of UpdateACustomerResponse from a dict
update_a_customer_response_from_dict = UpdateACustomerResponse.from_dict(update_a_customer_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


