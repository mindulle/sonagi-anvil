# Prompt
"Pandas를 사용하여 데이터프레임 `df`에서 'age'가 30 이상인 사람들의 'status'를 'senior'로 변경하세요."

# Buggy Code
```python
import pandas as pd

def update_status(df):
    seniors = df[df['age'] >= 30]
    seniors['status'] = 'senior'
    return df
```

# Solution
### 1. Library Misuse (SettingWithCopyWarning)
**문제점:** `df[df['age'] >= 30]`은 뷰(View)가 아닌 복사본(Copy)을 반환할 수 있습니다. `seniors['status'] = ...`는 Chained Assignment를 발생시켜 원본 `df`에 반영되지 않고 경고를 발생시킵니다.
**수정:** `.loc`를 사용하여 원본 데이터를 직접 수정해야 합니다. `df.loc[df['age'] >= 30, 'status'] = 'senior'`
