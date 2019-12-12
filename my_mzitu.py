import os
import requests
import uuid
import urllib.request

from lxml import etree

# 下载图片保存路径
DIR_PATH = r"/home/lijixiang/Desktop/images/"

HEADERS = {"Referer": "https://www.mzitu.com", 'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.87 Safari/537.36'}


# 首页分页url
index_page_urls = ['https://www.mzitu.com/page/{}'.format(i) for i in range(1, 238)]

# page_urls: 每页的url
for page_urls in index_page_urls:

    # 获取该页套图的网页信息
    response_html = requests.get(url=page_urls, headers=HEADERS)
    html_data = response_html.content.decode("utf-8")

    # 获取该页每个套图的url
    html_object = etree.HTML(html_data)
    set_image_url = html_object.xpath("//body/div[2]//ul/li/a/@href")

    # 套图中的单张图片url获取
    for img_url in set_image_url:
        response_one_html = requests.get(url=img_url, headers=HEADERS)
        one_html_data = response_one_html.content.decode("utf-8")

        # 获取套图的图片数量及描述名
        one_html_object = etree.HTML(one_html_data)
        set_image_describe = one_html_object.xpath("//body/div[2]/div[1]/h2/text()")[0]

        # 创建文件夹
        try:
            os.mkdir("/home/lijixiang/Desktop/images/{}".format(set_image_describe))
            file_path = "/home/lijixiang/Desktop/images/{}/".format(set_image_describe)
            print("文件夹创建成功")
        except:
            continue
        print("开始下载套图: " + set_image_describe)

        img_count = one_html_object.xpath("//body/div[2]/div[1]/div[4]/a[5]/span/text()")[0]
        img_count = int(img_count)

        set_url_list = [img_url + "/" + "{}".format(i) for i in range(1, img_count+1)]

        # 获取图片并下载到指定路径
        for url in set_url_list:

            # 配置下载图片的headers(防盗链)
            headers = {"Referer": "{}".format('https://www.mzitu.com/215027'),
                       'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko)'
                                     ' Chrome/76.0.3809.87 Safari/537.36'}

            response_img_html = requests.get(url=img_url, headers=headers)
            img_html_data = response_img_html.content.decode("utf-8")

            img_html_object = etree.HTML(img_html_data)
            img_result = img_html_object.xpath("//body/div[2]/div[1]/div[3]/p/a/img/@src")[0]

            # 下载图片
            # 获得图片后缀并添加图片文件名
            file_suffix = os.path.splitext(img_result)[1]
            image_name = str(uuid.uuid4()).replace('-', '') + file_suffix

            # 第一种下载方式
            try:
                result = requests.get(img_result)
                with open(file_path + image_name, 'wb') as image:
                    image.write(result.content)
            except Exception as e:
                print('下载错误：' + str(e))

            # # 第二种下载方式
            # with requests.get(img_result, headers=headers) as response, \
            #         open(file_path + image_name, 'wb') as image_save:
            #     image_save.write(response.read())

            # 第三种下载方式
            # urllib.request.urlretrieve(url, filename=file_path + image_name)







































