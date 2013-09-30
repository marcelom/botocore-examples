__author__ = 'eric'

import botocore.session

def main():
    print
    print "Putting a file in s3 - initial parameters"

    bucket     = 'yourbucketname'
    key        = 'xyzzy'
    filename   ='testfile.txt' # assume sto be in this program's working folder
    region     = 'us-east-1' # change this to your region
    acl        = 'public-read' # we are going to set the aco to public-read so we can access the file via a url

    print
    print '         region: ' + region
    print '         bucket: ' + bucket
    print 'key (subfolder): ' + key
    print '       filename: ' + './' + filename
    print '            acl: ' + acl

    session = botocore.session.get_session()
    s3 = session.get_service('s3')
    operation = s3.get_operation('PutObject')
    endpoint = s3.get_endpoint(region)

    print
    print "uploading the file to s3"

    fp = open('./' + filename, 'rb')
    http_response, response_data = operation.call(endpoint,
                                              bucket=bucket,
                                              key=key + '/' + filename,
                                              body=fp)
    print http_response
    print response_data
    print
    print "getting s3 object properties of file we just uploaded"
    operation = s3.get_operation('GetObjectAcl')
    http_response, response_data = operation.call(endpoint,
                                                  bucket=bucket,
                                                  key=key + '/' + filename)
    print http_response
    print response_data
    print
    print "setting the acl to public-read"
    operation = s3.get_operation('PutObjectAcl')
    http_response, response_data = operation.call(endpoint,
                                                  bucket=bucket,
                                                  key=key + '/' + filename,
                                                  acl=acl)
    print http_response
    print response_data
    print
    print "The url of the object is:"
    print
    print 'http://'+bucket+'.s3.amazonaws.com/'+ key + '/' + filename

if __name__ == "__main__":
    main()