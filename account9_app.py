import streamlit as st
import pandas as pd
from datetime import datetime
import json
import os

# 페이지 설정
st.set_page_config(page_title="모임 회계 관리", page_icon="💰", layout="wide")

# 데이터 파일 경로
DATA_FILE = "meeting_data.json"

# 데이터 로드 함수
def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            data = json.load(f)
            # 기존 데이터에 categories가 없으면 추가
            for meeting_id in data:
                if "categories" not in data[meeting_id]:
                    data[meeting_id]["categories"] = {
                        "수입": ["회비", "기타수입"],
                        "지출": ["식사비", "간식비", "교통비", "주유비", "숙박비", "기타지출"]
                    }
            return data
    else:
        return {
            "모임1": {
                "name": "모임1", 
                "transactions": [],
                "categories": {
                    "수입": ["회비", "기타수입"],
                    "지출": ["식사비", "간식비", "교통비", "주유비", "숙박비", "기타지출"]
                }
            },
            "모임2": {
                "name": "모임2", 
                "transactions": [],
                "categories": {
                    "수입": ["회비", "기타수입"],
                    "지출": ["식사비", "간식비", "교통비", "주유비", "숙박비", "기타지출"]
                }
            }
        }

# 데이터 저장 함수
def save_data(data):
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

# 세션 상태 초기화
if 'data' not in st.session_state:
    st.session_state.data = load_data()

# 타이틀
st.title("💰 모임 회계 관리 시스템")
st.markdown("---")

# 사이드바 - 모임 선택 및 설정
with st.sidebar:
    st.header("설정")
    
    # 모임 이름 변경
    st.subheader("모임 이름 관리")
    for meeting_id in ["모임1", "모임2"]:
        new_name = st.text_input(
            f"{meeting_id} 이름", 
            value=st.session_state.data[meeting_id]["name"],
            key=f"name_{meeting_id}"
        )
        if new_name != st.session_state.data[meeting_id]["name"]:
            st.session_state.data[meeting_id]["name"] = new_name
            save_data(st.session_state.data)
    
    st.markdown("---")
    
    # 항목 관리
    st.subheader("항목 관리")
    
    # categories 키가 없으면 초기화
    if "categories" not in st.session_state.data[selected_meeting]:
        st.session_state.data[selected_meeting]["categories"] = {
            "수입": ["회비", "기타수입"],
            "지출": ["식사비", "간식비", "교통비", "주유비", "숙박비", "기타지출"]
        }
        save_data(st.session_state.data)
    
    # 수입 항목 관리
    with st.expander("수입 항목 관리"):
        income_categories = st.session_state.data[selected_meeting]["categories"].get("수입", [])
        st.write("현재 수입 항목:")
        for cat in income_categories:
            col1, col2 = st.columns([3, 1])
            with col1:
                st.text(cat)
            with col2:
                if st.button("삭제", key=f"del_income_{cat}_{selected_meeting}"):
                    st.session_state.data[selected_meeting]["categories"]["수입"].remove(cat)
                    save_data(st.session_state.data)
                    st.rerun()
        
        new_income_category = st.text_input("새 수입 항목 추가", key=f"new_income_{selected_meeting}")
        if st.button("수입 항목 추가", key=f"add_income_{selected_meeting}"):
            if new_income_category and new_income_category not in income_categories:
                st.session_state.data[selected_meeting]["categories"]["수입"].append(new_income_category)
                save_data(st.session_state.data)
                st.success(f"'{new_income_category}' 항목이 추가되었습니다!")
                st.rerun()
    
    # 지출 항목 관리
    with st.expander("지출 항목 관리"):
        expense_categories = st.session_state.data[selected_meeting]["categories"].get("지출", [])
        st.write("현재 지출 항목:")
        for cat in expense_categories:
            col1, col2 = st.columns([3, 1])
            with col1:
                st.text(cat)
            with col2:
                if st.button("삭제", key=f"del_expense_{cat}_{selected_meeting}"):
                    st.session_state.data[selected_meeting]["categories"]["지출"].remove(cat)
                    save_data(st.session_state.data)
                    st.rerun()
        
        new_expense_category = st.text_input("새 지출 항목 추가", key=f"new_expense_{selected_meeting}")
        if st.button("지출 항목 추가", key=f"add_expense_{selected_meeting}"):
            if new_expense_category and new_expense_category not in expense_categories:
                st.session_state.data[selected_meeting]["categories"]["지출"].append(new_expense_category)
                save_data(st.session_state.data)
                st.success(f"'{new_expense_category}' 항목이 추가되었습니다!")
                st.rerun()리"):
        expense_categories = st.session_state.data[selected_meeting].get("categories", {}).get("지출", [])
        st.write("현재 지출 항목:")
        for cat in expense_categories:
            col1, col2 = st.columns([3, 1])
            with col1:
                st.text(cat)
            with col2:
                if st.button("삭제", key=f"del_expense_{cat}"):
                    st.session_state.data[selected_meeting]["categories"]["지출"].remove(cat)
                    save_data(st.session_state.data)
                    st.rerun()
        
        new_expense_category = st.text_input("새 지출 항목 추가", key="new_expense")
        if st.button("지출 항목 추가", key="add_expense"):
            if new_expense_category and new_expense_category not in expense_categories:
                if "categories" not in st.session_state.data[selected_meeting]:
                    st.session_state.data[selected_meeting]["categories"] = {"수입": [], "지출": []}
                st.session_state.data[selected_meeting]["categories"]["지출"].append(new_expense_category)
                save_data(st.session_state.data)
                st.success(f"'{new_expense_category}' 항목이 추가되었습니다!")
                st.rerun()
    
    st.markdown("---")
    
    # 모임 선택
    selected_meeting = st.radio(
        "관리할 모임 선택",
        ["모임1", "모임2"],
        format_func=lambda x: st.session_state.data[x]["name"]
    )
    
    st.markdown("---")
    
    # 데이터 초기화
    if st.button("모든 데이터 초기화", type="secondary"):
        if st.checkbox("정말 초기화하시겠습니까?"):
            st.session_state.data = {
                "모임1": {
                    "name": "모임1", 
                    "transactions": [],
                    "categories": {
                        "수입": ["회비", "기타수입"],
                        "지출": ["식사비", "간식비", "교통비", "주유비", "숙박비", "기타지출"]
                    }
                },
                "모임2": {
                    "name": "모임2", 
                    "transactions": [],
                    "categories": {
                        "수입": ["회비", "기타수입"],
                        "지출": ["식사비", "간식비", "교통비", "주유비", "숙박비", "기타지출"]
                    }
                }
            }
            save_data(st.session_state.data)
            st.success("데이터가 초기화되었습니다!")
            st.rerun()

# 현재 선택된 모임
current_meeting = st.session_state.data[selected_meeting]
meeting_name = current_meeting["name"]

# 메인 영역을 두 개의 탭으로 구성
tab1, tab2, tab3 = st.tabs(["거래 입력", "내역 조회", "이미지 입력 (준비중)"])

# 탭 1: 거래 입력
with tab1:
    st.header(f"{meeting_name} - 거래 입력")
    
    col1, col2 = st.columns(2)
    
    with col1:
        transaction_type = st.selectbox("구분", ["수입", "지출"])
        date = st.date_input("날짜", datetime.now())
        
    with col2:
        # 선택된 구분에 따라 항목 목록 가져오기
        available_categories = st.session_state.data[selected_meeting].get("categories", {}).get(transaction_type, [])
        
        # 드롭다운과 직접 입력 옵션
        category_option = st.radio("항목 선택 방법", ["목록에서 선택", "직접 입력"], horizontal=True)
        
        if category_option == "목록에서 선택":
            if available_categories:
                category = st.selectbox("항목", available_categories)
            else:
                st.warning("등록된 항목이 없습니다. 사이드바에서 항목을 추가하거나 '직접 입력'을 선택하세요.")
                category = ""
        else:
            category = st.text_input("항목", placeholder="예: 회비, 식사비, 간식비 등")
    
    amount = st.number_input("금액 (원)", min_value=0, step=1000)
    description = st.text_area("상세 내용", placeholder="거래에 대한 추가 설명을 입력하세요")
    
    if st.button("저장", type="primary", use_container_width=True):
        if amount > 0 and category:
            new_transaction = {
                "date": date.strftime("%Y-%m-%d"),
                "type": transaction_type,
                "category": category,
                "amount": amount,
                "description": description,
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
            st.session_state.data[selected_meeting]["transactions"].append(new_transaction)
            save_data(st.session_state.data)
            st.success("거래가 저장되었습니다!")
            st.rerun()
        else:
            st.error("금액과 항목을 모두 입력해주세요.")

# 탭 2: 내역 조회
with tab2:
    st.header(f"{meeting_name} - 거래 내역")
    
    transactions = current_meeting["transactions"]
    
    if len(transactions) > 0:
        # 데이터프레임 생성
        df = pd.DataFrame(transactions)
        df['amount_signed'] = df.apply(lambda x: x['amount'] if x['type'] == '수입' else -x['amount'], axis=1)
        
        # 요약 정보
        col1, col2, col3, col4 = st.columns(4)
        
        total_income = df[df['type'] == '수입']['amount'].sum()
        total_expense = df[df['type'] == '지출']['amount'].sum()
        balance = total_income - total_expense
        
        with col1:
            st.metric("총 수입", f"{total_income:,}원")
        with col2:
            st.metric("총 지출", f"{total_expense:,}원")
        with col3:
            st.metric("잔액", f"{balance:,}원", delta=f"{balance:,}원")
        with col4:
            st.metric("총 거래", f"{len(transactions)}건")
        
        st.markdown("---")
        
        # 필터링
        col1, col2 = st.columns(2)
        with col1:
            filter_type = st.multiselect("구분 필터", ["수입", "지출"], default=["수입", "지출"])
        with col2:
            categories = df['category'].unique().tolist()
            filter_category = st.multiselect("항목 필터", categories, default=categories)
        
        # 필터 적용
        filtered_df = df[df['type'].isin(filter_type) & df['category'].isin(filter_category)]
        
        # 거래 내역 표시
        st.subheader("거래 내역")
        
        # 정렬 옵션
        sort_order = st.radio("정렬", ["최신순", "오래된순"], horizontal=True)
        
        display_df = filtered_df.sort_values('date', ascending=(sort_order == "오래된순")).reset_index(drop=True)
        
        for display_idx, row in display_df.iterrows():
            # 원본 transactions 리스트에서의 실제 인덱스 찾기
            original_idx = None
            for i, trans in enumerate(transactions):
                if (trans['date'] == row['date'] and 
                    trans['type'] == row['type'] and 
                    trans['category'] == row['category'] and 
                    trans['amount'] == row['amount'] and
                    trans['timestamp'] == row['timestamp']):
                    original_idx = i
                    break
            
            with st.expander(f"{row['date']} | {row['type']} | {row['category']} | {row['amount']:,}원"):
                st.write(f"**금액:** {row['amount']:,}원")
                st.write(f"**구분:** {row['type']}")
                st.write(f"**항목:** {row['category']}")
                if row['description']:
                    st.write(f"**상세 내용:** {row['description']}")
                st.write(f"**등록 시간:** {row['timestamp']}")
                
                # 삭제 버튼
                if original_idx is not None and st.button("삭제", key=f"delete_{display_idx}_{row['timestamp']}"):
                    del st.session_state.data[selected_meeting]["transactions"][original_idx]
                    save_data(st.session_state.data)
                    st.success("삭제되었습니다!")
                    st.rerun()
        
        # CSV 다운로드
        st.markdown("---")
        csv = display_df.to_csv(index=False, encoding='utf-8-sig')
        st.download_button(
            label="CSV 다운로드",
            data=csv,
            file_name=f"{meeting_name}_transactions_{datetime.now().strftime('%Y%m%d')}.csv",
            mime="text/csv"
        )
        
    else:
        st.info("아직 등록된 거래 내역이 없습니다. '거래 입력' 탭에서 거래를 추가해보세요!")

# 탭 3: 이미지 입력 (준비중)
with tab3:
    st.header("영수증 이미지 인식 (준비중)")
    st.info("""
    향후 추가될 기능:
    - 영수증 이미지 업로드
    - OCR을 통한 금액, 날짜, 항목 자동 추출
    - 추출된 정보 확인 및 수정
    - 자동 저장
    
    이 기능을 구현하려면 다음이 필요합니다:
    - OCR API (예: Google Cloud Vision, Tesseract, CLOVA OCR 등)
    - 이미지 전처리
    - 텍스트 파싱 로직
    """)
    
    uploaded_file = st.file_uploader("영수증 이미지 업로드 (준비중)", type=['png', 'jpg', 'jpeg'], disabled=True)

# 푸터
st.markdown("---")
st.markdown("💡 Tip: 각 모임의 이름은 사이드바에서 변경할 수 있습니다.")
