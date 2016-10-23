# -*- coding: utf-8 -*-

from scrapy.downloadermiddlewares.retry import RetryMiddleware

class CustomRetryMiddleware(RetryMiddleware):

    def process_response(self, request, response, spider):
        url = response.url
        if response.status in [301, 302,503,403]:
	    reason = 'redirect %d' %response.status 
            return self._retry(request,reason,spider) or response
        return response
