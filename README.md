# Business Portal Cache Lambda

This lambda caches files into S3 for use in the business portal. The files are
stored in S3 according to the `S3_BUCKET`and `S3_PREFIX` env vars. Files will be
stored at `S3_BUCKET/S3_PREFIX/<filename>`.

Currently caches:

1) The
[business types file](https://data.cityofgainesville.org/resource/i9px-haju.json).
Stored with filename `business_types.json`.
2) The
[business permits file](https://data.cityofgainesville.org/resource/mfe4-6q3g.json).
Stored with filename `business_permits.json`.


## Usage

Run `make package` to create the artifact for the lambda, this will create
`business_portal_cache_lambda.zip`. This is ready for use with the Python 3.6
runtime and handler `business_portal_cache_lambda.lambda_handler`.

The script can also be run manually with
`python business_portal_cache_lambda.py`.


## Requirements

This requires the `S3_BUCKET` and `S3_PREFIX` environment variables to be set.

`S3_BUCKET`: The bucket on S3 to use.  
`S3_PREFIX`: Prefix to prepend to files when saving to the bucket. Prefix and
filename will be joined with "/". If empty, the file will be saved to the root
of the bucket.

The lambda must be given write permissions to the desired location on S3.


## Modification

To edit which files are cached or under what names, edit the `URLS_TO_CACHE`
variable in `business_portal_cache_lambda.py`.


## License
By contributing your code, you agree to license your contribution under the
[MIT License](https://github.com/c4gnv/business-portal-cache-lambda/blob/master/LICENSE).
