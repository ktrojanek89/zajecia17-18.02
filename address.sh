#!/usr/bin/bash
ip address|grep inet|grep enp0s3|awk '{print$2}'|cut -d '/' -f1
