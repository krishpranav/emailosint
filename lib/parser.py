#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# import
import re

class parser:
    def __init__(self, content, target):
        self.target = target
        self.content = str(content)

    def email(self):
        tmp_email = re.findall(r'[a-zA-Z0-9.\-_+#~!$&\',;=:]+'
                               + '@' + r'[a-zA-Z0-9.-]*' + self.target, self.clean)
        email_list = []
        for _ in tmp_email:
            if _ not in email_list and _.split('@')[0] not in ('"', "'"):
                email_list.append(_)
        return email_list