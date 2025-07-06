# RetrieveAProductResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] [readonly] 
**message** | **str** |  | [optional] [readonly] 
**product** | [**ListOfAllProductsResponseProductsInner**](ListOfAllProductsResponseProductsInner.md) |  | [optional] 

## Example

```python
from ls_zoho_billing_products.models.retrieve_a_product_response import RetrieveAProductResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RetrieveAProductResponse from a JSON string
retrieve_a_product_response_instance = RetrieveAProductResponse.from_json(json)
# print the JSON string representation of the object
print(RetrieveAProductResponse.to_json())

# convert the object into a dict
retrieve_a_product_response_dict = retrieve_a_product_response_instance.to_dict()
# create an instance of RetrieveAProductResponse from a dict
retrieve_a_product_response_from_dict = RetrieveAProductResponse.from_dict(retrieve_a_product_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


