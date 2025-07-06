# CustomerResponseDocumentsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**can_show_in_portal** | **object** | Set to true if the attachment can be viewed in Client Portal. | [optional] 
**file_name** | **object** | Name of the attached file. | [optional] 
**file_type** | **object** | Type of the attached file. | [optional] 
**file_size** | **object** |  | [optional] 
**file_size_formatted** | **object** |  | [optional] 
**document_id** | **object** | Unique ID of the attached file. | [optional] 
**attachment_order** | **object** | Order of the attached file for a particular customer. | [optional] 

## Example

```python
from ls_zoho_billing_customers.models.customer_response_documents_inner import CustomerResponseDocumentsInner

# TODO update the JSON string below
json = "{}"
# create an instance of CustomerResponseDocumentsInner from a JSON string
customer_response_documents_inner_instance = CustomerResponseDocumentsInner.from_json(json)
# print the JSON string representation of the object
print(CustomerResponseDocumentsInner.to_json())

# convert the object into a dict
customer_response_documents_inner_dict = customer_response_documents_inner_instance.to_dict()
# create an instance of CustomerResponseDocumentsInner from a dict
customer_response_documents_inner_from_dict = CustomerResponseDocumentsInner.from_dict(customer_response_documents_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


