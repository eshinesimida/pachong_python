# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 11:04:46 2019

@author: lenovo
"""

import requests
import re
import time

import pandas as pd
import requests
import csv
import numpy as np
import pymysql
import math
import datetime

connect = pymysql.Connect(
        host='rm-wz988to0p0a7js870o.mysql.rds.aliyuncs.com',
        port=3306,
        user='root',
        passwd='zd45+3=48',
        db='ctrip_gengxin',
        use_unicode=1,
        charset='utf8'
    )

head = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:56.0) Gecko/20100101 Firefox/56.0'}
url = 'https://www.zhihu.com/api/v4/search_v3?t=general&q=%E7%AE%97%E6%B3%95&correction=1&offset=0&limit=20&lc_idx=20&show_all_topics=0&search_hash_id=fb7df4a866632699a074851473178cb5&vertical_info=0%2C1%2C1%2C1%2C0%2C0%2C0%2C0%2C0%2C1'
time.sleep(2)
res_json = requests.get(url, headers = head).json()

headers = {
   'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36',
   'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
   'X-Requested-With':'XMLHttpRequest',
   'Referer':'https://www.zhihu.com',
   'Cookie':'_xsrf=qPZaHP46snrSEX06lvN2mgexj4sJoKs4; _zap=d067c3c5-a359-45da-bca1-67b99900801e; d_c0="ALBjljrV2Q-PTvs7RwHJ93Y46IUvOt-k9Xs=|1565096557"; capsion_ticket="2|1:0|10:1568460488|14:capsion_ticket|44:ZWYxNjYyN2E4NDY1NGYwMzg4YzdiZWFlNjc1OTkxNzA=|e6da20d674e4f026cc05de36c8bf6f763e375bb9587532889073d048b549baf7"; z_c0="2|1:0|10:1568460515|4:z_c0|92:Mi4xMkNHekRBQUFBQUFBc0dPV090WFpEeVlBQUFCZ0FsVk40eHhxWGdEN0NQd3l2NXJ0dWFmcjJyX0xXMzJtY3YwQjhB|324cb9ed117436703d5ccd3c6b459e008a6394feb649df8cdff317e970cb7c49"; tst=r; q_c1=083e30b7d0484a8cbdd7eb17eaed4c65|1568460599000|1565096601000; __utma=51854390.205924543.1569746010.1569746010.1569746010.1; __utmz=51854390.1569746010.1.1.utmcsr=zhihu.com|utmccn=(referral)|utmcmd=referral|utmcct=/question/290268306; __utmv=51854390.100--|2=registration_date=20181012=1^3=entry_date=20181012=1; tgw_l7_route=f2979fdd289e2265b2f12e4f4a478330; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1569635476,1569681686,1569724506,1569821566; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1569821570'
}



cursor = connect.cursor()
num = len(res_json['data'])
m = 0
for i in range(1,num):
    m = m + 1
    print(m)
    if(len(res_json['data'][i]['highlight']) == 0):
        continue
    title = res_json['data'][i]['highlight']['title']
    #print(title)
    question = re.sub('<em>||</em>','',title)
    #title = ''.join(re.findall(u'[\u4e00-\u9fa5]', title))
    id_problem = res_json['data'][i]['object']['id']
    #try:
    if('question' in res_json['data'][i]['object'].keys()):
        que_id = res_json['data'][i]['object']['question']['id']
    else:
        que_id = 'none'
    #user_id = res_json['data'][i]['object']['author']['id']
    #name = res_json['data'][i]['object']['author']['name']
    #sex = res_json['data'][i]['object']['author']['gender']
    #url_user = res_json['data'][i]['object']['author']['url']
    
    
    #comment_count = res_json['data'][i]['object']['comment_count']
    #content = res_json['data'][i]['object']['content']
    #content = ''.join(re.findall(u'[\u4e00-\u9fa5]', content))
    #print(question,id_problem,que_id)
    if(que_id != 'none'):
        answer_url = 'https://www.zhihu.com/api/v4/questions/'+str(que_id)+'/answers?include=data%5B*%5D.is_normal%2Cadmin_closed_comment%2Creward_info%2Cis_collapsed%2Cannotation_action%2Cannotation_detail%2Ccollapse_reason%2Cis_sticky%2Ccollapsed_by%2Csuggest_edit%2Ccomment_count%2Ccan_comment%2Ccontent%2Ceditable_content%2Cvoteup_count%2Creshipment_settings%2Ccomment_permission%2Ccreated_time%2Cupdated_time%2Creview_info%2Crelevant_info%2Cquestion%2Cexcerpt%2Crelationship.is_authorized%2Cis_author%2Cvoting%2Cis_thanked%2Cis_nothelp%2Cis_labeled%2Cis_recognized%2Cpaid_info%2Cpaid_info_content%3Bdata%5B*%5D.mark_infos%5B*%5D.url%3Bdata%5B*%5D.author.follower_count%2Cbadge%5B*%5D.topics&offset=0&limit=20&sort_by=default&platform=desktop'
        answer_json = requests.get(answer_url, headers = headers).json()
        num1 = answer_json['paging']['totals']
        page = math.ceil(num1/20)
        #urls = []
        for j in range(page):
            url_1 = 'https://www.zhihu.com/api/v4/questions/'+str(que_id)+'/answers?include=data%5B*%5D.is_normal%2Cadmin_closed_comment%2Creward_info%2Cis_collapsed%2Cannotation_action%2Cannotation_detail%2Ccollapse_reason%2Cis_sticky%2Ccollapsed_by%2Csuggest_edit%2Ccomment_count%2Ccan_comment%2Ccontent%2Ceditable_content%2Cvoteup_count%2Creshipment_settings%2Ccomment_permission%2Ccreated_time%2Cupdated_time%2Creview_info%2Crelevant_info%2Cquestion%2Cexcerpt%2Crelationship.is_authorized%2Cis_author%2Cvoting%2Cis_thanked%2Cis_nothelp%2Cis_labeled%2Cis_recognized%2Cpaid_info%2Cpaid_info_content%3Bdata%5B*%5D.mark_infos%5B*%5D.url%3Bdata%5B*%5D.author.follower_count%2Cbadge%5B*%5D.topics&offset=' +str(j*20)+'&limit=20&sort_by=default&platform=desktop'
            time.sleep(1)
            json1 = requests.get(url_1, headers = headers).json()
            for k in json1['data']:
                ID = k['id']
                name = k['author']['name']
                text = k['excerpt']
                gender = k['author']['gender']
                follower_count = k['author']['follower_count']
                time1 = k['created_time']
                user_id = k['author']['id']
                comment_count = k['comment_count']
                zhantong = k['voteup_count']
                
                url_2 = 'https://api.zhihu.com/people/' + str(user_id)
                time.sleep(2)
                user_json = requests.get(url_2, headers = headers).json()
                #geren_des = user_json['description']
                try:    
                    hangye = user_json['business']['name']
                except:
                    hangye = 'none'
                try:
                    zhiyejingli = user_json['employment'][0][0]['name']
                except:
                    zhiyejingli = 'none'
                
                try:    
                    jiaoyu = user_json['education'][0]['name']
                except:
                    jiaoyu = 'none'
                dt = datetime.datetime.fromtimestamp(time1)
                time2 = dt.strftime("%Y-%m-%d %H:%M:%S")
                try:
                    fans = user_json['follower_count']
                except:
                    fans = 'none'
                try:
                    guanzhu = user_json['following_count']
                except:
                    guanzhu = 'none'
                try:
                    answer_count = user_json['answer_count']
                except:
                    answer_count = 'none'
                try:
                    question_count = user_json['question_count']
                except:
                    question_count = 'none'
                try:
                    articles_count = user_json['articles_count']
                except:
                    articles_count = 'none'
                
               # print(question,ID,name, text,gender,time2,hangye, zhiyejingli, jiaoyu,fans,guanzhu,
                   #   answer_count, question_count,articles_count)
                
                
                comment_url = 'https://www.zhihu.com/api/v4/answers/' + str(ID) + '/root_comments?order=normal&limit=20&offset=0&status=open'
                time.sleep(1)
                comment_json = requests.get(comment_url, headers = headers).json()
                if(comment_json['paging']['totals'] == 0):
                    comment = 'none'
                    continue
                else:
                    total = comment_json['paging']['totals']
                    page1 = math.ceil(total/20)
                    print('page:',page1)
                    for e in range(page1):
                        url_comm = 'https://www.zhihu.com/api/v4/answers/' + str(ID) + '/root_comments?order=normal&limit=20&offset='+str(e*20)+'&status=open'
                        time.sleep(1)
                        comment_json = requests.get(url_comm, headers = headers).json()
                        for M in comment_json['data']:
                            comment_id = M['id']
                            comment = M['content']
                            time_c = M['created_time']
                            dt1 = datetime.datetime.fromtimestamp(time_c)
                            time_comment = dt1.strftime("%Y-%m-%d %H:%M:%S")
                            name_comment = M['author']['member']['name']
                            sex_comment = M['author']['member']['gender']
                            url_c = M['author']['member']['url']
                            child = len(M['child_comments'])
                            
                            url_id1 = M['author']['member']['id']
                            url_user1 = 'https://api.zhihu.com/people/' + str(url_id1)
                            user_info = get_user(url_user1)
                            other = ','.join([name_comment,comment,time_comment,str(child),user_info])
                            print(comment_id)
                            huifu = []
                            huifu.append(other)
                            if(child != 0 ):
                            
                                for n in range(child):
                                    content1 = M['child_comments'][n]['content']
                                    name1 = M['child_comments'][n]['author']['member']['name']
                                    sex1 = M['child_comments'][n]['author']['member']['gender']
                                    toname1 = M['child_comments'][n]['reply_to_author']['member']['name']
                                    time_huifu1 = M['child_comments'][n]['created_time']
                                    
                                    dt2 = datetime.datetime.fromtimestamp(time_huifu1)
                                    time_huifu2 = dt2.strftime("%Y-%m-%d %H:%M:%S")
                                    
                                    url_id2 = M['child_comments'][n]['author']['member']['id']
                                    url_user2 = 'https://api.zhihu.com/people/' + str(url_id2)
                                    user_info2 = get_user(url_user2)
                                    other1 = ','.join([name1,toname1,content1,time_huifu2,user_info2])
                                    huifu.append(other1)
                            huifu_all = ';'.join(huifu)
                            print(huifu_all)
                                
                                
                            
                            
                        #print(comment_id,comment,time_comment,name_comment,
                            #  sex_comment,child)
                    
                
                            cursor = connect.cursor()
                            sql = "INSERT IGNORE INTO zhihu1(question,ID,name, text,gender,time,hangye,zhiyejingli, jiaoyu,fans,guanzhu,answer_count, question_count,articles_count,comment_id,comment_count,zhantong,huifu) VALUES ( '%s','%s', '%s', '%s','%s', '%s', '%s','%s','%s', '%s', '%s','%s', '%s', '%s', '%s','%s','%s','%s')"
                            data = (question,ID,name, text,gender,time2,hangye,zhiyejingli, jiaoyu,fans,guanzhu,
                                answer_count, question_count,articles_count,comment_id,comment_count,zhantong,huifu_all)
            #print data
                            try:
                                cursor.execute(sql % data)
                            except:
                                print(ID)

                            connect.commit()
                            
                        
                   
        



  
    
url = 'https://www.zhihu.com/api/v4/questions/'+str(que_id)+'/answers?include=data%5B*%5D.is_normal%2Cadmin_closed_comment%2Creward_info%2Cis_collapsed%2Cannotation_action%2Cannotation_detail%2Ccollapse_reason%2Cis_sticky%2Ccollapsed_by%2Csuggest_edit%2Ccomment_count%2Ccan_comment%2Ccontent%2Ceditable_content%2Cvoteup_count%2Creshipment_settings%2Ccomment_permission%2Ccreated_time%2Cupdated_time%2Creview_info%2Crelevant_info%2Cquestion%2Cexcerpt%2Crelationship.is_authorized%2Cis_author%2Cvoting%2Cis_thanked%2Cis_nothelp%2Cis_labeled%2Cis_recognized%2Cpaid_info%2Cpaid_info_content%3Bdata%5B*%5D.mark_infos%5B*%5D.url%3Bdata%5B*%5D.author.follower_count%2Cbadge%5B*%5D.topics&offset=3&limit=15&sort_by=default&platform=desktop'
log = 'http://piao.qunar.com/ticket/detailLight/sightCommentList.json?sightId=39037&index=1&page=1&pageSize=10&tagType=0'
requests.get(log, headers = head).json()

url = 'https://api.zhihu.com/people/55a03f1c27ebfa7c434d32b58584bf75'
def get_user(url):
    time.sleep(1)
    user_json = requests.get(url, headers = headers).json()
    
    try:
        headline = user_json['headline']
    except:
        headline = 'none'
        
    try:
        des = user_json['description']
    except:
        des = 'none'
    try:
        loc = user_json['location'][0]['name']
    except:
        loc = 'none'
    
    
                
    try:    
        hangye = user_json['business']['name']
    except:
        hangye = 'none'
    try:
        zhiyejingli = []
        for i in user_json['employment']:
            for j in i:
                name = j['name']
                zhiyejingli.append(name)
        zhiye = ','.join(zhiyejingli)
        
    except:
        zhiye = 'none'
                
    try:    
        jiaoyu = user_json['education'][0]['name']
    except:
        jiaoyu = 'none'
                
    try:
        fans = user_json['follower_count']
    except:
        fans = 'none'
    try:
        guanzhu = user_json['following_count']
    except:
        guanzhu = 'none'
    try:
        answer_count = user_json['answer_count']
    except:
        answer_count = 'none'
    try:
        question_count = user_json['question_count']
    except:
        question_count = 'none'
    try:
        articles_count = user_json['articles_count']
    except:
        articles_count = 'none'
        
    other = ','.join([headline,des,loc,hangye,zhiye, jiaoyu,str(fans),str(guanzhu),
             str(answer_count),str(question_count),str(articles_count)])
    return other