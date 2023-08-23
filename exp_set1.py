import streamlit as st
import random
import subprocess
import os
import streamlit as st
from PIL import Image
import json
import pandas as pd


#パート1

tab1, tab2, tab3,tab4= st.tabs(["説明","大問1", "大問2","回答確認と感想"])
with tab1:
	st.markdown("""
	## 実験の説明
	本実験は，音源と図形の関係性を調査するための実験です．
	### 実験の手順
	1. 2つの図形を確認してください．
	2. 2種類の音源を聴取してください．
		- 何回でも聴取可能です．
               - 1つの大問で同じ選択肢を選んでも構いません．
	3. それぞれの音源のイメージと合致する図形を選択し，回答してください．
	1~3の手順で問題を2問回答してもらいます．
	""")

	st.markdown("""
	## システムの操作説明
	### 再生の操作
	1. 再生マークを押します．
	2. 音源が再生されます．
	""")
	uploaded_file = 'sample_sound/G63-76612-3353-36972.wav'
	st.audio(uploaded_file)

with tab2:
	###各種ランダムの設定###
	###音源のランダムの設定###
	audio_files = [
    	{
        	"name": "Chorus",
        	"file_path": 'sample_sound/G63-65601-3313-29473.wav'
    	},
    	{
        	"name": "feDelay",
        	"file_path": 'sample_sound/G63-71512-2212-21983.wav'
    	}
	]
	
	def play_audio(file_path):
		st.audio(file_path)

	def get_selected_audio1():
		if "selected_audio1" not in st.session_state:
			st.session_state.selected_audio1 = random.choice(audio_files)
		return st.session_state.selected_audio1

	def get_selected_audio2():
		if "selected_audio2" not in st.session_state:
			remaining_audio_files = [audio for audio in audio_files if audio != get_selected_audio1()]
			st.session_state.selected_audio2 = random.choice(remaining_audio_files)
		return st.session_state.selected_audio2
	
	selected_audio1 = get_selected_audio1()
	selected_audio2 = get_selected_audio2()
	
	###画像ファイルのリスト###
	###吹き出し画像のランダムの設定###
	image_files = [
    	{
        	"name": "吹き出し1",
        	"file_path": 'speechballoon/e1489_1.jpg'
    	},
    	{
        	"name": "吹き出し2",
        	"file_path": 'speechballoon/double.jpg'
    	}
	]
	
	def get_selected_image1():
		if "selected_image1" not in st.session_state:
			st.session_state.selected_image1 = random.choice(image_files)
		return st.session_state.selected_image1
	
	def get_selected_image2():
		if "selected_image2" not in st.session_state:
			remaining_image_files = [image for image in image_files if image != get_selected_image1()]
			st.session_state.selected_image2 = random.choice(remaining_image_files)
		return st.session_state.selected_image2
		
	random_image1 = get_selected_image1()
	other_images2 = get_selected_image2()

	###ページ内情報###
	##問題提示##
	st.title('Q.それぞれの吹き出しのイメージに合う音源を選んで回答してください')
	
	#ランダムに設定された画像の提示#
	col1, col2 = st.columns(2)
	with col1:
		st.image(random_image1["file_path"], use_column_width=True)

	with col2:
		st.image(other_images2["file_path"], use_column_width=True)
	
	st.write("選択肢")	

	#音源の提示#
	st.write("音源A")
	play_audio(selected_audio1["file_path"])
	st.write("音源B")
	play_audio(selected_audio2["file_path"])
		
	#ラジオボタンの設定	
	answer_a = st.radio("Q1.左の図形と対応する音源を選択してください",("A","B"))
	
	if "answers" not in st.session_state:
		st.session_state.answers_a = {}
	st.session_state.answers_a = answer_a
	
	answer_b = st.radio("Q2.右の図形と対応する音源を選択してください",("A","B"))
	
	if "answers" not in st.session_state:
		st.session_state.answers_b = {}
	st.session_state.answers_b = answer_b
	
with tab3:
	###各種ランダムの設定###
	###音源のランダムの設定###
	audio_files = [
    	{
        	"name": "NoFX",
        	"file_path": 'sample_sound/G63-51301-1111-20698.wav'
    	},
    	{
        	"name": "OverDrive",
        	"file_path": 'sample_sound/G63-62407-4423-40685.wav'
    	}
	]
	
	def play_audio(file_path):
		st.audio(file_path)

	def get_selected_audio3():
		if "selected_audio3" not in st.session_state:
			st.session_state.selected_audio3 = random.choice(audio_files)
		return st.session_state.selected_audio3

	def get_selected_audio4():
		if "selected_audio4" not in st.session_state:
			remaining_audio_files = [audio for audio in audio_files if audio != get_selected_audio3()]
			st.session_state.selected_audio4 = random.choice(remaining_audio_files)
		return st.session_state.selected_audio4
	
	selected_audio3 = get_selected_audio3()
	selected_audio4 = get_selected_audio4()
	
	###画像ファイルのリスト###
	###吹き出し画像のランダムの設定###
	image_files = [
    	{
        	"name": "吹き出し3",
        	"file_path" : 'speechballoon/e1156_1.jpg'
    	},
    	{
        	"name": "吹き出し4",
        	"file_path" :  'speechballoon/e1346_1.jpg'
    	}
	]
	
	def get_selected_image3():
		if "selected_image3" not in st.session_state:
			st.session_state.selected_image3 = random.choice(image_files)
		return st.session_state.selected_image3
	
	def get_selected_image4():
		if "selected_image4" not in st.session_state:
			remaining_image_files = [image for image in image_files if image != get_selected_image3()]
			st.session_state.selected_image4 = random.choice(remaining_image_files)
		return st.session_state.selected_image4
		
	random_image3 = get_selected_image3()
	other_images4 = get_selected_image4()

	###ページ内情報###
	##問題提示##
	st.title('Q.それぞれの吹き出しのイメージに合う音源を選んで回答してください')
	
	#ランダムに設定された画像の提示#
	col1, col2 = st.columns(2)
	with col1:
		st.image(random_image3["file_path"], use_column_width=True)

	with col2:
		st.image(other_images4["file_path"], use_column_width=True)
	
	st.write("選択肢")	

	#音源の提示#
	st.write("音源C")
	play_audio(selected_audio3["file_path"])
	st.write("音源D")
	play_audio(selected_audio4["file_path"])
		
	#ラジオボタンの設定	
	answer_c = st.radio("Q1.左の図形と対応する音源を選択してください",("C","D"))
	
	if "answers" not in st.session_state:
		st.session_state.answers_c = {}
	st.session_state.answers_c = answer_c
	
	answer_d = st.radio("Q2.右の図形と対応する音源を選択してください",("C","D"))
	
	if "answers" not in st.session_state:
		st.session_state.answers_d = {}
	st.session_state.answers_d = answer_d
	
with tab4:
	
	user_id = st.text_input('被験者ID')
	user_feelings = st.text_input('感想')
	
	collected_data = {
		"sound_name":{
			"A":selected_audio1,
			"B":selected_audio2,
			"C":selected_audio3,
			"D":selected_audio4,
		},
		"answer":{
			"1": {
				"name" :st.session_state.answers_a,
				"file_name" :st.session_state.selected_image1["file_path"]
			},
			"2": {
				"name" :st.session_state.answers_b,
				"file_name" :st.session_state.selected_image2["file_path"]
			},
			"3": {
				"name" :st.session_state.answers_c,
				"file_name" :st.session_state.selected_image3["file_path"]
			},
			"4": {
				"name" :st.session_state.answers_d,
				"file_name" :st.session_state.selected_image4["file_path"]
			}
		}
	}
	
	object1_keys = list(collected_data["sound_name"].keys())
	###大問1の解答の整理(画像の種類と解答した音源の種類のセットの生成)###
	if collected_data["answer"]["1"]["name"] == object1_keys[0] and collected_data["answer"]["2"]["name"] == object1_keys[1]:
		answer_set1 = [collected_data["answer"]["1"]["file_name"],collected_data["sound_name"]["A"]["name"]]
		answer_set2 = [collected_data["answer"]["2"]["file_name"],collected_data["sound_name"]["B"]["name"]]
	elif collected_data["answer"]["1"]["name"] == object1_keys[0] and collected_data["answer"]["2"]["name"] == object1_keys[0]:
		answer_set1 = [collected_data["answer"]["1"]["file_name"],collected_data["sound_name"]["A"]["name"]]
		answer_set2 = [collected_data["answer"]["2"]["file_name"],collected_data["sound_name"]["A"]["name"]]		
	elif collected_data["answer"]["1"]["name"] == object1_keys[1] and collected_data["answer"]["2"]["name"] == object1_keys[0]:
		answer_set1= [collected_data["answer"]["1"]["file_name"],collected_data["sound_name"]["B"]["name"]]
		answer_set2 = [collected_data["answer"]["2"]["file_name"],collected_data["sound_name"]["A"]["name"]]
	elif collected_data["answer"]["1"]["name"] == object1_keys[1] and collected_data["answer"]["2"]["name"] == object1_keys[1]:
		answer_set1 = [collected_data["answer"]["1"]["file_name"],collected_data["sound_name"]["B"]["name"]]
		answer_set2 = [collected_data["answer"]["2"]["file_name"],collected_data["sound_name"]["B"]["name"]] 
				
	###大問2の解答の整理(画像の種類と解答した音源の種類のセットの生成)###
	if collected_data["answer"]["3"]["name"] == object1_keys[2] and collected_data["answer"]["4"]["name"] == object1_keys[3]:
		answer_set3 = [collected_data["answer"]["3"]["file_name"],collected_data["sound_name"]["C"]["name"]]
		answer_set4 = [collected_data["answer"]["4"]["file_name"],collected_data["sound_name"]["D"]["name"]]
	elif collected_data["answer"]["3"]["name"] == object1_keys[2] and collected_data["answer"]["4"]["name"] == object1_keys[2]:
		answer_set3= [collected_data["answer"]["3"]["file_name"],collected_data["sound_name"]["C"]["name"]]
		answer_set4 = [collected_data["answer"]["4"]["file_name"],collected_data["sound_name"]["C"]["name"]]
	elif collected_data["answer"]["3"]["name"] == object1_keys[3] and collected_data["answer"]["4"]["name"] == object1_keys[2]:
		answer_set3= [collected_data["answer"]["3"]["file_name"],collected_data["sound_name"]["D"]["name"]]
		answer_set4 = [collected_data["answer"]["4"]["file_name"],collected_data["sound_name"]["C"]["name"]]
	elif collected_data["answer"]["3"]["name"] == object1_keys[3] and collected_data["answer"]["4"]["name"] == object1_keys[3]:
		answer_set3= [collected_data["answer"]["3"]["file_name"],collected_data["sound_name"]["D"]["name"]]
		answer_set4 = [collected_data["answer"]["4"]["file_name"],collected_data["sound_name"]["D"]["name"]]
	
	result = {
		"1" : [answer_set1[0],answer_set1[1]],
		"2" : [answer_set2[0],answer_set2[1]],
		"3" : [answer_set3[0],answer_set3[1]],
		"4" : [answer_set4[0],answer_set4[1]],
		"感想" : [user_feelings,""]
	}
		
	df = pd.DataFrame(result)

	st.markdown("## 回答一覧")
	st.write("大問1_Q1：",st.session_state.answers_a)
	st.image(st.session_state.selected_image1["file_path"],width=100)
	st.write("大問1_Q2：",st.session_state.answers_b)
	st.image(st.session_state.selected_image2["file_path"],width=100)
	st.write("大問2_Q3：",st.session_state.answers_c)
	st.image(st.session_state.selected_image3["file_path"],width=100)
	st.write("大問2_Q4：",st.session_state.answers_d)
	st.image(st.session_state.selected_image4 ["file_path"],width=100)	
	
	if st.button("CSVに変換してダウンロード"):
		csv = df.to_csv(index=False)
		st.download_button(label="Download CSV", data=csv, file_name= user_id + ".csv", mime="text/csv")
	
