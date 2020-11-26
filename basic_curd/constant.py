class ResponseHandle(object):
    @staticmethod
    def onSuccess(data,statusCode = '2XX'):
        return {'status_code':statusCode,'data':data,'message':'success'}
    @staticmethod
    def onFailure(data,statusCode = '4XX'):
        return {'status_code':statusCode,'message':data}

PAGE_SIZE=10