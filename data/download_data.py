# Author: Taiwo Owoseni
# Date: 16th December, 2021
# Project: Swifter Project

'''
Downloads text data from a given URL to a local filepath.
Usage: download_data.py --url=<url> --file_path=<file_path>

Options:
--url=<url>                 URL for the data file to be downloaded 
--file_path=<file_path>     Path (including filename) to save the downloaded file
'''
  
from docopt import docopt
import requests
import os

opt = docopt(__doc__)

def main(url, file_path): 
    try:
        data = requests.get(url)
    except Exception as request:
        print(f'{url} does not exists')
        print(request)

    _, extension = os.path.splitext(file_path)
    if request.status_code == 200 and extension =='.txt':
        try:
            with open(file_path, 'wb')as file:
                file.write(data.content)
        except:
            os.makedirs(os.path.dirname(file_path))
            with open(file_path, 'wb')as file:
                file.write(data.content)

    # assertion tests
    assert extension == '.csv', f'Wrong extesnion type. Extension has to be a {extension}'

if __name__ == '__main__':
  main(opt['--url'], opt['--file_path'])
