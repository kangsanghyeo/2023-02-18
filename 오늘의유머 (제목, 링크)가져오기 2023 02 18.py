import requests

headers = \
{'User-Agent':'Mozilla/5.0 (windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko'}

url = 'https://www.todayhumor.co.kr/board/list.php?table=bestofbest'
site = requests.get(url, headers=headers)
source_data = site.text

count1 = source_data.count('"subject"><a href=')

for i in range(count1):
      pos1 = source_data.find('"subject"><a href=')+ len('"subject"><a href=')
      source_data = source_data[pos1:]

      pos2 = source_data.find('target="_top">')
      a_data = source_data[:pos2]

      pos3 = source_data.find('=1" target="_top">')+ len('=1" target="_top">')
      source_data = source_data[pos3:]

      pos4 = source_data.find('</a><span class=')
      b_data = source_data[:pos4]


      
      url = 'https://www.todayhumor.co.kr'+a_data
      site = requests.get(url, headers=headers)
      source_data = site.text
       
      count2 = source_data.count('<p>    <img src=')/ 가져와야하는 이미지개수를 저장하기

      for i in range(count2):
            pos5 = source_data.find('<p>    <img src=')+ len('<p>    <img src=')/ 앞부분 지정하기
            source_data = source_data[pos5:]

            pos6 = source_data.find('alt="')/ 뒷부분 지정하기
            c_data = source_data[:pos6]
            
            source_data = source_data[pos6+1:]
            print(i+1, a_data, b_data, c_data)/ a_data내용과 b_data내용 c_data내용 출력하기
