#!/usr/bin/env python3
"""รวมไฟล์ทั้งหมดเป็น HTML ไฟล์เดียวไว้ทดลองเล่น/แชร์ลิงก์ (ตัวเกมจริงยังเป็นหลายไฟล์)"""
import re,os
root=os.path.join(os.path.dirname(__file__),'..');rd=lambda p:open(os.path.join(root,p),encoding='utf8').read()
h=rd('index.html')
h=re.sub(r'<link rel="manifest"[^>]*>\n?','',h)
h=re.sub(r'<link rel="stylesheet" href="([^"]+)">',lambda m:'<style>'+rd(m.group(1))+'</style>',h)
h=re.sub(r'<script src="([^"]+)"></script>',lambda m:'<script>'+rd(m.group(1)).replace('</script>','<\\/script>')+'</script>',h)
open(os.path.join(root,'..','blossom-link-saga-preview.html'),'w',encoding='utf8').write(h)
