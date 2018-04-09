# SwitchCryptoCoinMining

しばらく使いながら修正していましたが、採掘単価が下がったため公開。

■修正していない部分(メモ)
・マイニングプールのフェイルオーバー出来るようにする。
　⇒割とサーバ側が死んでいることがある。
・マイニングする通貨の対象・対象外を簡単に変更出来るようにコードの修正
　⇒ある程度の量をマイニングしてからウォレットに送金しないと、手数料の割合が
　　大きくなり効率が下がる。
・マイニングソフトのバージョンアップでハッシュレートが上がったりするので
　スクレイピング対象のURLの変更を簡単できるようにする。


■iniの内容
[CryptoCoinMining]
LogDir:効率の良い仮想通貨を取得した履歴ログを保存するフォルダ

[Miner]
xxxxDirectory:マイニングソフトのディレクトリ
cmdxxx:各仮想通貨のマイニング実行コマンド(コマンドは各マイニングソフトのHelpを参照のこと)
