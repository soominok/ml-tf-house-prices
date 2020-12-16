import pandas as pd
import numpy as np
import seaborn as from sns
import matplotlib as plt

'''
MSSubClass:  판매와 관련된 주거유형
MSZoning: 판매와 관련된 일반 구역 분류
LotFrontage: 부동산에 연결된 거리의 선형 피트
LotArea: 평방 피트 단위의 부지 크기
Street: 부동산에 대한 도로 접근 유형
Alley: 재산에 대한 골목 접근 유형
LotShape: 속성의 일반적인 모양
LandContour: 부동산의 평탄도
Utilities: 사용 가능한 유틸리티 유형
LotConfig: 로트 구성
LandSlope: 재산의 경사
Neighborhood: Ames시 경계 내의 물리적 위치
Condition1: 다양한 조건에 대한 근접성
Condition2: 다양한 조건에 대한 근접성 (둘 이상이 있는 경우)
BldgType: 주거 유형
HouseStyle: 주거 스타일
OverallQual: 집의 전체 재료와 마감 평가
OverallCond: 집의 전반적인 상태 평가
YearBuilt: 원래 건설 날짜
YearRemodAdd: 리모델링 날짜 (리모델링 또는 추가가 없는 경우 건설 날짜와 동일)
RoofStyle: 지붕 유형
RoofMatl: 지붕 재료
Exterior1st: 집 외부 커버
Exterior2nd: 집의 외부 커버 (하나 이상의 재료인 경우)
MasVnrType: 벽돌 겉치장 유형
MasVnrArea: 벽돌 겉치장 면적 (평방 피트)
ExterQual: 외부 재료의 품질 평가
ExterCond: 외장재의 현재 상태 평가
Foundation: 기초 유형
BsmtQual: 지하실 높이 평가
BsmtCond: 지하실의 일반적인 상태 평가
BsmtExposure: 파업 또는 정원 수준벽
BsmtFinType1: 지하실 마감 면적 등급
BsmtFinSF1: 유형 1 완성 평방 피트
BsmtFinType2: 지하실 마감 면적 등급 (여러 유형인 경우)
BsmtFinSF2: 유형 2 마감 평방 피트
BsmtUnfSF: 미완성된 지하실 면적
TotalBsmtSF: 지하 총 평방 피트
Heating: 난방 유형
HeatingQC: 난방 품질 및 상태
CentralAir: 중앙 에어컨
Electrical: 전기 시스템
1stFlrSF: 1층 평방 피트
2ndFlrSF: 2층 평방 피트
LowQualFinSF: 저품질 마감 평방 피트 (모든 층)
GrLivArea: 지상 거실 면적 평방 피트
BsmtFullBath: 지하 전체 욕실
BsmtHalfBath: 지하 반 욕실
FullBath: 등급 이상의 전체 욕실
HalfBath: 학년 이상의 전체 목욕
Bedroom: 위층 침실 (지하 침실은 포함 X)
Kitchen: 등급 이상의 부엌
KitchenQual: 주방 품질
TotRmsAbvGrd: 학년 이상의 총 방 (화장실 제외)
Functional: 홈 기능 (공제가 보장되지 않는 한 일반적으로 가정)
Fireplaces: 벽난로 수
FireplaceQu: 벽난로 품질
GarageType: 차고 위치
GarageYrBlt: 차고 건설 연도
GarageFinish: 차고 내부 마감
GarageCars: 차량 수용 가능 차고 크기
GarageArea: 차고 크기 (평방 피트)
GarageQual: 차고 품질
GarageCond: 사고 상태
PavedDrive: 포장된 진입로
WoodDeckSF: 목재 데크 면적 (평방 피트)
OpenPorchSF: 평방 피트 단위의 열린 현관 영역
EnclosedPorch: 닫힌 현관 영역 (평방 피트)
3SsnPorch: 평방 피트 단위의 3계절 현관 면적
ScreenPorch: 스크린 현관 영역 (평방 피트)
PoolArea: 수영장 면적 (평방 피트)
PoolQC: 수영장 품질
Fence: 울타리 품질
MiscFeature: 다른 카테고리에서 다루지 않는 기타 기능
MiscVal: 기타 기능의 $ 값
MoSold: 월 매출 (MM)
YrSold:  판매 연도 (YYYY)
SaleType: 판매 유형
SaleCondition: 판매 조건
'''