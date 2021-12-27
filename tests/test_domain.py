from datetime import (
    timedelta,
    datetime
)
from pathlib import Path
import pytest
import domain


aws_cloudfront_site = 'https://aws.amazon.com/pt/cloudfront/'
mock_miss_cloudfront_response_headers = {'X-Cache': 'Miss from cloudfront', 'Content-Type': 'text/html;charset=UTF-8', 'Transfer-Encoding': 'chunked', 'Connection': 'keep-alive', 'Server': 'Server', 'Date': 'Fri, 10 Dec 2021 00:47:40 GMT', 'X-Frame-Options': 'SAMEORIGIN', 'X-XSS-Protection': '1; mode=block', 'Strict-Transport-Security': 'max-age=300', 'X-Content-Type-Options': 'nosniff', 'Last-Modified': 'Tue, 07 Dec 2021 01:26:54 GMT', 'Content-Security-Policy-Report-Only': "default-src *; connect-src *; font-src * data:; frame-src *; img-src * data:; media-src *; object-src *; script-src 'unsafe-eval' 'unsafe-inline' *; style-src 'unsafe-inline' *; report-uri https://prod-us-west-2.csp-report.marketing.aws.dev/submit", 'Content-Encoding': 'gzip', 'Vary': 'accept-encoding,Content-Type,Accept-Encoding,X-Amzn-CDN-Cache,X-Amzn-AX-Treatment,User-Agent', 'Permissions-Policy': 'interest-cohort=()', 'Via': '1.1 5d3bd95ad13de92aaf890c12b505bd56.cloudfront.net (CloudFront)', 'X-Amz-Cf-Pop': 'GIG51-C1'}
mock_hit_cloudfront_response_headers = {'X-Cache': 'Hit from cloudfront', 'Content-Type': 'text/html;charset=UTF-8', 'Transfer-Encoding': 'chunked', 'Connection': 'keep-alive', 'Server': 'Server', 'Date': 'Fri, 10 Dec 2021 00:47:40 GMT', 'X-Frame-Options': 'SAMEORIGIN', 'X-XSS-Protection': '1; mode=block', 'Strict-Transport-Security': 'max-age=300', 'X-Content-Type-Options': 'nosniff', 'Last-Modified': 'Tue, 07 Dec 2021 01:26:54 GMT', 'Content-Security-Policy-Report-Only': "default-src *; connect-src *; font-src * data:; frame-src *; img-src * data:; media-src *; object-src *; script-src 'unsafe-eval' 'unsafe-inline' *; style-src 'unsafe-inline' *; report-uri https://prod-us-west-2.csp-report.marketing.aws.dev/submit", 'Content-Encoding': 'gzip', 'Vary': 'accept-encoding,Content-Type,Accept-Encoding,X-Amzn-CDN-Cache,X-Amzn-AX-Treatment,User-Agent', 'Permissions-Policy': 'interest-cohort=()',  'Via': '1.1 5d3bd95ad13de92aaf890c12b505bd56.cloudfront.net (CloudFront)', 'X-Amz-Cf-Pop': 'GIG51-C1'}


@pytest.mark.parametrize(
    "test_input,expected", [
        ("1s", timedelta(seconds=1)),
        ("10m", timedelta(minutes=10)),
        ("1d", timedelta(days=1))
    ]
)
def test_parse_time_step(test_input, expected: timedelta):
    value_to_test = domain.parse_time_step(test_input)
    assert expected.seconds == value_to_test.seconds


def test_request_endpoint():
    headers, elapsed_time = domain.request_endpoint(aws_cloudfront_site)
    print(headers, elapsed_time)


@pytest.mark.parametrize(
    "test_input,expected", [
        (mock_hit_cloudfront_response_headers, True),
        (mock_miss_cloudfront_response_headers, False)
    ]
)
def test_check_endpoint_aws_cloudfront(test_input, expected):
    value_to_test = domain.check_endpoint_aws_cloudfront(test_input)
    assert expected == value_to_test


def test_append_record():
    response_status = domain.ResponseStatus(
        cached=True,
        date_time=datetime.now(),
        elapsed_time=timedelta(days=1),
        url='https://aws.amazon.com/pt/cloudfront/'
    )
    domain.append_record(response_status, Path('~/x.csv'))
