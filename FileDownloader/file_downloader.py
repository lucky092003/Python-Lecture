import requests

def download_file(url, file_name):

    file_name=f"{file_name}.{url.split(".")[-1].lower()}" # to generate extsion from url

    response = requests.get(url)

    if response.status_code == 200:

        with open(file_name, 'wb') as file:
            file.write(response.content)
        print(f"File '{file_name}' downloaded successfully.")
    else:
        print(f"Failed to download file. Status code: {response.status_code}")

if __name__ == "__main__":
	url = 'https://www.python.org/static/img/psf-logo.png'
	file_name = 'file'
	download_file(url, file_name)