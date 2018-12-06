import re


def replace_img_src(html_body):
    rule = r'src="(.*?)"'
    img_data_src_list = re.compile(rule, re.I).findall(html_body)
    for img_src in img_data_src_list:
        if img_src.startswith("/"):
            html_body = html_body.replace(img_src,"http://img.chyxx.com%s"%img_src)
    return html_body