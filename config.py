import os

PRODUCTION = "production"
DEVELOPMENT = "development"

COIN_TARGET = "BTC"
COIN_REFER = "USDT"

ENV = os.getenv("ENVIRONMENT", PRODUCTION)
DEBUG = True

BINANCE = {
  "key": "Gq8PfHlamdq5xK2u2SSNLTupiUC2Rxv8O2VtWTjHgFCYRtycZnNBGFZMctA9i8Y1",
  "secret": "zouTLLMi8xdB8FMEhbuLjJPNP0SkK6EnfqnAMLGvBeSzi64MjnL8M7lggDmsWMmF"
}

TELEGRAM = {
  "channel": "111",
  "bot": "222"
}

print("ENV = ", ENV)