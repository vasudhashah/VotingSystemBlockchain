from django.urls import path
from . import views
app_name="BlockchainApp"

urlpatterns = [
    path('blockchain/',views.route_blockchain,name='route_blockchain'),
    path('blockchain/range/',views.route_blockchain_range,name='route_blockchain_range'),
    path('blockchain/length/',views.route_blockchain_length,name='route_blockchain_length'),
    path('blockchain/mine/',views.route_blockchain_mine,name='route_blockchain_mine'),
    path('wallet/transact/',views.route_wallet_transact,name='route_wallet_transact'),
    path('transactions/',views.route_transactions,name='route_transactions'),


]
