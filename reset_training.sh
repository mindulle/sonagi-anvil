#!/bin/bash
# 이 스크립트는 dsa_training 내의 모든 알고리즘 문제를 초기화(TODO 상태)합니다.
# 주의: 작성 중이던 모든 정답 코드가 삭제되니 실행 전 반드시 커밋하거나 백업하세요!

echo "🔄 DSA 훈련장을 초기화합니다..."
echo "----------------------------------------"

# .templates 폴더가 없으면 에러
if [ ! -d "dsa_training/.templates" ]; then
  echo "❌ 오류: dsa_training/.templates 디렉토리를 찾을 수 없습니다."
  exit 1
fi

# 템플릿 파일들을 원본 위치로 덮어쓰기
cp -r dsa_training/.templates/* dsa_training/

echo "✅ 모든 문제가 초기화되었습니다. 백지 상태에서 다시 TDD 훈련을 시작하세요!"
echo "명령어: cd dsa_training && pytest"
