# DeleteAProductResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] [readonly] 
**message** | **str** |  | [optional] [readonly] 

## Example

```python
from ls_zoho_billing_products.models.delete_a_product_response import DeleteAProductResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteAProductResponse from a JSON string
delete_a_product_response_instance = DeleteAProductResponse.from_json(json)
# print the JSON string representation of the object
print(DeleteAProductResponse.to_json())

# convert the object into a dict
delete_a_product_response_dict = delete_a_product_response_instance.to_dict()
# create an instance of DeleteAProductResponse from a dict
delete_a_product_response_from_dict = DeleteAProductResponse.from_dict(delete_a_product_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


