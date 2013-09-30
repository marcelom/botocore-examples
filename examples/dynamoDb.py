__author__ = 'eric'
import botocore.session
import time

def main():

    print "some dynamoDb examples"

    session = botocore.session.get_session()
    db = session.get_service('dynamodb')

    print "DescribeTable"
    operation = db.get_operation('DescribeTable')
    endpoint = db.get_endpoint('us-east-1') # change this to your region
    tableName = 'myTable' #change this to your dynamoDb test table name
    http_response, response_data = operation.call(endpoint,
                                              table_name=tableName)
    print
    print "results of DescribeTable for tableName:" + tableName
    print http_response
    print response_data

    getops = db.get_operation('GetItem')
    # assumes a numeric hash key as the primaryKey and named customerId
    # you can create this item in the aws console if you want
    getItem = {u'customerId':{"N":"1"}}
    http_response, response_data = getops.call(endpoint, table_name='myTable', key=getItem)

    print
    print http_response
    print "getItem Results: " + str(response_data)

    print
    print "Insert a few hundred Items (records) in " + tableName

    putops = db.get_operation('PutItem')

    i = 0
    x = {}
    y = {}
    while i < 200:
        print i
        string = "this is a made up key string for itemId=" + str(i)
        putItem = {u'customerId':{"N":i}}
        x['N']=str(i)
        y['S']=string
        putItem[u'customerId']=x
        putItem[u'astringattribute']=y
        # 'N' tells AWS that the string should be treated as a number
        # 'S' treat the string as a string
        # 'SS' treat the string as a set of strings (like an array)
        putItem[u'setstringattribute'] = {u'SS':(u"x", u"y")}

        # uncomment out the print putItem if you want to see what we are inserting into DynamoDb
        #print putItem

        http_response, response_data = putops.call(endpoint, table_name='myTable', item=putItem)
        i = i + 1

        # dynamoDb throttles inserts so you may see them slow down in your terminal window
        # lets put a little delay into the inserts ourselves
        if i % 10 == 0:
            time.sleep(2)


if __name__ == "__main__":
    main()
