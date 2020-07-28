# 파이썬을 이용한 컴퓨터 과학 입문
- 북사이트 : https://introcs.cs.princeton.edu/python/home/
- 예제 소스 : https://introcs.cs.princeton.edu/python/code/
- 길벗 예제 소스 : https://github.com/gilbutITbook/006793

## 기본 패키지 설치 (우분투)
```python
# pygame 설치를 위한 라이브러리 설치
sudo apt-get build-dep python-pygame

# 파이썬 패키지 설치
pip install -r requirements.txt

# 책에서 사용하는 입출력 라이브러리 설치
cd introcs-1.0 && python setup.py install
```

## 디렉터리, 및 파일 구조
- `introcs-1.0` : 교재에서 사용되는 기본 라이브러리
- `<장>.<절>` : 예)1.1 = 1장 1절에 사용되는 코드 모음
  - `prac_<num>` : 연습 문제
  - `adv_<num>` : 심화 문제
