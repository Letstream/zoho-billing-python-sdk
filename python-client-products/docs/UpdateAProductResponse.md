# UpdateAProductResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] [readonly] 
**message** | **str** |  | [optional] [readonly] 
**product** | [**ListOfAllProductsResponseProductsInner**](ListOfAllProductsResponseProductsInner.md) |  | [optional] 

## Example

```python
from ls_zoho_billing_products.models.update_a_product_response import UpdateAProductResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateAProductResponse from a JSON string
update_a_product_response_instance = UpdateAProductResponse.from_json(json)
# print the JSON string representation of the object
print(UpdateAProductResponse.to_json())

# convert the object into a dict
update_a_product_response_dict = update_a_product_response_instance.to_dict()
# create an instance of UpdateAProductResponse from a dict
update_a_product_response_from_dict = UpdateAProductResponse.from_dict(update_a_product_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


