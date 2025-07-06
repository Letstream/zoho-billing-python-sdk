# CreateACustomerResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] [readonly] 
**message** | **str** |  | [optional] [readonly] 
**customer** | [**CustomerResponse**](CustomerResponse.md) |  | [optional] 

## Example

```python
from ls_zoho_billing_customers.models.create_a_customer_response import CreateACustomerResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateACustomerResponse from a JSON string
create_a_customer_response_instance = CreateACustomerResponse.from_json(json)
# print the JSON string representation of the object
print(CreateACustomerResponse.to_json())

# convert the object into a dict
create_a_customer_response_dict = create_a_customer_response_instance.to_dict()
# create an instance of CreateACustomerResponse from a dict
create_a_customer_response_from_dict = CreateACustomerResponse.from_dict(create_a_customer_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


