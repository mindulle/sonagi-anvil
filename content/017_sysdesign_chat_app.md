# Prompt
"WhatsApp과 같은 실시간 채팅 앱의 백엔드를 설계해주세요. 사용자는 메시지를 보내고 지연 없이 수신해야 합니다."

# Buggy Response
(모델의 답변 요약)
"사용자는 REST API 엔드포인트 `POST /messages`를 통해 메시지를 서버에 보냅니다. 다른 사용자들은 매초마다 `GET /messages`를 호출하는 HTTP Polling 방식을 사용하여 새로운 메시지가 있는지 확인하고 화면을 업데이트합니다."

# Solution
### 1. Protocol Inefficiency (HTTP Polling)
**문제점:** 매초 수백만 명의 사용자가 HTTP Polling을 수행하면 서버 트래픽과 리소스가 낭비되고 서버는 곧 다운됩니다. 실시간 채팅 앱에서는 절대 권장되지 않는 안티패턴입니다.
**수정:** Persistent Connection을 유지하는 **WebSocket** 프로토콜이나 Server-Sent Events (SSE)를 사용해야 합니다. 
### 2. Scalability (Pub/Sub 누락)
**수정:** 백엔드 서버가 여러 대일 경우, 사용자 A가 접속한 서버와 사용자 B가 접속한 서버가 다를 수 있습니다. 이 경우 서버 간 메시지를 라우팅하기 위해 **Redis Pub/Sub**나 Kafka 같은 Message Broker 도입을 언급해야 합니다.
