import time

from celery import shared_task

from api.models import File


@shared_task
def upload_file(file_id):
    file = File.objects.get(id=file_id)
    print(f'Processing file {file.filename}')
    if '.txt' in file.filename:
        print(f'Processing TEXT extension file {file.filename}')
    elif '.img' in file.filename:
        print(f'Processing IMAGE extension file {file.filename}')
    else:
        print('Processing file of undefined in tasks.py extension')
    time.sleep(10)
    file.processed = True
    file.save()
    print('File has been processed')
