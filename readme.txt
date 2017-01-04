#-----------------------------------------------------------------
# alcohol_c8y.py
# Read the analog sensor value via MCP3002.
# Last udpate: 2016/12/27 by Sho KANEMARU
#-----------------------------------------------------------------
○必要なライブラリをインストール
$ sudo pip install pyyaml

○起動方法
まず、アルコールセンサに搭載されているヒーターをONにする
$ python alcohol-heater.py

続いて、センサによる測定を開始する
$ ./alcohol_c8y.sh
