# GANomaly_Anomaly_Detection
This repo contains the anomaly detection solution for inspecting defects(anomalies) by using GANomaly: Semi-Supervised Anomaly Detection via Adversarial Training [[1]](#reference)  
forked from: https://github.com/samet-akcay/ganomaly [[2]](#reference)  

## 1. GANomaly  
<img width="1172" alt="image" src="https://user-images.githubusercontent.com/30382262/142762483-328a8c66-8e0e-4f9b-a396-5d8228a90faa.png"></img>  

- GANomaly trains only on **Normal data**.
- In inference time, GANomaly re-produces NORMAL image that contains the features of the input image regarless of if the input image is **normal** or **abnormal** sample.

## 2. Losses
<img width="1172" alt="image" src="https://user-images.githubusercontent.com/30382262/142760977-87331ad6-e61f-4287-8934-b477ed0142ae.png"></img>  
- GANomaly is Encoder-Decoder structured GAN which utilize Adversarial, Contextual and Encoder Losses. 
- The **Adversarial Loss** is simmliar with GAN Loss.
- The **Contextual Loss** is pix2pix loss which is used in CycleGAN: Unpaired Image-to-Image Translation using Cycle-Consistent Adversrial Networks [[3]](#reference)
- The **Encoder Loss** was suggested by GANomaly. It is simmilar with the Consistency Loss that is commonly used for Semi-Supervised Learning.  



## 3. Data
<img width="1172" alt="image" src="https://user-images.githubusercontent.com/30382262/142762714-f3dd331f-c716-480c-9a91-911bc7b668bc.png"></img>  

