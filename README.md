# STT and TTS report
语音识别语音合成模型调研

STT:speech to text语音识别
TTS:speech to text语音合成

## 1.付费大模型

这几个大模型使用方法：付费获得对应的STT,TTS API key,相当于把数据上传到服务器后返回结果。
- [Google Cloud](https://cloud.google.com/speech-to-text?utm_source=google&utm_medium=cpc&utm_campaign=na-US-all-en-dr-bkws-all-all-trial-e-dr-1605212&utm_content=text-ad-none-any-DEV_c-CRE_553443483826-ADGP_Desk%20%7C%20BKWS%20-%20EXA%20%7C%20Txt%20_%20AI%20%26%20ML%20_%20Speech-to-Text_Speech%20to%20Text_General-KWID_43700076157305329-aud-1436107373922%3Akwd-21425535976&utm_term=KW_google%20speech%20to%20text-ST_google%20speech%20to%20text&gclid=Cj0KCQjw0tKiBhC6ARIsAAOXutmHOklLcF_1b7lCO53k4_IYUXv9TbM1F6h5NLa6TiFT6N4BljJL0A4aAvxZEALw_wcB&gclsrc=aw.ds)

   Google Cloud Speech-to-Text（STT）：Google提供了一个强大的、基于云的语音识别服务，可以识别多种语言和方言。它可以实时转录长时间的语音，并提供了一些高级功能，如自动标点和语音自适应。

   Google Cloud Text-to-Speech（TTS）：Google的Text-to-Speech API基于谷歌的WaveNet技术，可以生成自然、真实的语音。它支持多种语言、语音和自定义发音。您还可以调整语速、音高和音量增益。

- [Microsoft Azure](https://azure.microsoft.com/en-us/products/cognitive-services/speech-to-text)

  Microsoft Azure Speech Service：微软的Azure Speech Service包括了一个语音识别服务，支持多种语言和场景。它提供实时和批量转录功能，还可以适应不同的领域词汇和说话风格。

  Microsoft Azure Text to Speech：微软的Text to Speech服务使用神经网络生成自然 sounding 语音。它支持多种语言和语音，还可以创建定制的语音。您可以调整语速、音高和发音。
  
- [IBM watson](https://www.ibm.com/cloud/watson-text-to-speech)

  IBM Watson Speech to Text（STT）：IBM Watson提供了一个语音识别服务，可以识别多种语言和说话风格。它支持实时和批量转录，还可以适应特定领域的词汇和短语。

  IBM Watson Text to Speech（TTS）：IBM Watson的Text to Speech服务可以将文本转换为自然 sounding 语音。它支持多种语言和语音，并提供了一些高级功能，如表情控制和定制发音。

## 2.开源大模型
  
使用方法：
  - 加载预训练模型和对应tokenizer
  - 读取音频文件
  - 分析音频文件获得文字记录

模型如下：  
  - Wav2Vec2（STT）：Wav2Vec2 是 Facebook AI 提供的一种语音识别模型，在Hugging Face Transformers库中提供了预训练的 Wav2Vec2 模型。支持多语言。GitHub 仓库：https://huggingface.co/docs/transformers/model_doc/wav2vec2
  
  - Mozilla TTS（TTS）：Mozilla TTS 是一个开源的 TTS 引擎，提供了预训练的 Tacotron2 和 FastSpeech2 等模型。它支持多种语言，中文支持较好，并允许自定义语音。GitHub 仓库：https://github.com/mozilla/TTS

  - Mozilla DeepSpeech（STT）：DeepSpeech 是一个由 Mozilla 开发的开源语音识别引擎，基于 Baidu 的 Deep Speech 研究。DeepSpeech 提供了预训练的模型，支持多种语言，中文支持较好。GitHub 仓库：https://github.com/mozilla/DeepSpeech

  - chinese_speech_pretrain(STT): 针对中文语音转文字的预训练模型。1 万小时中文数据作为无监督预训练数据。数据主要来源于 YouTube 和 Podcast，覆盖了各种类型录制场景、背景噪声、说话方式等，其领域主要包括有声书、解说、纪录片、电视剧、访谈、新闻、朗读、演讲、综艺和其他等10大场景。Github 仓库：https://github.com/TencentGameMate/chinese_speech_pretrain

  - HuBERT (STT): 一个用于语音识别的深度学习自监督模型。它是 Facebook AI 的一个项目，旨在创建一个通用的预训练语音表示模型。HuBERT 的目标是学习音频信号中的丰富表示，以便在下游任务中表现良好。代码仓库：https://huggingface.co/docs/transformers/model_doc/hubert
  
  - Open AI Whisper(STT): Whisper 是 OpenAI 开发的一种自动语音识别（ASR）系统。Whisper ASR 是一个深度学习模型，旨在将声音转换为文字。它被训练用于多种应用，如语音识别、语音翻译、语音助手等。Whisper 模型的一个关键特点是它能够在各种语言和领域中表现良好，这得益于其在大量多语言数据上进行的预训练。官网链接：https://openai.com/research/whisper

## 3.模型实例
part1. 语音转文字：
使用方法：

- 首先安装transformers,jiwer库用于计算词错误率WER和字错误率CER，librosa库用于音频导入
- 选择已微调好的模型，推荐wbbbbb/wav2vec2-large-chinese-zh-cn，其CER大概在12.30%左右
- 选择语音文件，该模型只允许以16kHz采样的wav格式文件
- 运行程序即可得到语音识别的音频文字
- 若要计算WER,CER等，需要提供ground_truth为正确音频文字

这里给出所用的音频文件及翻译ground_truth在main目录下。

代码链接：[STT.ipynb](STT.ipynb)

