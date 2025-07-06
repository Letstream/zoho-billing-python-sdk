# PageContextInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | **int** | Number of pages | [optional] 
**per_page** | **int** | Per page values | [optional] 
**has_more_page** | **bool** | Check if has more pages | [optional] 
**report_name** | **str** | The report name | [optional] 
**applied_filter** | **str** | The filer applied for sorting | [optional] 
**sort_column** | **str** | Sort quotes. Allowed Values &lt;code&gt;customer_name&lt;/code&gt;, &lt;code&gt;estimate_number&lt;/code&gt;, &lt;code&gt;date&lt;/code&gt;, &lt;code&gt;total&lt;/code&gt; and &lt;code&gt;created_time&lt;/code&gt; | [optional] 
**sort_order** | **str** | The order for sorting | [optional] 

## Example

```python
from ls_zoho_billing_quotes.models.page_context_inner import PageContextInner

# TODO update the JSON string below
json = "{}"
# create an instance of PageContextInner from a JSON string
page_context_inner_instance = PageContextInner.from_json(json)
# print the JSON string representation of the object
print(PageContextInner.to_json())

# convert the object into a dict
page_context_inner_dict = page_context_inner_instance.to_dict()
# create an instance of PageContextInner from a dict
page_context_inner_from_dict = PageContextInner.from_dict(page_context_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


