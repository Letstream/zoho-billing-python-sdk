# coding: utf-8

"""
    Quotes

    A quote is an approximation, of the prices, which a seller projects to a buyer. There can be different quotes to different buyers.<br><br><b>Possible error codes: </b><br><table><thead><tr><th>Error Code</th><th>Message</th></tr></thead><tbody><tr><td><span style=\"color:#FF0000;\"> 1001</span></td><td>Quote Number already exist</td></tr><tr><td><span style=\"color:#FF0000;\"> 1002</span></td><td>Quote does not exist</td></tr><td><span style=\"color:#FF0000;\"> 2007</span></td><td>Quote cannot be raised for items that have been deleted or marked as inactive</td></tr><tr><td><span style=\"color:#FF0000;\"> 4041</span></td><td>Quote status cannot be changed to Draft</td></tr><tr><td><span style=\"color:#FF0000;\"> 9526</span></td><td>Please enter a valid retainer percentage. It should be greater than 0 and less than or equal to 100</td></tr></tbody></table>

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from setuptools import setup, find_packages  # noqa: H301

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools
NAME = "ls_zoho_billing_quotes"
VERSION = "1.0.0"
PYTHON_REQUIRES = ">= 3.9"
REQUIRES = [
    "urllib3 >= 2.1.0, < 3.0.0",
    "python-dateutil >= 2.8.2",
    "pydantic >= 2",
    "typing-extensions >= 4.7.1",
]

setup(
    name=NAME,
    version=VERSION,
    description="Quotes",
    author='Letstream',
    author_email='support@theletstream.com',
    url="https://www.theletstream.com?utm_source&#x3D;github-zohobillingclient",
    keywords=["OpenAPI", "OpenAPI-Generator", "Quotes"],
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    long_description_content_type='text/markdown',
    long_description="""\
    A quote is an approximation, of the prices, which a seller projects to a buyer. There can be different quotes to different buyers.&lt;br&gt;&lt;br&gt;&lt;b&gt;Possible error codes: &lt;/b&gt;&lt;br&gt;&lt;table&gt;&lt;thead&gt;&lt;tr&gt;&lt;th&gt;Error Code&lt;/th&gt;&lt;th&gt;Message&lt;/th&gt;&lt;/tr&gt;&lt;/thead&gt;&lt;tbody&gt;&lt;tr&gt;&lt;td&gt;&lt;span style&#x3D;\&quot;color:#FF0000;\&quot;&gt; 1001&lt;/span&gt;&lt;/td&gt;&lt;td&gt;Quote Number already exist&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;&lt;span style&#x3D;\&quot;color:#FF0000;\&quot;&gt; 1002&lt;/span&gt;&lt;/td&gt;&lt;td&gt;Quote does not exist&lt;/td&gt;&lt;/tr&gt;&lt;td&gt;&lt;span style&#x3D;\&quot;color:#FF0000;\&quot;&gt; 2007&lt;/span&gt;&lt;/td&gt;&lt;td&gt;Quote cannot be raised for items that have been deleted or marked as inactive&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;&lt;span style&#x3D;\&quot;color:#FF0000;\&quot;&gt; 4041&lt;/span&gt;&lt;/td&gt;&lt;td&gt;Quote status cannot be changed to Draft&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;&lt;span style&#x3D;\&quot;color:#FF0000;\&quot;&gt; 9526&lt;/span&gt;&lt;/td&gt;&lt;td&gt;Please enter a valid retainer percentage. It should be greater than 0 and less than or equal to 100&lt;/td&gt;&lt;/tr&gt;&lt;/tbody&gt;&lt;/table&gt;
    """,  # noqa: E501
    package_data={"ls_zoho_billing_quotes": ["py.typed"]},
)