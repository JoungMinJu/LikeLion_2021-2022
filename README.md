# rest_api


<h5>API 뷰 감싸기</h5>
REST 프레임워크는 API 뷰를 작성하는 데 사용할 수 있는 두 가지 래퍼를 제공합니다.

@api_view 데코레이터를 함수 기반 뷰에서 사용할 수 있습니다.
APIView 클래스는 클래스 기반 뷰에서 사용할 수 있습니다.
이 래퍼들은 뷰에서 받은 Request에 몇몇 기능을 더하거나, 콘텐츠가 잘 변환되도록 Response에 특정 context를 추가합니다.
또한 때에 따라 405 Method Not Allowed를 반환하거나, request.data가 깨진 경우 ParseError 예외를 던지는 등의 일도 수행합니다.




![image](https://user-images.githubusercontent.com/81295661/136196809-5e37578e-1254-4bf3-9cfe-0a767f5b1b5b.png)



- 카카오 api 써보기

- 인프런강의 듣기 
- 노마드코더로 강의 듣기
- 자바 Spring 공부

