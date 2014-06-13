voice_change
============
voice_change是一個語音處理的程式,其主要目的是對頻域訊號進行壓縮或伸展,來改變對應的聲音訊號的音調.
其中包含一個主程式(main.py)和其他三個小的程式(pyaudio_record.py) (spectrum_frep_process.py) (spectrum_freq_scale.py)

pyaudio_record.py
-----------------
pyaudio_record.py主要是用來記錄使用者的聲音
程式中用一些全域變數來設定錄音參數:
以SAMPLING_RATE為採樣頻率,每次讀入一塊有NUM_SAMPLES個採樣的資料區塊,當讀入的採樣資料中有COUNT_NUM個值大於LEVEL時,
將資料儲存到WAV檔案中,一旦開始儲存資料,儲存的資料長度最短為SAVE_LENGTH個區塊.

<br>
![程式碼](./picture/pyaudio_record1.png)
![程式碼](./picture/pyaudio_record2.png)
<br>

spectrum_freq_process.py
------------------------
spectrum_freq_process.py訊號處理

<br>
![訊號處理流程](./picture/spectrum_freq_process1.png)
<br>
