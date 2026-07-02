# Prompt
"초당 1,000개의 URL을 단축해야 하는 URL Shortener 서비스(예: bit.ly)의 아키텍처를 설계해줘. 데이터베이스 선택과 핵심 단축 알고리즘을 포함해야 해."

# Buggy Response
(모델의 답변 요약)
"데이터베이스로 관계형 DB(MySQL)를 사용하고, 사용자가 긴 URL을 입력하면 MD5 해시 함수를 사용하여 URL을 해싱한 뒤 앞 7자리를 잘라서 단축 URL 키로 사용합니다. 충돌이 발생하면 다시 해싱합니다."

# Solution
### 1. Algorithm Flaw (Hash Collision & Performance)
**문제점:** MD5 해시의 앞 7자리를 자르는 방식은 충돌(Collision) 확률이 높습니다. 충돌 시마다 DB에 쿼리를 던져 확인하고 다시 해싱하는 구조는 초당 1,000개의 쓰기 요청(TPS 1000)을 처리할 때 막대한 DB 부하를 유발합니다.
**수정:** `Base62` 인코딩과 분산 ID 생성기(예: Twitter Snowflake, 혹은 RDBMS의 Auto-increment ID를 활용한 Base62 변환), 또는 사전에 키를 생성해두는 Key Generation Service (KGS)와 ZooKeeper 조합을 제안하는 것이 모범 답안입니다.

### 2. Database Choice (Read/Write Heavy)
**문제점:** 단축 URL 서비스는 Read Heavy(보통 Read:Write = 10:1) 시스템입니다. MySQL 하나만 제안하기보다는, 빠른 리디렉션을 위해 Redis/Memcached 같은 캐시 레이어 도입이 필수적으로 언급되어야 합니다.
