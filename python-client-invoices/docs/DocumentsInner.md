# DocumentsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_name** | **object** | Name of the attached file. | [optional] 
**file_type** | **object** | Type of the attached file. | [optional] 
**file_size** | **object** |  | [optional] 
**file_size_formatted** | **object** |  | [optional] 
**document_id** | **object** | Unique ID of the attached file. | [optional] 
**attachment_order** | **object** | Order of the attached file for a particular customer. | [optional] 

## Example

```python
from ls_zoho_billing_invoices.models.documents_inner import DocumentsInner

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentsInner from a JSON string
documents_inner_instance = DocumentsInner.from_json(json)
# print the JSON string representation of the object
print(DocumentsInner.to_json())

# convert the object into a dict
documents_inner_dict = documents_inner_instance.to_dict()
# create an instance of DocumentsInner from a dict
documents_inner_from_dict = DocumentsInner.from_dict(documents_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


