import http.client
import json

conn = http.client.HTTPSConnection("{{server_url}}")
payload = "{\n    \"employee\": \n        {\n            \"name\": \"{{name}}\",\n            \"nis\": \"{{nis}}\",\n            \"registration_number\": \"{{registration_number}}\",\n            \"email\": \"{{employee_email}}\",\n            \"use_qrcode\": {{use_qrcode}}\n        }\n}"
headers = {
  'Content-Type': 'application/json',
  'access-token': '{{client_token}}'
}
conn.request("PUT", "/external_api/v1/employees/{{employee_id}}", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))