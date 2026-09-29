import yfinance as yf

# 1. 애플 (AAPL) 주식 종목 설정
ticker_symbol = "AAPL"

# 2. 주식 데이터 가져오기
ticker = yf.Ticker(ticker_symbol)

# 3. 최신 주가 정보 및 최신 5일간의 시세 정보 출력
info = ticker.info
hist = ticker.history(period="5d")

print(f"=== {info.get('shortName', ticker_symbol)} 주식 정보 ===")
print(f"현재 통화: {info.get('currency')}")
print(f"최근 종가: {info.get('previousClose')} {info.get('currency')}")
print("\n[최근 5일간 주가 흐름]")
print(hist[['Open', 'High', 'Low', 'Close', 'Volume']])