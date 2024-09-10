<과제 설명>  
Django DRF를 이용하여 스파르타마켓 구현  

<기본 조건>
-개별 과제  
-각 유저는 자신의 물건 등록  
-지역별 유저 고려X  
-필수 앱 -> accounts, products
-.gitignore 사용
-DRF 집중
-Postman 사용 권장  
  
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
 
