import requests

bx_sent_cur = ['BTC','ETH','REP','BCH','XCN','DAS','DOG','EOS','EVX','FTC','GNO','HYP','LTC','NMC','OMG','PND','XPY','PPC','POW','XPM','XRP','ZEC','XZC','ZMN']
bt_sent_cur = ['BTC','ETH','REP','BCH','DAS','DOG','EOS','FTC','GNO','LTC','OMG','POW','XRP','ZEC','XZC']

temp_cur = [0]*5
temp_tradeA = [0]*5
temp_tradeB = [0]*5
temp_value = [0]*5

bt_price = [0]*300
bt_price_buy = [0]*300
bt_price_sell = [0]*300
bt_pair_name = [0]*300
bt_sell = [0]*300
bt_buy = [0]*300
bt_name_pri = [0]*300
bt_name_sec = [0]*300


getmarket_url ='https://bittrex.com/api/v1.1/public/getmarkets'




getmarket_data = requests.get(getmarket_url)
getmarket_data_json = getmarket_data.json()
market_name= getmarket_data_json['result']
for i in range(len(market_name)):
	try:

		if (market_name[i]['BaseCurrency'] in bx_sent_cur or market_name[i]['MarketCurrency'] in bx_sent_cur):
				
			order_url = 'https://bittrex.com/api/v1.1/public/getorderbook?market='+market_name[i]['MarketName']+'&type=both'
			#print(market_name[i]['MarketName'])
			order_data = requests.get(order_url)
			order_data_json = order_data.json()
			BDRbt_buy = order_data_json['result']['buy'][0]['Rate']
			BDRbt_sell = order_data_json['result']['sell'][0]['Rate']
			
			#print(" sell %s" %(BDRbt_sell))
			#print(" buy %s" %(BDRbt_buy))
			
			bt_name_pri[i] = market_name[i]['BaseCurrency']
			bt_name_sec[i] = market_name[i]['MarketCurrency']
			bt_price_sell[i] = BDRbt_sell
			bt_price_buy[i] = BDRbt_buy
	except:
		pass

for i in range(len(market_name)):
	try:

		if ((market_name[i]['BaseCurrency'] in bt_name_sec) and (market_name[i]['MarketCurrency'] in bx_sent_cur) and (bt_base_curr[i] == 0)):
				
			order_url = 'https://bittrex.com/api/v1.1/public/getorderbook?market='+market_name[i]['MarketName']+'&type=both'
			#print(market_name[i]['MarketName'])
			order_data = requests.get(order_url)
			order_data_json = order_data.json()
			BDRbt_buy = order_data_json['result']['buy'][0]['Rate']
			BDRbt_sell = order_data_json['result']['sell'][0]['Rate']
			
			#print(" sell %s" %(BDRbt_sell))
			#print(" buy %s" %(BDRbt_buy))
			
			bt_name_pri[i] = market_name[i]['BaseCurrency']
			bt_name_sec[i] = market_name[i]['MarketCurrency']
			bt_price_sell[i] = BDRbt_sell
			bt_price_buy[i] = BDRbt_buy

	except:
		pass

bt_fee = {'BTC':0.0005000,'ETH':0.0060000,'REP':0.1000000,'BCH':0.0010000,'DAS':0.0500000,'DOG':2.0000000,'EOS':0.0200000,'FTC':0.2000000,'GNO':0.0200000,'LTC':0.0100000,'OMG':0.3500000,'POW':5.0000000,'XRP':1.0000000,'ZEC':0.0050000,'XZC':0.0200000}
bx_fee = {'BTC':0.0005000,'ETH':0.0050000,'REP':0.0100000,'BCH':0.0001000,'XCN':0.0100000,'DAS':0.0050000,'DOG':5.0000000,'EOS':0.0001000,'EVX':0.0100000,'FTC':0.0100000,'GNO':0.0100000,'HYP':0.0100000,'LTC':0.0050000,'NMC':0.0100000,'OMG':0.2000000,'PND':2.0000000,'XPY':0.0050000,'PPC':0.0200000,'POW':0.0100000,'XPM':0.0200000,'XRP':0.0100000,'ZEC':0.0050000,'XZC':0.0050000,'ZMN':0.0100000}


bx_pair = requests.get('https://bx.in.th/api/pairing/')
bx_data_pair = bx_pair.json()
money = 2000 ;
bx_price = [0]*40
bx_price_buy = [0]*40
bx_price_sell = [0]*40
bx_name_pri = [0]*40
bx_name_sec = [0]*40

for i in range(1,34):
	try:
		bx_price[i] = requests.get('https://bx.in.th/api/orderbook/?pairing='+str(i))
		bx_price[i] = bx_price[i].json()
		bx_price_sell[i] = float(bx_price[i]['asks'][0][0])
		bx_price_buy[i] = float(bx_price[i]['bids'][0][0])
		bx_name_pri[i] = bx_data_pair[str(i)]['primary_currency']
		bx_name_sec[i] = bx_data_pair[str(i)]['secondary_currency']


	except:
		pass
#print(bx_price_sell[1])
#print(bx_price_buy[1])

THB_id = []
bx_cur_to_thb = []

for i in range(1,34):
	try:
		if(bx_data_pair[str(i)]['primary_currency']=='THB'):
			THB_id.append(i)
			bx_cur_to_thb.append(bx_data_pair[str(i)]['secondary_currency'])
	except:
		pass
#print(THB_id)
#print('***************************************')
#print(bx_name_pri)
#print(bx_name_sec)
#print(bx_price_sell)
#print(bx_price_buy)

#print('a')
for i in THB_id:
	value = money/bx_price_sell[i]
	value_cur = bx_data_pair[str(i)]['secondary_currency']
	#print("%f %s"%(value,value_cur))
	value = value-bx_fee[value_cur] #Send to bittrex
	temp_cur[0] = value_cur;
	temp_tradeA[0]=bx_data_pair[str(i)]['primary_currency']
	temp_tradeB[0]=bx_data_pair[str(i)]['secondary_currency']
	temp_value[0] = value
	#print('b')
	#---------------Sent to Bittrex ---------------
	for j in range(300):
		value = temp_value[0]
		if(temp_cur[0] == bt_name_pri[j]):
			value = value/bt_price_sell[j] 
			value_cur = bt_name_sec[j]
			temp_tradeA[1] = bt_name_pri[j]
			temp_tradeB[1] = bt_name_sec[j]
		elif(temp_cur[0] == bt_name_sec[j]):
			value = value*bt_price_buy[j]
			value_cur = bt_name_pri[j]
			temp_tradeA[1] = bt_name_sec[j]
			temp_tradeB[1] = bt_name_pri[j]
		else : continue
		temp_cur[1] = value_cur;
		temp_value[1] = value

		#print('c')
		for k in range(300):
			value = temp_value[1]
			if((bt_name_pri[k] or bt_name_sec[k]) in bt_sent_cur):
				if(temp_cur[1] == bt_name_pri[k]):
					value = value/bt_price_sell[k] 
					value_cur = bt_name_sec[k]
					temp_tradeA[2] = bt_name_pri[k]
					temp_tradeB[2] = bt_name_sec[k]
					
				elif(temp_cur[1] == bt_name_sec[k]):
					value = value*bt_price_buy[k]
					value_cur = bt_name_pri[k]
					temp_tradeA[2] = bt_name_sec[k]
					temp_tradeB[2] = bt_name_pri[k]
					#print(value_cur)
				if(not(value_cur in bt_sent_cur)):
					continue;
				value = value - bt_fee[value_cur]
				temp_cur[2] = value_cur;
				temp_value[2] = value
				#--------------Send back to Bx-------------
				#print('d')
				for l in range(40):
					value=temp_value[2]
					if((bx_name_sec[l] or bx_name_pri[l]) in bx_cur_to_thb):
						if(temp_cur[2] == bx_name_pri[l]):
							value = value/bx_price_sell[l] 
							value_cur = bx_name_sec[l]
							temp_tradeA[3]=bx_name_pri[l]
							temp_tradeB[3]=bx_name_sec[l]
						elif(temp_cur[2] == bx_name_sec[l]):
							value = value*bx_price_buy[l]
							value_cur = bx_name_pri[l]
							temp_tradeA[3]=bx_name_sec[l]
							temp_tradeB[3]=bx_name_pri[l]
						else : continue
						temp_cur[3] = value_cur;
						temp_value[3] = value
						#print('e')
						for m in THB_id:
							value = temp_value[3]
							if(temp_cur[3] == bx_name_sec[m]):
								value = value*bx_price_buy[m]
								temp_tradeA[4]=bx_name_sec[m]
								temp_tradeB[4]=bx_name_pri[m]
								value_cur = 'THB'
								temp_value[4] = value
								#print('zzz')
								print(value)
								print("THB > %s > %s > %s > %s >THB"%(temp_cur[0],temp_cur[1],temp_cur[2],temp_cur[3]))
								print("THB > %s/%s > %s/%s > %s/%s > %s/%s > %s/%s"%(temp_tradeA[0],temp_tradeB[0],temp_tradeA[1],temp_tradeB[1],temp_tradeA[2],temp_tradeB[2],temp_tradeA[3],temp_tradeB[3],temp_tradeA[4],temp_tradeB[4]))
								if(value > money):
									print("Result money %d   Profit %d" %(value,value-money))
									print("%s > %s > %s > %s >THB"%(temp_cur[0],temp_cur[1],temp_cur[2],temp_cur[3]))

