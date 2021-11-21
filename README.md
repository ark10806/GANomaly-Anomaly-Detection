# GANomaly-Anomaly Detection
This repo contains the anomaly detection solution for inspecting defects(anomalies) by using GANomaly: Semi-Supervised Anomaly Detection via Adversarial Training [[1]](#reference)  
forked from https://github.com/samet-akcay/ganomaly [[2]](#reference)  

## 1. Model  
<img width="1172" alt="image" src="https://user-images.githubusercontent.com/30382262/142762483-328a8c66-8e0e-4f9b-a396-5d8228a90faa.png"></img>  

- GANomaly trains only on **Normal data**.
- In inference time, GANomaly re-produces NORMAL image that contains the features of the input image regarless of if the input image is **normal** or **abnormal** sample.

## 2. Losses
<img width="1024" alt="image" src="https://user-images.githubusercontent.com/30382262/142760977-87331ad6-e61f-4287-8934-b477ed0142ae.png"></img>  
- GANomaly is Encoder-Decoder structured GAN which utilize Adversarial, Contextual and Encoder Losses. 
- The **Adversarial Loss** is simmliar with GAN Loss.
- The **Contextual Loss** is pix2pix loss which is used in CycleGAN: Unpaired Image-to-Image Translation using Cycle-Consistent Adversrial Networks [[3]](#reference)
- The **Encoder Loss** was suggested by GANomaly. It is simmilar with the Consistency Loss that is commonly used for Semi-Supervised Learning.  



## 3. Dataset
<img width="1172" alt="image" src="https://user-images.githubusercontent.com/30382262/142765302-86d336cb-febf-4db4-91a4-da0dc327e753.png"></img>
- The valve seat is a part located in an internal combustion engine and is used to control the flow of fuel.  </br></br>  

<img width="876" alt="image" src="https://user-images.githubusercontent.com/30382262/142768214-c88bf19f-ab60-488e-adda-17155e3749be.png"></img>
- The examples of an anomaly on valve seat are the image corresponding to the red labels.
- Our tasks are **localizing** and **classifying** anomalies.

## 4. Results
<img width="1172" alt="image" src="https://user-images.githubusercontent.com/30382262/142768325-20fc3ca0-0693-4a7f-839f-f868f6e8ccfa.png"></img>

| GT \ PRED   |  normal  |    anomaly   |
|-------------|----------|--------------|
| normal      |    131   |      19      |
| anomaly     |     20   |     606      |  

F1-SCORE on classification: 0.96 


## 4. References
[1]  Akcay S., Atapour-Abarghouei A., Breckon T.P. (2019) GANomaly: Semi-supervised Anomaly Detection via Adversarial Training. In: Jawahar C., Li H., Mori G., Schindler K. (eds) Computer Vision – ACCV 2018. ACCV 2018. Lecture Notes in Computer Science, vol 11363. Springer, Cham  
[2]  https://github.com/samet-akcay/ganomaly  
[3]  Jun-Yan Zhu*, Taesung Park*, Phillip Isola, and Alexei A. Efros. "Unpaired Image-to-Image Translation using Cycle-Consistent Adversarial Networks", in IEEE International Conference on Computer Vision (ICCV), 2017. 
