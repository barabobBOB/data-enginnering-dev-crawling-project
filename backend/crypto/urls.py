from django.urls import path
from . import apis

urlpatterns = [
    path(
        "api-v1/coinsync",
        apis.MarketCoinListCreateInitalization.as_view(),
        name="coin_sync"
    ),
    
    path(
        "api-v1/coinlist", 
        apis.CoinTotalListViewInitailization.as_view(), 
        name="coin_list"
    ),
    
    path(
        "api-v1/coindata",
         apis.CoinTradingCreateInitalization.as_view(),
         name="coin_data"
    ),
    
    path(
        "api-v1/cointrade",
        apis.TradeCoinDataViewInitailization.as_view(),
        name="coin_trade"
    ),
    
]
