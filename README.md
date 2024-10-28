# 113-1 師大科技系資料庫系統  
  > 授課教師：蔡芸琤老師  [老師的github](https://github.com/peculab/Database)
# 基本資料  
  * 姓名：**張育瑞**  
  * 系級：**科技系碩士班四年級**
  * 學號：**61071031H**
# 課程筆記區
2024/9/23  API： ngrok、1.邏輯：read抓creat檔案內容顯示在index中。 修正內容：修改index內容使其符合目標動作，creat改用post指令，所以之前get指令會有問題，需將問題丟給chatgpt修改。 需指向自訂檔案  
2024/9/30  利用app.py串接create.py, read.py, delete.py，但發生循環建立檔案須修正。
ngrok：註冊並下載執行檔，在執行檔終端機中輸入ngrok config add-authtoken <token> 終端機會將token註冊到本機中，接著輸入ngrok http 5000表示在本機中執行、https://c337-140-122-91-108.ngrok-free.app/  
[Mermaid](https://mermaid.d.foundation/) 利用chatgpt建立create.py, read.py, and delete.py並利用flow chart & mermaid建立樹狀圖  
Html模板：live demo  
2024/10/7  利用app.py連結update、delete、create、read，多一個searchID後也要在app.py裡添加，各個py檔指向的資料庫需要一致。如果要在flask框架下放入網頁圖片需建立在static資料夾下面不然會找不到。搜尋結果需要建立一個新的html並在原來的index加入連結，利用searchID進行判斷


# 作業連結區
  1.  [H.W1](https://github.com/TaroRay/DB/tree/main/HW1)  [Video](https://youtube.com/shorts/ufXtbNpw_DQ?feature=share)
HW1 Note：  
1.SQL無法匯入，查詢CHATGPT後可能是TEMP權限問題，但始終無法解決，因此透過助教協助從CHAPTGPT上找尋自行建立後端資料庫的程式碼。  
2.問題2 :程式使用 mysql.connector，而 MySQL sever使用 caching_sha2_password ， 此 mysql.connector 版本中不支援。解決方法：pip install --upgrade mysql-connector-python  更新外掛的版本終於解決
  3.  [H.W2](https://github.com/TaroRay/DB/tree/main/1014_Update%26search_ID)  [Video](https://youtu.be/7EL8gIfzrGc) [MYSQLWorkbench](https://youtu.be/bSnRVC_4QzE)  [ER-diagram](https://github.com/TaroRay/DB/blob/main/ER-Diagram.jpg)
  5.  [H.W3](https://github.com/TaroRay/DB/tree/main/1028_noSQL)[Video](https://youtu.be/C4uuo4k-KIg)  
  6.  [H.W4]
# 專題連結區
