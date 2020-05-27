import base64
import json
import requests

class Pinterest:
#TODO: CRIO_TASK_MODULE_PINTEREST_SHARE
# As part of this module you are expected to complete the publish_photo_msg function
# Tasks:
# 1) You need to register as pinterest developer to obtain app_id & app_secret
# 2) Obtain an access token using Postman method and store it in access_tokens.sh
# 3) Obtain Pinterest board ID by creating a Pinterest Board using the Pinterest Create Board API
#    (https://developers.pinterest.com/docs/api/boards/) and store it in access_tokens.sh
# 4) Enter board_id & access_token in access_tokens.sh - IMPORTANT step
#    PINTEREST_BOARD_ID=board_id
#    PINTEREST_ACCESS_TOKEN=access_token
# 5) Complete the publish_photo_msg() function. This function should publish a pin with
#    the given message and photo. The post should be published to the board you have created
#    in the earlier step
# 6) Manually verify the pin created and submit the code
#
# NOTE: The Pinterest API has a rate limit of 10 requests/hour. If you exceed
#       this limit, you can either wait until the rate counter resets or create
#       a new board and use it to test your implementation.

# Args:
#   1) message   -> string message to be posted
#   2) image_url -> publicly accessible url of the image to be posted

# write your code below
    def publish_photo_msg(self, message, image_url):

        url = 'https://api.pinterest.com/v1/pins/?access_token=Ai6ilWntsTcxmhkalJqQS6S82QcqFes-BYoiF4JGeSXao8ChzQoYADAAAxrtRnkmNl_AxZ4AAAAA&fields=id%2Clink%2Cnote%2Curl&board=Voltmommy/Qeats&note=' + message + '&image_url=' + image_url
        response = requests.request("POST", url, headers={}, data = {})
        print(response.json())

Pinterest().publish_photo_msg('Is it working?!', 'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAATYAAACjCAMAAAA3vsLfAAAAP1BMVEX///+msbegrLKfq7GjrrXi5efEy8+vub6ps7nv8fL29/istrzf4+XY3d/o6+y7w8jR1tm5wcbN09bCyc3y9PTNNlT3AAACUUlEQVR4nO3c6W6DMBBG0XpswhYIEN7/Wcu+tGnjqSrZSPdIlar8Gn0y48GBfHwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAID/dn9mWegaLqcy4kwZuoqLKVIxgzR0HdeSGzem5h6hC7mUYgptiK0JXcmlZHNqxuahK7mS57LYaG0atV0XWxK6lCtp187GhqCxLjZmXY1E5rVmitCVXEozj2wlqal0Q2xOutBlXEF+r6oqmddXYyXrxn/zZPyQ0e0HVWpFnHNis2aIq8jHzKpW5g9F2nvoCiPUyDrcjh3NPsZZrX7K4VMnrgpdZWT68hDaktH0dyYpG8RBLcaPM33oWuPhndoYHLktiq/X4m/sLXS5sWgVsVmO3haJfZ/WlhpDyKr0T02YQFaK/cDR1zY3/87GEdJOcYnS2Da9YkMIXWtEEu/WRmc7aLxbm+Ma3XXesQlHbjv/jVS4G90R258oYqtD1xoR/97GlnCg2EkZQHaV4tQodK0RUdzJc3O1KxQ3V9zK7/xTo7sdPBTNjWPKjWZPILeN5uRoyI3rdKH4LmHgMm4WJv4D74xvryaaEWRab6ELjsRTtdyYQha5arlZzo8WmtGNx+03veKJIxbbTnHoRmc7yN4HtsQWutKo1J67Aq9fnXVe7Y1L9KvUo7053pD8xme18Zz4N/375cbs8ULvTq9ulG2bnd7myFhrLy2/XmGMuNt8OlTcH2tw0gauLmKVsSL29HJVMb2KZUsmj9/k9YvnivKa6xMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAsPoElgcQiyXfWy4AAAAASUVORK5CYII=')
