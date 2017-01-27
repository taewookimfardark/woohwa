from time import time
import cloudstorage

def _save_file(image_binary, filepath):
    ext = filepath.split(".")[-1]
    gcs_file = cloudstorage.open(filepath,
                                 'w',
                                 content_type='image/'+ext,
                                 options={'x-goog-acl':'public-read'})
    gcs_file.write(image_binary)
    gcs_file.close()

def upload_image(image_binary, folder_name):
    filename = str(time()).replace('.', '')+".jpg"
    directory = '/woohwa_bucket/' + folder_name + '/'
    filepath = directory + filename
    _save_file(image_binary, filepath)
    urlpath = 'http://storage.googleapis.com' + directory + filename
