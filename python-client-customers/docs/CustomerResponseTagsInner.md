# CustomerResponseTagsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tag_option_id** | **int** | Id of the Tag Option | [optional] 
**is_tag_mandatory** | **str** |  | [optional] 
**tag_name** | **str** |  | [optional] 
**tag_id** | **int** | ID of the Tag | [optional] 
**tag_option_name** | **str** |  | [optional] 

## Example

```python
from ls_zoho_billing_customers.models.customer_response_tags_inner import CustomerResponseTagsInner

# TODO update the JSON string below
json = "{}"
# create an instance of CustomerResponseTagsInner from a JSON string
customer_response_tags_inner_instance = CustomerResponseTagsInner.from_json(json)
# print the JSON string representation of the object
print(CustomerResponseTagsInner.to_json())

# convert the object into a dict
customer_response_tags_inner_dict = customer_response_tags_inner_instance.to_dict()
# create an instance of CustomerResponseTagsInner from a dict
customer_response_tags_inner_from_dict = CustomerResponseTagsInner.from_dict(customer_response_tags_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


