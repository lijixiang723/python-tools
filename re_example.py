import re

# 正则匹配国内手机号
phone = 15812345678
# 根据手机号变更随时改变匹配条件
phone_apt = re.compile(r'^(13\d|14[5|7]|15\d|166|17[3|6|7]|18\d)\d{8}$')
match_result = re.search(phone_apt, str(phone))


# 正则匹配域名
links = 'http://www.123.com'
re_data = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
match_links = re.findall(re_data, links)
























