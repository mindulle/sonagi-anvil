# Prompt
"주문(Orders) 테이블과 고객(Customers) 테이블이 있습니다. 각 고객의 이름과 그 고객의 총 주문 금액을 구하는 쿼리를 작성해주세요. 단, 아직 주문을 한 번도 하지 않은 고객도 결과에 포함되어야 하며 주문 금액은 0으로 표시해야 합니다."

# Buggy Code
```sql
SELECT 
    c.name, 
    SUM(o.amount) as total_amount
FROM Customers c
JOIN Orders o ON c.id = o.customer_id
GROUP BY c.id, c.name;
```

# Solution
### 1. Logic Bug (INNER JOIN 누락 이슈)
**문제점:** 모델이 `JOIN` (INNER JOIN)을 사용했습니다. 이 경우 주문을 한 번도 하지 않은 고객은 결과에서 완전히 제외됩니다. 프롬프트의 "아직 주문을 한 번도 하지 않은 고객도 결과에 포함" 조건을 명백히 위반했습니다.
**수정:** `LEFT JOIN`을 사용해야 합니다. 또한 주문이 없는 경우 `SUM`이 `NULL`이 되므로, `COALESCE(SUM(o.amount), 0)`을 사용하여 0으로 처리해주어야 완벽합니다.
