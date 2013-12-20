__author__ = 'eric'
import botocore.session
import time

def main():

    start = time.time()

    print
    print "Show how to use the Batch function with SQS queues"

    # change this to your queue_url
    queue_url = 'https://some queue url'
    region     = 'us-east-1' # change this to your region

    print 'queue_url: ' + queue_url
    print '   region: ' + region

    session = botocore.session.get_session()
    sqs = session.get_service('sqs')
    endpoint = sqs.get_endpoint(region)
    send = sqs.get_operation('SendMessageBatch')

    print "Send  99 messages, 10 at a time"
    # message bodies can be json, xml, plan text and a lot more
    message_body_prefix =  "1234567890_" # this can be any ascii text and can contain some other characters

    entries = list()
    counter=0
    while counter <99:
        # send batch every 10 messages,
        entry = {'Id': "testmsg_" + str(counter), 'MessageBody' : message_body_prefix + str(counter)}
        entries.append(entry)
        # bacth size of up to 10 messages allowed
        if (counter+1) % 10 == 0:
            http_response, response_data = send.call(endpoint, queue_url = queue_url, entries = entries)
            # in production you can get a 200 status value and some of the messages still might have failed to be sent
            # see the aws documentation on how to detect individual message failures
            if not http_response.status_code == 200:
                print "error sending batch messages: " + str(http_response.status_code) + " " + str(response_data)
            entries = list()
        counter += 1

    # process any remaining messages
    if len(entries) > 0:
        http_response, response_data = send.call(endpoint, queue_url = queue_url, entries = entries)
        if not http_response.status_code == 200:
            print "error sending batch messages: " + str(http_response.status_code) + " " + str(response_data)

    print "Total elapsed time (sec): " + str(time.time() - start)

if __name__ == '__main__':
    main()