# STT and TTS report
语音识别与语音合成模型调研

STT(Speech to Text): 语音识别

TTS(Speech to Text): 语音合成
## 1.评价标准
在评估语音转文字（STT）模型的性能时，去除标点符号是一种常见的做法，尤其是当模型的主要目标是识别语音中的单词或字符时。去除标点符号可以帮助消除标点在评估指标（如 CER）中的影响，从而使得评估结果更加集中于单词或字符的识别准确性。因此，评估中将给出去除标点符号前后的字符错误率与准确率。计算CER与Accuracy的代码为：[cer_accuracy.py](code/cer_accuracy.py)

在中文语音识别任务中，因为中文的最小单位是字符而非单词，所以相较准确率和词错误率，字符错误率能够更好地评估STT任务质量。
### 字符错误率CER(character error rate)
字符错误率是评估模型在字符级别的错误识别表现。它主要通过计算插入、删除和替换字符的数量，并将其与参考文本中字符的总数进行比较。CER 越低，表示模型的性能越好。CER 的计算公式为：
CER = (插入 + 删除 + 替换) / 参考文本字符数

CER 的值范围从 0 到 1，0 表示完美的识别，1 表示识别结果与参考完全不同。
### 准确率Accuracy
准确率是用于衡量分类任务性能的一个指标，它表示正确预测的样本数量占总样本数量的比例。准确率越高，表示模型的性能越好。准确率的计算公式为：
Accuracy = (正确预测的样本数量) / (总样本数量)

准确率的值范围从 0 到 1，1 表示模型完美地预测了所有样本，而 0 表示模型没有正确预测任何样本。

## 2.模型介绍
### 调用API接口的付费模型
使用方法：付费获得对应的STT,TTS API key,相当于把数据上传到服务器后返回结果。
- Google Cloud

   [Google Cloud Speech-to-Text（STT）](https://console.cloud.google.com/speech/overview?hl=zh-cn&project=enduring-sweep-386203)：Google提供了一个强大的、基于云的语音识别服务，可以识别多种语言和方言。它可以实时转录长时间的语音，并提供了一些高级功能，如自动标点和语音自适应。在P290_convert.wav上测验结果如下：
Accuracy: 0.26,
Accuracy without punctuation: 0.58,
CER: 0.14,
CER without punctuation: 0.08.

   [Google Cloud Text-to-Speech（TTS）](https://console.cloud.google.com/marketplace/product/google/texttospeech.googleapis.com?hl=zh-cn&project=enduring-sweep-386203&returnUrl=%2Fspeech%2Ftext-to-speech%3Fhl%3Dzh-cn%26project%3Denduring-sweep-386203)：Google的Text-to-Speech API基于谷歌的WaveNet技术，可以生成自然、真实的语音。它支持多种语言、语音和自定义发音。您还可以调整语速、音高和音量增益。

- [Baidu](https://ai.baidu.com/ai-doc/SPEECH/Tl9mh38eu)

    百度提供了短文本，长文本以及离线语音识别和合成功能，并且有10个语音可供选择。

- 腾讯云[语音识别](https://cloud.tencent.com/document/product/1093)和[语音合成](https://cloud.tencent.com/product/tts)模型

    腾讯云提供了高识别准确率的语音识别服务和高拟真度、灵活配置的语音合成产品。

### 调用开源模型
  
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
  
  - Open AI Whisper(STT): Whisper 是 OpenAI 开发的一种自动语音识别（ASR）系统。Whisper ASR 是一个深度学习模型，旨在将声音转换为文字。它被训练用于多种应用，如语音识别、语音翻译、语音助手等。Whisper 模型的一个关键特点是它能够在各种语言和领域中表现良好，这得益于其在大量多语言数据上进行的预训练。GitHub上给出了Whisper在中文文本上的平均词错误率(WER)达到了14.7%。官网链接：https://openai.com/research/whisper

## 3.模型实例
Part1. 语音转文字(STT)：

### 使用方法：

- 首先安装transformers,jiwer库用于计算词错误率WER和字错误率CER，librosa库用于音频导入
- 选择已微调好的模型，推荐wbbbbb/wav2vec2-large-chinese-zh-cn，去掉标点符号后其CER大概在7.0%左右
- 选择语音文件，该模型只允许以16kHz采样的wav格式文件
- 运行程序即可得到语音识别的音频文字
- 若要计算WER,CER, Accuracy等，需要提供ground_truth为正确音频文字

这里给出所用的音频文件分别为P279_convert.wav,P28_convert.wav和P290_convert.wav，以及翻译ground_truth文件ground_truth_3voice.docx在main目录下。

代码链接：[STT.ipynb](code/STT.ipynb)

不同模型的准确率及字符错误率为：

CER without punctuation：去除标点符号后的字符错误率，

Accuracy without punctuation：去除标点符号后的准确率

![model_comparison.JPG](model_comparison.JPG)

Part2. 文字转语音(TTS):

- bark模型：需要GPU加速，代码如下：[TTS_bark.ipynb](code/TTS_bark.ipynb)

- 使用hugging face上已有的训练好的语音合成模型，生成的语音见[audioP290.wav](voice/audioP290.wav)，模型仓库链接：https://huggingface.co/spaces/chenmgtea/cn_tts

- 调用百度API, 填写好信息之后运行即可，代码如下：[TTS_baidu.ipynb](code/TTS_baidu.ipynb)，申请百度API链接：https://ai.baidu.com/



