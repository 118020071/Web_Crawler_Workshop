import requests, random, time, openpyxl, datetime, concurrent.futures, threading

time1 = datetime.datetime.now()
print("Code start at", datetime.datetime.strftime(time1,'%Y-%m-%d %H:%M:%S'))

## Section: modifiable global variable
## In this module, variable content can be altered

g_headers = []
with open("userAgent0.txt", "r") as f:
    while True:
        a = f.readline()
        if len(a) == 0:
            break
        a = a.replace("\n", "")
        g_headers.append(a)

proxyList = []
with open("proxy.txt", "r") as f2:
    while True:
        a = f2.readline()
        if len(a) == 0:
            break
        a = a.replace("\n", "")
        proxyList.append(a)
proxyIndex = 0

print(len(g_headers), len(proxyList))
## Section: unmodifiable global variable

videoList = []
threadList = []
videoDetailList = []
upInfoList = []

## Section: unify data

def deleteUnit(a):
    #例如有'万',则添加0
    if "万" in a:
        aTenThousand = a[0:a.find(".")]
        aLeftover = a[(a.find(".")+1):a.find("万")]
        a = int(aTenThousand)*10000 + int(aLeftover)*1000
    return str(a)

def unixTimeDecoding(value):
    #convert time in unix to yy:mm:dd hh:mm:ss
    format = '%Y-%m-%d %H:%M:%S'
    value = time.localtime(value)
    dt = time.strftime(format, value)

    return dt

## Section: get json response from a given url
## Variable: mother link, changing value in the link

def request_json(url, timeout=2):

    global g_headers, proxyList,proxyIndex

    fake_user_agent = { "User-Agent": g_headers[random.randint(0, len(g_headers)-1)]}
    proxy_num = proxyList[(proxyIndex)%len(proxyList)]
    proxyIndex += random.randint(1,min(len(g_headers),len(proxyList)))
    proxy = { "http": "http://"+proxy_num}

    html = requests.get(
        url = url,
        headers = fake_user_agent,
        proxies = proxy,
        timeout = timeout
    )

    # html = requests.get(
    #     url = url,
    #     headers = fake_user_agent,
    #     timeout = timeout
    # )

    response_data = html.json() # as type: dictionary
    # if "bvid" in url:
    html.close()
        
    return response_data

## Section: get detailed info

def get_aid(bvid):

    url = "https://api.bilibili.com/x/web-interface/view?bvid="+str(bvid)
    
    data = request_json(url)
    aid = data.get("data").get("aid")

    return aid

def get_videoInfo(bvid):
    
    url = "http://api.bilibili.com/x/web-interface/archive/stat?bvid="+str(bvid)

    i = 0
    while True:
        data = request_json(url)
        
        # form: aid,bvid,view,danmaku,reply,favorite,coin,share,like,now_rank,
        # his_rank,no_reprint,copyright,argue_msg,evaluation
        video_data = data.get("data")

        if video_data != None or str(video_data) != "None":
            # print(video_data)
            break
        # else:
            # print(bvid, video_data, "Trying to relink at time", i)
            # print(data)
            # time.sleep(random.randint(1,3))
            # i += 1
    #copyright == 1: 自制, 2: 转载

    # print(video_data, type(video_data))
    return video_data

def get_tagInfo(bvid):
    
    url = "https://api.bilibili.com/x/web-interface/view/detail/tag?bvid="+str(bvid)
    
    data = request_json(url)

    tag_data = data.get("data")

    whole_list = []
    tag_list = []

    for i in range(len(tag_data)):
        single_tag = tag_data[i]
        single_dict = {}
        single_dict["标签名称"] = single_tag.get("tag_name")
        single_dict["标签订阅数"] = single_tag.get("subscribed_count")
        single_dict["标签下视频数"] = single_tag.get("archive_count")
        single_dict["标签下精选视频数"] = single_tag.get("featured_count")

        whole_list.append(str(single_dict))
        tag_list.append(single_tag.get("tag_name"))

    # print(';'.join(whole_list), ','.join(tag_list))
    return ';'.join(whole_list), ','.join(tag_list)

def get_up_info(uuid):

    url = "https://api.bilibili.com/x/relation/stat?vmid="+str(uuid)

    data = request_json(url)

    up_data = data.get("data")

    up_info = {}

    up_info["following"] = up_data.get("following")
    up_info["follower"] = up_data.get("follower")

    # print(up_info)
    return up_info
## Section: get basic info

def getVideoDetails(pageNum, result, i):
    global videoList

    # //mode singleInfo.get("")
    singleInfo = result[i]
    ## Get info from searching page

    # Div: img-anchor
    videoLen = singleInfo.get("duration")#In array

    # Div: headline clearfix
    #subclass under headline clearfix
    videoType = singleInfo.get("typename")#In array
    title = singleInfo.get("title")#In array
    title = title.replace('<em class="keyword">',"")
    title = title.replace('</em>',"")
    videoBVid = singleInfo.get("bvid")
    videoLink = singleInfo.get("arcurl")
    if ("https" not in videoLink) and ("http" in videoLink):
        videoLink = videoLink.replace("http", "https")#In array

    # Div: des hide
    subscription = singleInfo.get("description")#In array

    # Div: tags
    uploadTime = singleInfo.get("pubdate")
    uploadTime = unixTimeDecoding(int(uploadTime))#In array
    updateTime = singleInfo.get("senddate")
    updateTime = unixTimeDecoding(int(updateTime))#In array
    
    UpName = singleInfo.get("author")#In array
    UpUUID = singleInfo.get("mid")#In array
    UpLink = "https://space.bilibili.com/"+str(UpUUID)#In array

    ## Get info of API-bilibili
    # api_info = get_videoInfo(videoBVid)
    # api_tagInfo, api_tag = get_tagInfo(videoBVid)
    # api_upInfo = get_up_info(UpUUID)

    ## Put infos into a dictionary
    # Video info
    infoDict = {}
    infoDict['搜索页位置'] = pageNum
    infoDict['UnixTimeStamp'] = singleInfo.get("pubdate")
    infoDict['视频分类'] = videoType
    infoDict['视频时常'] = videoLen
    infoDict['视频标题'] = title
    infoDict['视频url'] = videoLink
    infoDict['视频BV号'] = videoBVid
    infoDict['aid'] = singleInfo.get("aid")
    infoDict['视频简介'] = subscription
    infoDict['视频上传时间'] = uploadTime
    infoDict['视频重新上传时间'] = updateTime
    # if (api_info.get("no_reprint") == 0):
    #     infoDict['视频可转载'] = "不可转载"#作品可转载？
    # else: infoDict['视频可转载'] = "可转载"
    # if (api_info.get("copyright") == 1):
    #     infoDict['视频类型'] = "自制"#作品类型：自制/转载
    # else:   infoDict['视频类型'] = "转载"
    infoDict['视频标签'] = singleInfo.get("tag")
    # infoDict['视频标签详细信息'] = api_tagInfo
    # Viewer info
    infoDict['播放数'] = int(singleInfo.get("play"))
    infoDict['弹幕数'] = singleInfo.get("video_review")
    # infoDict['点赞数'] = api_info.get("like")
    # infoDict['投币数'] = api_info.get("coin")
    infoDict['收藏数'] = singleInfo.get("favorite")#收藏
    # infoDict["分享数"] = api_info.get("share")
    infoDict['评论数'] = singleInfo.get("review")
    # infoDict["本周视频排行"] = api_info.get("now_rank")
    # infoDict["历史视频排行"] = api_info.get("his_rank")
    # Up info
    infoDict['Up名字'] = UpName
    if singleInfo.get("is_union_video") == 0:
        infoDict['Up名字'] = "否"
    else:
        infoDict['Up名字'] = "是"
    infoDict['视频总体排位分数'] = singleInfo.get("rank_score")
    # infoDict['Up粉丝数'] = api_upInfo.get("follower")#粉丝数
    # infoDict['Up关注列表数'] = api_upInfo.get("following")#Up关注数
    infoDict['Up空间URL'] = UpLink
    infoDict['Up的uuid'] = UpUUID

    for key, value in infoDict.items():
        value = str(value)
        value = value.replace('\n', '')
        infoDict[key] = value.strip()

    videoList.append(infoDict)

## Section: start getVideoDetails with multiple thread

def getVideoLinks(url):
    global threadList

    data = request_json(url)
    while (data.get("data") == None or data.get("data") == "None"):
        # print(data)
        data = request_json(url)
    if len(data.get("data")) < 6:
        print(data)
    html = data.get("data")

    pageNum = str(html.get("page"))
    pageSize = int(html.get("pagesize"))
    result = html.get("result") #list object, with dict element

    if result != None:#exception handler
        for i in range(0, pageSize):
            if i < len(result):#exception handler
                x = threading.Thread(target=getVideoDetails,  args=(pageNum, result, i))
                x.start()
                threadList.append(x)

def startSearch(keywords = '-海遥-', searchType = 'click', duration = 0, max_thread = 20):

    global threadList
    
    url = "https://api.bilibili.com/x/web-interface/search/type?;order="+searchType+"&search_type=video&keyword="+keywords+"&duration="+str(duration)+"&page="

    urlList = []
    for i in range(1, 51):
        urlList.append(url+str(i))

    with concurrent.futures.ThreadPoolExecutor(max_workers=max_thread) as executor:
        # Start the load operations and mark each future with its URL
        future_to_url = [executor.submit(getVideoLinks, url) for url in urlList]

        index = 1
        length = len(future_to_url)
        for future in concurrent.futures.as_completed(future_to_url):
            # url = future_to_url[future]
            try:
                pass
                print("Finished at %d/%d"%(index, length), end='\r')
                index += 1
            except:
                print("Page %d generate exception"%future_to_url.index(future))

    executor.shutdown(wait=True)
    for i in threadList:
        i.join()

## Section: after get basic info, start to get detailed info

def getBasicInfo(bvid):
    global videoDetailList, videoList

    while True:
        try:
            api_info = get_videoInfo(bvid)
            if api_info.get("aid") != None:
                break
        except: pass
    # print(api_info)

    # print(api_info)
    infoDict = {}

    infoDict['aid'] = api_info.get('aid')
    if (api_info.get("no_reprint") == 0):
        infoDict['视频可转载'] = "不可转载"#作品可转载？
    else: infoDict['视频可转载'] = "可转载"
    if (api_info.get("copyright") == 1):
        infoDict['视频类型'] = "自制"#作品类型：自制/转载
    else:   infoDict['视频类型'] = "转载"
    infoDict['点赞数'] = int(api_info.get("like"))
    infoDict['投币数'] = api_info.get("coin")
    infoDict["分享数"] = api_info.get("share")
    infoDict["本周视频排行"] = api_info.get("now_rank")
    infoDict["历史视频排行"] = api_info.get("his_rank")

    # print(infoDict)
    # print(infoDict)
    
    videoDetailList.append(infoDict)

def getBasicInfo_start(max_thread = 400):
    global videoList, videoDetailList

    # time.sleep(10)
    BV_list = [i.get("视频BV号") for i in videoList]

    # time.sleep(10)
    # bv_file = open("bv_file.txt", "w")
    # for i in BV_list:
    #     print(i, file=bv_file)
    # print(BV_list)
    length = len([i.get("视频BV号") for i in videoList if i.get("视频BV号") != None])
    print("valid BV list at length", length)

    # fi = open("videoBasic.txt", "w")
    # print("len(videoList)", len(videoList))
    # print(BV_list)
    # for i in BV_list:
    #     print(i, file=fi)
    # fi.close()


    
    with concurrent.futures.ThreadPoolExecutor(max_workers=max_thread) as executor:
        future_to_url = [executor.submit(getBasicInfo, bvid) for bvid in BV_list]

        index = 1
        length = len(future_to_url)
        # print(length)
        for future in concurrent.futures.as_completed(future_to_url):
            # url = future_to_url[future]
            try:
                # pass
                # print("",end="")
                print("Finished at %d/%d with existing data size %d"%(index, length, len(videoDetailList)), end='\r')
                index += 1
            except:
                print("Page %d generate exception"%future_to_url.index(future))

    executor.shutdown(wait=True)



    # index = 0
    # for bvid in BV_list:
    #     # length = len(future_to_url)
    #     getBasicInfo(bvid)
    #     print("Finished at %d/%d with existing data size %d"%(index, length, len(videoDetailList)), end='\r')
    #     index += 1






    ## Wait until all getVideoDetails thread is terminated
    videoDetailList = sorted(videoDetailList, key=lambda k: k['aid'])
    videoList = sorted(videoList, key=lambda k: k['aid'])
    # print(len(videoList), len(videoDetailList))
    # print(videoDetailList)
    # print()
    # concatenate two dictionaries
    # for i in videoDetailList:
    #     print(i)
    for i in range(len(videoList)):
        videoList[i].update(videoDetailList[i])

## Section: writing info
def writingInfo(sheet):

    global videoList

    if len(videoList) == 0: #exception handler
        return None
    # Initialize excel
    index = 1
    TitleRow = [i for i in videoList[0].keys()]
    for i in range(len(TitleRow)):
        sheet.cell(row = index, column = i+1).value = TitleRow[i]
    index += 1

    for subDict in videoList:
        colIndex = 1
        for subKey, subValue in subDict.items():
            try:
                sheet.cell(row = index, column = colIndex).value = subValue
            except:
                try:
                    print("Cannot write at", "row:", index, "column:", colIndex, "content:",subValue)
                except:
                    print("Invalid Input at", "row:", index, "column:", colIndex)
            colIndex += 1
        print("Writing data at", index, "/", len(videoList), end='\r')
        index += 1

def getWorkbook(dataType = 1):
    global book, videoList

    if (dataType == 1):
        videoList = sorted(videoList, key=lambda k: k['UnixTimeStamp'], reverse=True) 
        sheet1 = book.create_sheet("MostNew", 0)
        writingInfo(sheet1)
    elif (dataType == 2):
        sheet2 = book.create_sheet("MostView", 1)
        writingInfo(sheet2)

if __name__ == "__main__":
    keyword = '马保国'
    book = openpyxl.Workbook()
    today = time.strftime("%Y-%m-%d", time.localtime())
    bookname = "Video_about "+keyword+" at "+today+".xlsx"
    book.save(bookname)

    startSearch(keyword, 'pubdate', 0)
    videoList = sorted(videoList, key=lambda k: k['播放数'], reverse=True) 
    getBasicInfo_start()
    # print(videoList)
    getWorkbook(1)
    book.save(bookname)




    time2 = datetime.datetime.now()
    print("End start at", datetime.datetime.strftime(time2,'%Y-%m-%d %H:%M:%S'))