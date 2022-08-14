from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import urllib.request
from logging import setLoggerClass
options=webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches',['enable-logging'])

driver=webdriver.Chrome(options=options)
#driver=webdriver.Chrome("경로")
driver.get('https://movie.naver.com/')
#drive.get('사이트주소')

#창 닫기 driver.close()
#창이동 driver.switch_to_window(driver.window_handies[number])
#두번쨰 창이 있을 때 .. . number에 창 번호를 넣어주면 됩니도 0번쨰부터 시작한다.


#xpath 접근 후 driver.find_element_by_xpath(xpathPaper)
#+ .
#get_attribute 요소의 속성 중 name에 해당하는 속성의 값을 추출
#send_keys(value) value에 해당하는 키를 입력
#text 요소 내부의 글자


#창 넘기는 함수 작성
def changeWindow(number):
    if number==0:
        driver.close()
    driver.switch_to.window(driver.window_handles[number])

xpathPaper='/html/body/div/div[3]/div/div[1]/div/div/ul/li[3]/a'
driver.find_element_by_xpath(xpathPaper).send_keys(Keys.CONTROL+'\n')
#ctrl+n을 누르면 새창이 열린다! 새창으로 열어주세요 이런 의미

#새창으로 열기
changeWindow(0)

#영화랭킹내에 1~10까지는 1씩 증가하는데 11은 13이 됨! 그니까 10단위마다 1씩 늘어나는거여
result=[]
count=0 #10마다 1씩 추가되는 기능을 제공하기 위해

for i in range(1,5):
    info=[]
    xpathPaper='/html/body/div/div[4]/div/div/div/div/div[1]/table/tbody/tr['+str(i+1+count)+']/td[2]/div/a'
    #문자형이라 str함수처리하고 1부터시작해서 i+1을 했음
    driver.find_element_by_xpath(xpathPaper).send_keys(Keys.CONTROL+'\n')
    #(i+1)등 페이지로 넘어가는 코드 
    changeWindow(1) 
    #그 창으로 넘어가 달라는 뜻
    title=driver.find_element_by_xpath('/html/body/div/div[4]/div[3]/div[1]/div[2]/div[1]/h3/a[1]').text
    director=driver.find_element_by_xpath('/html/body/div/div[4]/div[3]/div[1]/div[2]/div[1]/dl/dd[2]/p/a').text
    src=driver.find_element_by_xpath('/html/body/div/div[4]/div[3]/div[1]/div[2]/div[2]/a/img').get_attribute('src')
    #포스터사진 get_attribute("원하는 형태")
    #urllib.request.urlretrieve(src,title+'jpg') 
    # #이미지 파일로 저장!
    info.append(title)
    info.append(director)
    info.append(src)

    xpathPaper='/html/body/div/div[4]/div[3]/div[1]/div[3]/ul/li[6]/a' #리뷰창으로 이동해라
    driver.find_element_by_xpath(xpathPaper).send_keys(Keys.CONTROL+'\n')
    changeWindow(0)
    changeWindow(1)
    for comment_num in range(1,4): #리뷰세개
        try:
            review=driver.find_element_by_xpath('/html/body/div/div[4]/div[3]/div[1]/div[4]/div/div/div/div/ul/li['+str(comment_num)+']/a/strong').text
            info.append(review)
        except:#리뷰가 세개 미만이면
            continue #걍 넘어가자
    # 해당 영화 정보를 받아오고
    result.append(info)
    #영화 하나의 정보를 넣었음
    changeWindow(0)
    #정보 다 가져온 페이지는 닫아버리기

    
    if i %10==0 :
        count+=1


#터미널에 판다스 설치하고
#csv로 저장 진행

import pandas as pd
list_df=pd.DataFrame(result, columns=['제목','감독','사진','리뷰1','리뷰2','리뷰3'])
list_df.to_csv('크롤링 결과2.csv',index=False, encoding='euc-kr')

print(result) 
#우리가 만든 결과를 출력해주세요

