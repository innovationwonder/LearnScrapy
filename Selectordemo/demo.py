# 直接使用

from scrapy import Selector

body = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>

</body>
</html>'''
selector = Selector(text=body)
title = selector.xpath('//title/text()').extract_first()
print(title)