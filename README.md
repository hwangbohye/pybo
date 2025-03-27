| 항목 | 내용 |
|:---  |---  |
| (4) 주요 기능의 구현 | ## 1. 관심 키워드 기반 아티클 추천 기능 
관심 키워드 기반 아티클 추천 기능은 크게 세 가지 단계를 거쳐 구현된다.<br>첫 번째로, 사용자가 관심사에 대해 간단히 입력하면, OpenAI를 통해 해당 입력과 관련된 키워드를 추출된다. 이때, 이전에 추출된 키워드가 있다면 이를 포함하여 새로운 키워드를 추출함으로써 사용자의 관심 분야를 확장하는 방식으로 키워드 목록을 갱신한다.<br> 두 번째로, 키워드 기반 기사 검색을 위해 미리 신뢰할 수 있는 언론사 목록을 작성하고, Custom Search JSON API를 사용하여 키워드와 언론사 정보를 바탕으로 쿼리를 구성하여 관련 기사 리스트를 추출한다. 마지막으로, 추출된 기사 목록과 사용자 입력을 활용하여 OpenAI를 통해 사용자 관심사와 퀴즈 출제에 가장 적합한 기사를 선정할 수 있도록 Instruction-based Prompting 기법을 활용해 기사를 추천하도록 요청한다. 이 과정을 통해 사용자는 자신의 관심에 맞는 기사들을 추천받을 수 있게 된다.<br><br>
(1) **사용 기술:** GPT-4o-mini, Custom Search JSON API, <br>|
