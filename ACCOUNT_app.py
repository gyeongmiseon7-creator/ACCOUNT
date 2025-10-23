# 💰 모임 회계 관리 시스템

두 개의 모임을 동시에 관리할 수 있는 수입/지출 관리 프로그램입니다.

## 주요 기능

### 현재 구현된 기능
- ✅ 2개 모임 동시 관리
- ✅ 수입/지출 입력 및 관리
- ✅ 거래 내역 조회 및 필터링
- ✅ 모임별 요약 통계 (총 수입, 총 지출, 잔액)
- ✅ 거래 내역 CSV 다운로드
- ✅ 모임 이름 커스터마이징
- ✅ 데이터 로컬 저장 (JSON)

### 향후 추가 예정
- 🔄 영수증 이미지 OCR 인식
- 🔄 차트 및 그래프 시각화
- 🔄 월별/연도별 통계

## 설치 방법

1. 저장소 클론
```bash
git clone <your-repo-url>
cd meeting-expense-manager
```

2. 필요한 패키지 설치
```bash
pip install -r requirements.txt
```

3. 앱 실행
```bash
streamlit run app.py
```

## GitHub와 Streamlit Cloud 배포

### 1. GitHub 저장소 생성
1. GitHub에서 새 저장소 생성
2. 로컬 저장소 초기화 및 푸시
```bash
git init
git add .
git commit -m "Initial commit"
git remote add origin <your-repo-url>
git push -u origin main
```

### 2. Streamlit Cloud 배포
1. [Streamlit Cloud](https://streamlit.io/cloud) 접속
2. GitHub 계정으로 로그인
3. "New app" 클릭
4. 저장소, 브랜치, 메인 파일(app.py) 선택
5. "Deploy" 클릭

## 사용 방법

### 기본 사용
1. 사이드바에서 관리할 모임 선택
2. "거래 입력" 탭에서 수입/지출 등록
3. "내역 조회" 탭에서 거래 내역 확인 및 관리

### 모임 이름 변경
- 사이드바의 "모임 이름 관리"에서 각 모임의 이름을 원하는 대로 변경할 수 있습니다.

### 데이터 관리
- 모든 데이터는 `meeting_data.json` 파일에 자동 저장됩니다.
- CSV 다운로드 기능으로 데이터를 백업할 수 있습니다.

## 파일 구조
```
meeting-expense-manager/
├── app.py                 # 메인 Streamlit 앱
├── requirements.txt       # 필요한 패키지들
├── README.md             # 프로젝트 설명
└── meeting_data.json     # 데이터 저장 파일 (자동 생성)
```

## 향후 개선 계획

### 이미지 OCR 기능 추가
영수증 이미지에서 자동으로 정보를 추출하는 기능을 추가할 예정입니다.

**필요한 작업:**
1. OCR API 선택 (Google Cloud Vision, CLOVA OCR, Tesseract 등)
2. 이미지 업로드 및 전처리
3. 텍스트 추출 및 파싱
4. 추출된 정보 확인 및 수정 UI

**추천 OCR 솔루션:**
- **무료:** Tesseract OCR (오픈소스, 한글 지원)
- **유료:** 
  - Google Cloud Vision API (정확도 높음)
  - NAVER CLOVA OCR (한국어 특화)
  - AWS Textract

## 라이선스
MIT License

## 문의
이슈나 개선 사항은 GitHub Issues를 통해 남겨주세요.
