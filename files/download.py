from urllib import request, parse
from urllib.error import URLError
from os import path, makedirs
import shutil
import arrow

def get_directory():
    """
    Set working directory to STORAGE_FOLDER constant.
    """
    STORAGE_FOLDER = path.dirname(path.abspath(__file__))
    return path.join(STORAGE_FOLDER, 'files')

def get_date(url):
    """
    Returns the modification date of the file pointed by *url* without
    downloading it.
    """
    url = request.urlopen(url)
    date = url.info().get('Last-Modified')
    return arrow.get(date, 'ddd D MMM YYYY HH:mm:ss')

def get_local_filename(url):
    """
    Returns the name of the file pointed by url, when put in directory *dir*
    """
    folder = get_directory()
    fn = path.basename(parse.urlsplit(url).path)
    return path.join(folder, fn)

def download(url, force=False, verbose=True):
    """
    Downloads the file pointed by *url*. The file will not be downloaded if there 
    is a local up-to-date file present. Unless *force* is True, overrides this behaviour.
    """
    dir_ = get_directory()
    filename = get_local_filename(url)
    local_url = r"file://" + filename
    mod_remote = get_date(url)

    try:
        mod_local = get_date(local_url)
    except request.URLError:
        # local file does not exists
        force = True

    if force or mod_remote > mod_local:
        if verbose:
            print("-> Downloading {}".format(url))
        
        makedirs(dir_, exist_ok=True)
        with request.urlopen(url) as response, open(filename, 'wb') as out:
            shutil.copyfileobj(response, out)  # downloads in chunks
    else:
        if verbose:
            print("-> Skipping {} (already downloaded)".format(url))

def make_archive(output_filename):
    folder = get_directory()
    shutil.make_archive(output_filename, 'zip', folder)
            
if __name__ == "__main__":

    # Example: 
    # download("http://www.gks.ru/free_doc/new_site/vvp/tab1.xls")
    
    from url_config import yield_urls_based_on_yaml as url_iter
    for url in url_iter():
        download(url)        
    make_archive("files")
    
    
    
    




