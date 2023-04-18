import os

for subdir, dirs, files in os.walk('./'):
	print(files)
 

# PUT /echo/put/json HTTP/1.1
# Host: reqbin.com
# Content-Type: application/json
# Content-Length: 80

# {
#   "Id": 12345,
#   "Customer": "John Smith",
#   "Quantity": 1,
#   "Price": 10.00
# }