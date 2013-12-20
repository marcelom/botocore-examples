__author__ = 'eric'
import botocore.session
import time

def main():

    start = time.time()

    print
    print "Sending a message, receive a message and delete a message from sqs queue"

    # change this to your queue_url
    queue_url = 'https://your queue url'
    region     = 'us-east-1' # change this to your region

    print 'queue_url: ' + queue_url
    print '   region: ' + region

    session = botocore.session.get_session()
    sqs = session.get_service('sqs')
    endpoint = sqs.get_endpoint(region)
    send = sqs.get_operation('SendMessage')
    receive = sqs.get_operation('ReceiveMessage')
    delete = sqs.get_operation('DeleteMessage')

    print "Send a message"
    print
    # message bodies can be json, xml, plan text and a lot more
    message_body =  "this is a message body" # this can be any ascii text and can contain some other characters

    http_response, response_data = send.call(endpoint, queue_url = queue_url, message_body = message_body)

    # if you use sendMessageBatch operation you can get a 200 status code returned even if one or more messages could not be sent
    # see the aws sqs documentation

    if not http_response.status_code == 200:
        print "An error value was returned"
        print http_response.status_code

    print "response_data:"
    print response_data
    print
    print "Receive a message"
    http_response, response_data = receive.call(endpoint, queue_url = queue_url)

    if not http_response.status_code == 200:
        print "An error value was returned"
        print http_response.status_code

    print response_data
    print
    msgs = response_data.get('Messages')
    print "  The message body: " + msgs[0].get("Body")
    print "The receipt handle: " + msgs[0].get('ReceiptHandle')
    print
    print "Delete the message we just received"

    http_response, response_data = delete.call(endpoint, queue_url = queue_url, receipt_handle = msgs[0].get('ReceiptHandle'))

    if not http_response.status_code == 200:
        print "An error value was returned"
        print http_response.status_code

    print response_data
    print
    print "Total elapsed time (sec): " + str(time.time() - start)

if __name__ == '__main__':
    main()