| 항목 | 내용 |
|:---|---|
| (4) 주요 기능의 구현 | <strong>1. 관심 키워드 기반 아티클 추천 기능</strong><br>관심 키워드 기반 아티클 추천 기능은 크게 세 가지 단계를 거쳐 구현된다. <br><br>먼저, 사용자가 관심사에 대해 간단히 입력하면, OpenAI를 통해 해당 입력과 관련된 키워드를 추출된다. 이때, 이전에 추출된 키워드가 있다면 이를 포함하여 새로운 키워드를 추출함으로써 사용자의 관심 분야를 확장하는 방식으로 키워드 목록을 갱신한다.<br><img src="" width="100" /><br><br>이후, 키워드 기반 기사 검색을 위해 미리 신뢰할 수 있는 언론사 목록을 작성하고, Custom Search JSON API를 사용하여 키워드와 언론사 정보를 바탕으로 쿼리를 구성하여 관련 기사 리스트를 추출한다.<br><img src="" width="100" /><br><br>마지막으로, 추출된 기사 목록과 사용자 입력을 활용하여 OpenAI를 통해 사용자 관심사와 퀴즈 출제에 가장 적합한 기사를 선정할 수 있도록 Instruction-based Prompting 기법을 활용해 기사를 추천하도록 요청한다. 이 과정을 통해 사용자는 자신의 관심에 맞는 기사들을 추천받을 수 있게 된다.<br><br>- 사용 기술: GPT-4o-mini, Custom Search JSON API <br><br><br><br><strong>2. 퀴즈와 서술형 퀴즈 피드백 생성</strong><br>퀴즈와 서술형 퀴즈 피드백 생성을 위해서는 아티클 스크래핑, 아티클 기반 퀴즈와 서술형 피드백 생성 과정을 거친다.<br><br>먼저 아티클을 스크래핑하기 전에 각 언론사의 도메인과 본문을 찾을 태그 및 클래스를 미리 매핑하여 SITE_CLASS_MAPPING 리스트를 작성한다.그 후, 최종 선택된 아티클을 기반으로 매핑 정보를 활용해 requests를 사용하여 HTML을 요청하고, BeautifulSoup으로 파싱하여 본문을 추출한다. 본문을 추출할 때는 텍스트 요소를 찾아 줄바꿈을 포함한 본문을 반환하며, 오류가 발생하면 None을 반환하도록 한다.<br><br>아티클 기반 퀴즈와 서술형 피드백 생성을 OpenAI로 처리하기 위해, 스크래핑을 통해 추출된 본문 텍스트를 OpenAI의 프롬프트에 적합한 크기와 형태로 가공해야 한다. 이를 위해 텍스트 분할 함수와 아티클 요약 함수를 사용하여 텍스트를 가공한다. 이후, 가공된 아티클 본문을 프롬프트에 포함시켜 Instruction-based Prompting 기법으로 아티클 기반 퀴즈와 서술형 피드백 생성을 요청하는 프롬프트를 구성한다. 다음 프롬프트로 OpenAI에게 아티클 기반 퀴즈와 서술형 피드백 생성을 요청하고, 요청 결과로 받은 퀴즈와 피드백 정보를 파싱하여 사용자에게 제공한다.<br><br>- 사용 기술: GPT-4o-mini, BeautifulSoup<br><br><br><br><strong>3.퀴즈봇 형식의 퀴즈 출제</strong><br> Django Channels를 이용한 실시간 WebSocket 통신을 구현하였다. 먼저, 실시간 통신을 위해 ASGI를 설정하여 WebSocket을 처리할 수 있도록 환경을 설정하고, URL 라우팅을 처리하였다. 이후, 클라이언트와의 통신을 위한 Consumer 클래스를 작성하여 웹소켓 연결과 채팅 형식의 실시간 퀴즈 데이터와 응답 메세지 처리를 구현하였다.<br><br>- 사용 기술: Django-channels, Redis<br><br><br><br><strong>4. 배틀 매칭</strong><br>경쟁 모드는 실시간 퀴즈 배틀 기능으로 Redis의 Queue 기능을 사용하여, 대기열에 추가된 접속 중인 사용자 두 명을 1:1로 매칭 시켜 배틀방을 생성하면서 시작한다.<br><br> 두 사용자가 동시에 배틀룸에 접속한 상태에서 배틀룸의 아티클과 퀴즈를 준비하고, 추천이 완료된 아티클 정보를 Django Channels의 group 메세지를 통해 두 사용자에게 동시에 전송한다. 이후 두 사용자에게 전송한 아티클 기반으로 생성된 동일한 퀴즈 3개를 제공하여 제한 시간 내에 더 높은 점수를 획득한 사용자가 이기는 게임 형식의 기능이다.<br><br>- 사용 기술: Django-channels, Redis|

