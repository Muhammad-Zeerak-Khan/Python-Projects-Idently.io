import requests
from requests import Response, RequestException
from requests.structures import CaseInsensitiveDict



def get_website_status(url: str) -> None:
    try:
        response: Response = requests.get(url=url)

        # Information
        status_code: int = response.status_code
        request_method: str | None = response.request.method
        headers: CaseInsensitiveDict[str] = response.headers
        content_type: str = headers.get('Content-Type', 'Unknown')
        server: str = headers.get('Server', 'Unknown')
        response_time: float = response.elapsed.total_seconds()

        # Print the information
        print(f"URL: {url}")
        print(f"Status Code: {status_code}")
        print(f"Request Method: {request_method}")
        print(f"Content Type: {content_type}")
        print(f"Server: {server}")
        print(f"Response Time: {response_time:.3f}")

    except RequestException as e:
        print(f"Error: {e}")


def main() -> None:
    url_to_check: str = "https://www.python.org"
    get_website_status(url=url_to_check)

if __name__ == "__main__":
    main()