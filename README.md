# Thumbhammer

An utterly fantastic way to generate thumbnails that are exactly 300x300px and storing them locally.

## Next Steps
Likely integrate django-storages for storing images in S3, since we don't have access to the local filesystem on Heroku.

## Deployment

Once images are being stored in AWS, this project is ready to be deployed to Heroku.

## Scaling

The thumbnail generation is easy to scale horizontally by adding additional celery workers. 