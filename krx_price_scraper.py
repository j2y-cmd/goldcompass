import requests
from bs4 import BeautifulSoup

url = "https://data.krx.co.kr/contents/MMC/ISIF/isif/MMCISIF016.cmd"

# 간혹 사이트에 따라 User-Agent 헤더가 필요함
headers = {'User-Agent': 'Mozilla/5.0'}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    price_element = soup.find('li', class_='indexPrice', attrs={'data-bind': 'TDD_CLSPRC'})
    if price_element:
        print(price_element)
        price_value = price_element.text.strip()
        print(price_value)  # 출력: 194,850
    else:
        print("해당 요소를 찾지 못했습니다.")
else:
    print("페이지를 가져오는데 실패했습니다, 상태 코드:", response.status_code)
