# CreateAProductRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of your choice to be displayed in the interface. | 
**description** | **str** | Short description regarding the product. | [optional] 
**email_ids** | **str** | The email IDs to which notifications related to the product need to be sent. (Use comma separation for multiple email-ids) | [optional] 
**redirect_url** | **str** | The URL to which customers should be redirected to once they subscribe to the product. | [optional] 

## Example

```python
from ls_zoho_billing_products.models.create_a_product_request import CreateAProductRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAProductRequest from a JSON string
create_a_product_request_instance = CreateAProductRequest.from_json(json)
# print the JSON string representation of the object
print(CreateAProductRequest.to_json())

# convert the object into a dict
create_a_product_request_dict = create_a_product_request_instance.to_dict()
# create an instance of CreateAProductRequest from a dict
create_a_product_request_from_dict = CreateAProductRequest.from_dict(create_a_product_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


