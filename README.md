Introduction
============
Recently Amazon AWS announced a new version of their AWS Command Line Interface (AWS CLI).  While researching the new
CLI I discovered that the project was using a new Python library called botocore.  Apparently botocore is meant to
eventually replace boto as the preferred Python AWS interface library.

As of September 29, 2013 the botocore documentation is lacking examples for calling most of the various AWS services.

Therefore I have put together these examples so others can jump start their usage of botocore.

Assumptions
===========
- You have a compatible Python version installed
- You have an AWS account and IAM credentials with the proper privileges configured on your system
- You know something about AWS

These examples assume you know what you are doing with AWS services.  These examples are NOT intended as a way to get familiar with
AWS Services.

Getting Started
================
If you go ahead and set up the Amazon Web Services Command Line tools
you will have botocore installed and will have your AWS credentials configured.  Since AWS CLI uses the botocore
credential verification routine you should be good to go on accessing AWS from these examples.

Each example requires you to fill in some values (for example the S3 bucket name) for these
examples to work.

Contributing
============
Pull requests and help with more examples are welcome.

Reference URLs
==============
- *[github botocore project](http://github.github.com/github-flavored-markdown/sample_content.html)*
- *[Amazon CLI Tools](http://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-set-up.html)*
- *For SES to work there are important steps in the [SES Documentation](http://docs.aws.amazon.com/ses/latest/DeveloperGuide/Welcome.html) that you must follow.*

License
=======
See the LICENSE.txt file in this project.

Contact Info
============
eric [at] alphaea [dot] com

