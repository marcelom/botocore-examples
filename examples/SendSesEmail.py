__author__ = 'eric'


import botocore.session

def main():
    print
    print "sending email via ses - initial parameters"

    subject     = "SES test email"
    region      = 'us-east-1' #change this to your region

    destination = {'ToAddresses': ['someone@somedomain.com']} # to test ses validate an email address and use that one
    source      = 'someone@somedomain.com' # this is the from address
    msgbody     = {'Subject': {'Data': 'this is a subject'}, 'Body': {'Text': {'Data': 'This is the body' + "\nand more lines"}}}

    print "setting up the session and sending the email"
    session = botocore.session.get_session()
    ses = session.get_service('ses')
    operation = ses.get_operation('SendEmail')
    endpoint = ses.get_endpoint(region)

    http_response, response_data = operation.call(endpoint,
                                                  source=source,
                                                  destination=destination,
                                                  message=msgbody)

    print "the results returned from the SendEmail operation"
    print http_response
    print response_data

if __name__ == "__main__":
    main()
