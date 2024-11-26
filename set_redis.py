from __init__ import r

# Redis에 결과값 저장
def set_result(request_id, result):
    
    try:
        r.set(request_id, result, ex=60)
        value = r.get(request_id)
        print("redis 값 저장 완료")
        print(f"{request_id} = {value}")
    
    except Exception as e:
        print(f"Error: {e}") 