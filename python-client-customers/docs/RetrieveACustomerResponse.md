# RetrieveACustomerResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] [readonly] 
**message** | **str** |  | [optional] [readonly] 
**customer** | [**RetrieveACustomerResponseCustomer**](RetrieveACustomerResponseCustomer.md) |  | [optional] 

## Example

```python
from ls_zoho_billing_customers.models.retrieve_a_customer_response import RetrieveACustomerResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RetrieveACustomerResponse from a JSON string
retrieve_a_customer_response_instance = RetrieveACustomerResponse.from_json(json)
# print the JSON string representation of the object
print(RetrieveACustomerResponse.to_json())

# convert the object into a dict
retrieve_a_customer_response_dict = retrieve_a_customer_response_instance.to_dict()
# create an instance of RetrieveACustomerResponse from a dict
retrieve_a_customer_response_from_dict = RetrieveACustomerResponse.from_dict(retrieve_a_customer_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


