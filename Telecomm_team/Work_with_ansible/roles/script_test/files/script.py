import requests
import logging


logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)



def create_request(url):
    try:
        response = requests.get(url, allow_redirects=False, timeout=10)

        if response.status_code // 100 in (1, 2, 3):
            logger.info(
                f"Request to {url} succeeded. "
                f"Status code: {response.status_code}. "
                f"Response body: {response.text.strip()}"
            )
        elif response.status_code // 100 in (4, 5):
            raise Exception(
                f"Request to {url} failed. "
                f"Status code: {response.status_code}. "
                f"Response body: {response.text.strip()}"
            )

        return response

    except requests.exceptions.RequestException as e:
        logger.error(f"Request to {url} failed with error: {str(e)}")
        raise
    except Exception as e:
        logger.error(str(e))
        raise


def main():
    test_urls = [
        "https://httpstat.us/100",
        "https://httpstat.us/200",
        "https://httpstat.us/301",
        "https://httpstat.us/404",
        "https://httpstat.us/500"
    ]

    for url in test_urls:
        try:
            logger.info(f"Making request to: {url}")
            create_request(url)
        except Exception as e:
            logger.error(f"Error processing request to {url}: {str(e)}")
        finally:
            logger.info("-" * 50)


if __name__ == "__main__":
    main()