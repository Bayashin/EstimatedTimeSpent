1. kjlb_StayWatchへssh
2. Docker内のMySQLへアクセス
3. データをファイルとして取得
	```
	SELECT * INTO OUTFILE '/var/lib/mysql-files/log.csv' 
	FROM (
		SELECT 'start_at','end_at' 
		UNION 
		SELECT start_at,end_at,user_id
		FROM app.logs 
		) AAA;
	```
- user_id=1の9月のデータが欲しい場合 
	```
	SELECT * INTO OUTFILE '/var/lib/mysql-files/1_9.csv' 
	FROM (
		SELECT 'start_at','end_at' 
		UNION 
		SELECT start_at,end_at 
		FROM app.logs 
		WHERE start_at >= '2023-9-01 00:00:00' 
			AND start_at <= '2023-9-30 23:59:59' 
			AND user_id = 1
		) AAA;
	```
4. ファイルをコンテナからVMへ移動
```
docker cp "コンテナID":/var/lib/mysql-files/log.csv mysql-files/
```
5. ファイルの所有者と権限の変更
```
chown member mysql-files/log.csv
chmod 750 mysql-files/log.csv
```
6. VMからファイルをコピー
```
scp "ホストネーム":/home/member/mysql-files/lgo.csv "ローカルパス"
```
