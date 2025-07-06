# EmailtemplatesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**selected** | **bool** | Boolean check for the email template. Whether selected or not | [optional] 
**name** | **str** | The name of the line item | [optional] 
**email_template_id** | **str** | Get the email content based on a specific email template. If this param is not inputted, then the content will be based on the email template associated with the customer. If no template is associated with the customer, then default template will be used. | [optional] 

## Example

```python
from ls_zoho_billing_quotes.models.emailtemplates_inner import EmailtemplatesInner

# TODO update the JSON string below
json = "{}"
# create an instance of EmailtemplatesInner from a JSON string
emailtemplates_inner_instance = EmailtemplatesInner.from_json(json)
# print the JSON string representation of the object
print(EmailtemplatesInner.to_json())

# convert the object into a dict
emailtemplates_inner_dict = emailtemplates_inner_instance.to_dict()
# create an instance of EmailtemplatesInner from a dict
emailtemplates_inner_from_dict = EmailtemplatesInner.from_dict(emailtemplates_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


