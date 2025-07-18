# ls_zoho_billing_hosted_pages
Zoho Billing provides a hosted payment page to integrate with your websites. You can securely integrate with Zoho Billing for collecting your customer's sensitive card information through the hosted page. These Hosted Pages will expire within one hour.

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 1.0.0
- Package version: 1.0.0
- Generator version: 7.14.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python 3.9+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import ls_zoho_billing_hosted_pages
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import ls_zoho_billing_hosted_pages
```

### Tests

Execute `pytest` to run the tests.

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import ls_zoho_billing_hosted_pages
from ls_zoho_billing_hosted_pages.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://www.zohoapis.com/billing/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ls_zoho_billing_hosted_pages.Configuration(
    host = "https://www.zohoapis.com/billing/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]


# Enter a context with an instance of the API client
with ls_zoho_billing_hosted_pages.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ls_zoho_billing_hosted_pages.HostedPagesApi(api_client)
    x_com_zoho_subscriptions_organizationid = '10234695' # str | ID of the organization
    add_payment_method_for_a_customer_request = ls_zoho_billing_hosted_pages.AddPaymentMethodForACustomerRequest() # AddPaymentMethodForACustomerRequest |  (optional)

    try:
        # Associate a Payment method for a customer
        api_response = api_instance.hostedpages_addpaymentmethod_post(x_com_zoho_subscriptions_organizationid, add_payment_method_for_a_customer_request=add_payment_method_for_a_customer_request)
        print("The response of HostedPagesApi->hostedpages_addpaymentmethod_post:\n")
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling HostedPagesApi->hostedpages_addpaymentmethod_post: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://www.zohoapis.com/billing/v1*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*HostedPagesApi* | [**hostedpages_addpaymentmethod_post**](docs/HostedPagesApi.md#hostedpages_addpaymentmethod_post) | **POST** /hostedpages/addpaymentmethod | Associate a Payment method for a customer
*HostedPagesApi* | [**hostedpages_buyonetimeaddon_post**](docs/HostedPagesApi.md#hostedpages_buyonetimeaddon_post) | **POST** /hostedpages/buyonetimeaddon | Buy one-time addon for a subscription
*HostedPagesApi* | [**hostedpages_get**](docs/HostedPagesApi.md#hostedpages_get) | **GET** /hostedpages | List of HostedPages
*HostedPagesApi* | [**hostedpages_hostedpage_id_get**](docs/HostedPagesApi.md#hostedpages_hostedpage_id_get) | **GET** /hostedpages/{hostedpage_id} | Retrieve a hosted page
*HostedPagesApi* | [**hostedpages_invoicepayment_post**](docs/HostedPagesApi.md#hostedpages_invoicepayment_post) | **POST** /hostedpages/invoicepayment | Record a Invoice Payment
*HostedPagesApi* | [**hostedpages_newsubscription_post**](docs/HostedPagesApi.md#hostedpages_newsubscription_post) | **POST** /hostedpages/newsubscription | Create a subscription
*HostedPagesApi* | [**hostedpages_updatecard_post**](docs/HostedPagesApi.md#hostedpages_updatecard_post) | **POST** /hostedpages/updatecard | Update card for a subscription
*HostedPagesApi* | [**hostedpages_updatepaymentmethod_post**](docs/HostedPagesApi.md#hostedpages_updatepaymentmethod_post) | **POST** /hostedpages/updatepaymentmethod | Update customer payment details
*HostedPagesApi* | [**hostedpages_updatesubscription_post**](docs/HostedPagesApi.md#hostedpages_updatesubscription_post) | **POST** /hostedpages/updatesubscription | Update a subscription


## Documentation For Models

 - [AddPaymentMethodForACustomerRequest](docs/AddPaymentMethodForACustomerRequest.md)
 - [AddPaymentMethodForACustomerResponse](docs/AddPaymentMethodForACustomerResponse.md)
 - [AddPaymentMethodForACustomerResponseHostedpage](docs/AddPaymentMethodForACustomerResponseHostedpage.md)
 - [AddonsInner](docs/AddonsInner.md)
 - [BillingAddress](docs/BillingAddress.md)
 - [BuyOneTimeAddonForASubscriptionRequest](docs/BuyOneTimeAddonForASubscriptionRequest.md)
 - [BuyOneTimeAddonForASubscriptionRequestAddonsInner](docs/BuyOneTimeAddonForASubscriptionRequestAddonsInner.md)
 - [BuyOneTimeAddonForASubscriptionResponse](docs/BuyOneTimeAddonForASubscriptionResponse.md)
 - [BuyOneTimeAddonForASubscriptionResponseHostedpage](docs/BuyOneTimeAddonForASubscriptionResponseHostedpage.md)
 - [BuyOneTimeAddonForASubscriptionResponseHostedpageCustomFieldsInner](docs/BuyOneTimeAddonForASubscriptionResponseHostedpageCustomFieldsInner.md)
 - [Card](docs/Card.md)
 - [CommentsInner](docs/CommentsInner.md)
 - [ContactpersonsInner](docs/ContactpersonsInner.md)
 - [Coupon](docs/Coupon.md)
 - [CreateASubscriptionRequest](docs/CreateASubscriptionRequest.md)
 - [CreateASubscriptionRequestAddonsInner](docs/CreateASubscriptionRequestAddonsInner.md)
 - [CreateASubscriptionRequestContactpersonsInner](docs/CreateASubscriptionRequestContactpersonsInner.md)
 - [CreateASubscriptionRequestCustomer](docs/CreateASubscriptionRequestCustomer.md)
 - [CreateASubscriptionRequestCustomerDefaultTemplates](docs/CreateASubscriptionRequestCustomerDefaultTemplates.md)
 - [CreateASubscriptionRequestPlan](docs/CreateASubscriptionRequestPlan.md)
 - [CreateASubscriptionResponse](docs/CreateASubscriptionResponse.md)
 - [Customer](docs/Customer.md)
 - [Data](docs/Data.md)
 - [DataSubscription](docs/DataSubscription.md)
 - [DataSubscriptionAddonsInner](docs/DataSubscriptionAddonsInner.md)
 - [DataSubscriptionCard](docs/DataSubscriptionCard.md)
 - [DataSubscriptionContactpersonsInner](docs/DataSubscriptionContactpersonsInner.md)
 - [DataSubscriptionCoupon](docs/DataSubscriptionCoupon.md)
 - [DataSubscriptionCustomFieldsInner](docs/DataSubscriptionCustomFieldsInner.md)
 - [DataSubscriptionCustomer](docs/DataSubscriptionCustomer.md)
 - [DataSubscriptionCustomerBillingAddress](docs/DataSubscriptionCustomerBillingAddress.md)
 - [DataSubscriptionNotesInner](docs/DataSubscriptionNotesInner.md)
 - [DataSubscriptionPlan](docs/DataSubscriptionPlan.md)
 - [DataSubscriptionTaxesInner](docs/DataSubscriptionTaxesInner.md)
 - [InvoiceItemsInner](docs/InvoiceItemsInner.md)
 - [ItemCustomFieldsInner](docs/ItemCustomFieldsInner.md)
 - [ListOfHostedpagesResponse](docs/ListOfHostedpagesResponse.md)
 - [ListOfHostedpagesResponseHostedPagesInner](docs/ListOfHostedpagesResponseHostedPagesInner.md)
 - [NotesInner](docs/NotesInner.md)
 - [PaymentGatewaysInner](docs/PaymentGatewaysInner.md)
 - [PaymentsInner](docs/PaymentsInner.md)
 - [Plan](docs/Plan.md)
 - [RecordInvoicePaymentForASubscriptionRequest](docs/RecordInvoicePaymentForASubscriptionRequest.md)
 - [RecordInvoicePaymentForASubscriptionResponse](docs/RecordInvoicePaymentForASubscriptionResponse.md)
 - [RecordInvoicePaymentForASubscriptionResponseHostedpage](docs/RecordInvoicePaymentForASubscriptionResponseHostedpage.md)
 - [RetrieveAHostedPageResponse](docs/RetrieveAHostedPageResponse.md)
 - [RetrieveAHostedPageResponseData](docs/RetrieveAHostedPageResponseData.md)
 - [RetrieveAHostedPageResponseDataInvoice](docs/RetrieveAHostedPageResponseDataInvoice.md)
 - [RetrieveAHostedPageResponseDataInvoiceBillingAddress](docs/RetrieveAHostedPageResponseDataInvoiceBillingAddress.md)
 - [RetrieveAHostedPageResponseDataInvoiceCouponInner](docs/RetrieveAHostedPageResponseDataInvoiceCouponInner.md)
 - [RetrieveAHostedPageResponseDataInvoiceCreditsInner](docs/RetrieveAHostedPageResponseDataInvoiceCreditsInner.md)
 - [RetrieveAHostedPageResponseDataInvoiceInvoiceItemsInner](docs/RetrieveAHostedPageResponseDataInvoiceInvoiceItemsInner.md)
 - [RetrieveAHostedPageResponseDataInvoicePaymentsInner](docs/RetrieveAHostedPageResponseDataInvoicePaymentsInner.md)
 - [RetrieveAHostedPageResponseDataSubscription](docs/RetrieveAHostedPageResponseDataSubscription.md)
 - [RetrieveAHostedPageResponseDataSubscriptionAddonsInner](docs/RetrieveAHostedPageResponseDataSubscriptionAddonsInner.md)
 - [RetrieveAHostedPageResponseDataSubscriptionCustomer](docs/RetrieveAHostedPageResponseDataSubscriptionCustomer.md)
 - [RetrieveAHostedPageResponseDataSubscriptionPlan](docs/RetrieveAHostedPageResponseDataSubscriptionPlan.md)
 - [ShippingAddress](docs/ShippingAddress.md)
 - [Subscription](docs/Subscription.md)
 - [SubscriptionCard](docs/SubscriptionCard.md)
 - [TagsInner](docs/TagsInner.md)
 - [UpdateASubscriptionRequest](docs/UpdateASubscriptionRequest.md)
 - [UpdateASubscriptionRequestPlan](docs/UpdateASubscriptionRequestPlan.md)
 - [UpdateASubscriptionResponse](docs/UpdateASubscriptionResponse.md)
 - [UpdateASubscriptionResponseHostedpage](docs/UpdateASubscriptionResponseHostedpage.md)
 - [UpdateCardForASubscriptionRequest](docs/UpdateCardForASubscriptionRequest.md)
 - [UpdateCardForASubscriptionResponse](docs/UpdateCardForASubscriptionResponse.md)
 - [UpdateCardForASubscriptionResponseHostedpage](docs/UpdateCardForASubscriptionResponseHostedpage.md)
 - [UpdatePaymentMethodRequest](docs/UpdatePaymentMethodRequest.md)
 - [UpdatePaymentMethodResponse](docs/UpdatePaymentMethodResponse.md)
 - [UpdatePaymentMethodResponseHostedpage](docs/UpdatePaymentMethodResponseHostedpage.md)


<a id="documentation-for-authorization"></a>
## Documentation For Authorization


Authentication schemes defined for the API:
<a id="Zoho_Auth"></a>
### Zoho_Auth

- **Type**: OAuth
- **Flow**: implicit
- **Authorization URL**: https://accounts.zoho.com/oauth/v2/auth
- **Scopes**: 
 - **ZohoSubscriptions.hostedpages.READ**: Read Hostedpages
 - **ZohoSubscriptions.hostedpages.CREATE**: Create Hostedpages


## Author




