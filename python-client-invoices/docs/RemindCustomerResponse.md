# RemindCustomerResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] [readonly] 
**message** | **str** |  | [optional] [readonly] 

## Example

```python
from ls_zoho_billing_invoices.models.remind_customer_response import RemindCustomerResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RemindCustomerResponse from a JSON string
remind_customer_response_instance = RemindCustomerResponse.from_json(json)
# print the JSON string representation of the object
print(RemindCustomerResponse.to_json())

# convert the object into a dict
remind_customer_response_dict = remind_customer_response_instance.to_dict()
# create an instance of RemindCustomerResponse from a dict
remind_customer_response_from_dict = RemindCustomerResponse.from_dict(remind_customer_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


