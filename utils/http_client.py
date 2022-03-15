#!/usr/bin/python
# encoding=utf-8

import decimal
import json
import time

import allure
from loguru import logger
from tep import client
from tep.client import TepResponse


def request_monkey_patch(req, *args, **kwargs):
    start = time.process_time()
    desc = ""
    if "desc" in kwargs:
        desc = kwargs.get("desc")
        kwargs.pop("desc")
    response = req(*args, **kwargs)
    end = time.process_time()
    elapsed = str(decimal.Decimal("%.3f" % float(end - start))) + "s"
    log4a = "{}\n{}status:{}\nresponse:{}\nelapsed:{}"
    try:
        kv = ""
        for k, v in kwargs.items():
            # if not json, str()
            try:
                v = json.dumps(v, ensure_ascii=False)
            except TypeError:
                v = str(v)
            kv += f"{k}:{v}\n"
        args = list(args)
        args += ["", ""]
        method, url, *t = args
        method_url = ""
        if method:
            method_url = f'\nmethod:"{method}" '
        if url:
            method_url += f'\nurl:"{url}" '
        request_response = log4a.format(method_url, kv, response.status_code, response.text, elapsed)
        logger.info(request_response)
        allure.attach(request_response, f'{desc} request & response', allure.attachment_type.TEXT)
    except AttributeError:
        logger.error("request failed")
    except TypeError:
        logger.warning(log4a)
    return TepResponse(response)


def request(method, url, **kwargs):
    client.tep_request_monkey_patch = request_monkey_patch
    return client.request(method, url, **kwargs)
