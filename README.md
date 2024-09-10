# spartamarket_DRF


## 1. Project name
spartamarket_DRF
<br/> 
## 2.Development time 
2024.09.06 ~ 09.10
 
## 3. Development Environment
-IDE : VSCODE
-Windows 10
-Python 3.10.14
-Django 4.2
-djangorestframework 3.15.2 
-djangorestframework-simplejwt 5.3.1

<br/>

## 4.Development member
배민석
<br/>
## 5.Development function
- 회원가입
- 로그인
- 프로필 조회
- 게시글 등록
- 게시글 수정
- 게시글 삭제
- 상품 목록 조회
<br/>
## 6. Project introduction
Django DRF를 이용하여 스파르타마켓 구현

<기본 조건>
-개별 과제  
-각 유저는 자신의 물건 등록  
-지역별 유저 고려X  
-필수 앱 -> accounts, products
-.gitignore 사용
-DRF 집중
-Postman 사용 권장
<과제 설명>  
Django DRF를 이용하여 스파르타마켓 구현  
  
<필수 구현>  
1. Accounts  
-회원가입: /api/accounts, POST  
-로그인: /api/accounts/login, POST  
-프로필 조회: api/accounts/<str:username>, GET  

*accounts 구현: UserSerializer 사용, 함수형 뷰  
**비밀번호 해싱 구현: make_password(password)  

2. Products  
-상품 등록: /api/products, POST  
-상품 목록 조회: /api/products, GET  
-상품 수정: /api/products/{productId}, PUT  
-상품 삭제: /api/products/{productId}, DELETE  

<br/>

## 7. project structure
```bash
spartamarket_DRF/
├── accounts/          # 사용자 관련 기능 (회원가입, 로그인, 프로필)
├── products/          # 상품 관련 기능 (등록, 조회, 수정, 삭제)
├── spartamarket_DRF/   # 메인 프로젝트 폴더 (설정 및 URL 설정)
└── manage.py          # Django 실행 파일
```
## ERD
![ERD](drf.drawio.png)
