import requests
response = requests.get("http://www.novelscape.net/wxxs/j/jingyong/ffwz/001.htm")
# response.enconding = "windows-1251"
# book1 = response.text
# print(book1)
# print(response)


print(response.encoding)
response.encoding='cp1252'
print(response.encoding)
print(response.text)