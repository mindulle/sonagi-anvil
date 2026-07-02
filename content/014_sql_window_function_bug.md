# Prompt
"직원(Employee) 테이블에서 부서(department_id)별로 가장 높은 급여(salary)를 받는 직원의 이름과 급여를 구하는 SQL 쿼리를 작성해줘."

# Buggy Code
```sql
SELECT name, MAX(salary)
FROM Employee
GROUP BY department_id;
```

# Solution
### 1. SQL Standard Violation (GROUP BY 에러)
**문제점:** 대부분의 모던 RDBMS(PostgreSQL, SQL Server 등)에서는 `GROUP BY` 절에 포함되지 않은 일반 컬럼(`name`)을 SELECT 절에서 집계 함수 없이 사용할 수 없습니다. (MySQL의 특정 설정에서는 동작할 수 있으나 표준이 아닙니다.)
**수정:** `RANK()` 또는 `ROW_NUMBER()` 같은 윈도우 함수(Window Function)를 사용하거나 서브쿼리 조인을 통해 해결해야 합니다.

### 2. Ideal English Feedback
"The generated SQL is invalid in standard RDBMS like PostgreSQL or SQL Server. You cannot select the `name` column without including it in the `GROUP BY` clause or wrapping it in an aggregate function. To find the employee with the highest salary per department, you should use a window function like `RANK() OVER (PARTITION BY department_id ORDER BY salary DESC)` or use a subquery to join the max salaries back to the original table."
