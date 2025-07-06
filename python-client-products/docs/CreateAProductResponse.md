# CreateAProductResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] [readonly] 
**message** | **str** |  | [optional] [readonly] 
**product** | [**ProductResponse**](ProductResponse.md) |  | [optional] 

## Example

```python
from ls_zoho_billing_products.models.create_a_product_response import CreateAProductResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAProductResponse from a JSON string
create_a_product_response_instance = CreateAProductResponse.from_json(json)
# print the JSON string representation of the object
print(CreateAProductResponse.to_json())

# convert the object into a dict
create_a_product_response_dict = create_a_product_response_instance.to_dict()
# create an instance of CreateAProductResponse from a dict
create_a_product_response_from_dict = CreateAProductResponse.from_dict(create_a_product_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


