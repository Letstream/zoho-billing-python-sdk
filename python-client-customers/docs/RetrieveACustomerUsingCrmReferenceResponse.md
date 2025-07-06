# RetrieveACustomerUsingCrmReferenceResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] [readonly] 
**message** | **str** |  | [optional] [readonly] 
**customer** | [**RetrieveACustomerUsingCrmReferenceResponseCustomer**](RetrieveACustomerUsingCrmReferenceResponseCustomer.md) |  | [optional] 

## Example

```python
from ls_zoho_billing_customers.models.retrieve_a_customer_using_crm_reference_response import RetrieveACustomerUsingCrmReferenceResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RetrieveACustomerUsingCrmReferenceResponse from a JSON string
retrieve_a_customer_using_crm_reference_response_instance = RetrieveACustomerUsingCrmReferenceResponse.from_json(json)
# print the JSON string representation of the object
print(RetrieveACustomerUsingCrmReferenceResponse.to_json())

# convert the object into a dict
retrieve_a_customer_using_crm_reference_response_dict = retrieve_a_customer_using_crm_reference_response_instance.to_dict()
# create an instance of RetrieveACustomerUsingCrmReferenceResponse from a dict
retrieve_a_customer_using_crm_reference_response_from_dict = RetrieveACustomerUsingCrmReferenceResponse.from_dict(retrieve_a_customer_using_crm_reference_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


