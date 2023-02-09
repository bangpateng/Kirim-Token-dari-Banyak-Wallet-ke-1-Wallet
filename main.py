from web3 import Web3
import pandas as pd
import config
import time

def mulai():
    data = pd.read_csv('dataiblis.csv')
    jumlah_pengirim = data.shape[0]
    for i in range(jumlah_pengirim):
        alamat_penerima = data.iloc[i]['alamat_penerima']
        private_key = data.iloc[i]['private_key']
        alamat_pengirim = data.iloc[i]['alamat_pengirim']

        
        nonce = web3.eth.getTransactionCount(alamat_pengirim)
        
        token_tx = contract.functions.transfer(alamat_penerima, amount).buildTransaction({
            'chainId': 97,
            'gas': 210000,
            'gasPrice': web3.toWei('50', 'gwei'),
            'nonce': nonce
        })
        
        sign_txn = web3.eth.account.signTransaction(token_tx, private_key=private_key)
        
        web3.eth.sendRawTransaction(sign_txn.rawTransaction)
        print(f"Token di Kirim ke Alamat {alamat_penerima}")
        time.sleep(2)

web3 = Web3(Web3.HTTPProvider(config.network))
print(web3.isConnected())

contract = web3.eth.contract(address=config.contract_address, abi=config.abi)
print("Nama Token: " + contract.functions.name().call())

send = input("Masukkan jumlah token yang akan dikirim: ")
amount = web3.toWei(send, 'ether')

# Memanggil fungsi untuk memulai pengiriman token
mulai()
time.sleep(3)
