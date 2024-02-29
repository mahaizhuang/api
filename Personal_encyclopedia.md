<div align=center>

 # 🌍个人百科
 
 ### 🚘问渠那得清如许？为有源头活水来。

</div>

---

<h2 id="1">🌹IT世界</h2>

主要是一些编程语言类的知识，项目，工具等

<h3 id="2">🚘Linux系统性能实时监控工具:netdata</h3>

---

- 项目地址：https://github.com/netdata/netdata
- 推荐理由：一款免费开源的Linux系统性能实时监控工具。它易于安装、占用资源少、功能强大，支持监控多种服务。Netdata可以帮助系统管理员和开发人员实时监测Linux系统的性能和健康状况，提供及时的故障诊断和优化建议。

![network-connections](https://github.com/netdata/netdata/assets/2662304/5f71c102-9146-463e-acba-329094b136a5)

<h3 id="3">🚘动画图解的数据结构与算法教程:hello-algo</h3>

---

- 项目地址：https://github.com/krahets/hello-algo
- 推荐理由：一个动画图解的数据结构与算法教程，支持多种编程语言，如 Java、C++、Python、Go、JS、TS、C#、Swift、Rust、Dart、Zig 等。通过可视化的方式，这个项目帮助学习者更轻松地理解和学习各种数据结构与算法。

![image](https://github.com/mahaizhuang/interesting/assets/43605010/d921a1b9-fdf3-4d07-9236-cc1c658e7373)

<h3 id="4">🚘前端小项目集合:50projects50 天之前</h3>

---

- 项目地址：https://github.com/bradtraversy/50projects50 天之前
- 推荐理由：50 个采用 HTML+CSS+JS 的前端小项目集合。项目包含网页源码和效果展示，标准入门级的前端开源项目。通过查看效果让新手感受前端的美妙，简单的源码降低了上手写代码门槛。

  ![image](https://github.com/mahaizhuang/interesting/assets/43605010/499a0e78-e4a3-456f-81a9-caed23d70c55)

<h3 id="5">🚘程序员的瑞士军刀:DevToys</h3>

---

- 项目地址：https://github.com/veler/DevToys
- 推荐理由：程序员的瑞士军刀，打包了各种日常开发中可能会用到的小工具。它包括时间戳转化、各种解码工具、输出美化工具、颜色选择器等实用功能。DevToys 的用户界面友好且功能强大，使程序员能够更高效地完成常见的开发任务。

---

<h2 id="6">🌹图像处理类</h2>

主要是一些AI处理工具

<h3 id="7">🚘图像生成软件:Fooocus</h3>

---

- 项目地址：https://github.com/lllyasviel/Fooocus
- 推荐理由：一个图像生成软件，基于Gradio开发。它不仅包含了内部优化和质量改进，还允许用户通过人机交互来探索和创造新的图像。Fooocus让用户不必担心复杂的技术参数，只需享受创造性的过程，拓展人类的想象力。这个项目适用于那些对图像生成和艺术创作感兴趣的人。

![image](https://github.com/mahaizhuang/interesting/assets/43605010/208475fd-5284-456b-90db-ae480c35aa04)

<h3 id="8">🚘下一代换脸器和增强器:facefusion</h3>

---

- 项目地址：https://github.com/facefusion/facefusion
- 推荐理由：一个下一代换脸器和图像增强器。它使用先进的图像处理技术，允许用户将不同的面部特征融合在一起，创造有趣和令人印象深刻的效果。这个项目的潜在应用包括娱乐、虚拟化妆和艺术创作，为用户提供了创造性的工具。

Then run

```python
python run.py [options]

options:
  -h, --help                                                                                                             show this help message and exit
  -s SOURCE_PATHS, --source SOURCE_PATHS                                                                                 choose single or multiple source images or audios
  -t TARGET_PATH, --target TARGET_PATH                                                                                   choose single target image or video
  -o OUTPUT_PATH, --output OUTPUT_PATH                                                                                   specify the output file or directory
  -v, --version                                                                                                          show program's version number and exit

misc:
  --skip-download                                                                                                        omit automate downloads and remote lookups
  --headless                                                                                                             run the program without a user interface
  --log-level {error,warn,info,debug}                                                                                    adjust the message severity displayed in the terminal

execution:
  --execution-providers EXECUTION_PROVIDERS [EXECUTION_PROVIDERS ...]                                                    accelerate the model inference using different providers (choices: cpu, ...)
  --execution-thread-count [1-128]                                                                                       specify the amount of parallel threads while processing
  --execution-queue-count [1-32]                                                                                         specify the amount of frames each thread is processing

memory:
  --video-memory-strategy {strict,moderate,tolerant}                                                                     balance fast frame processing and low vram usage
  --system-memory-limit [0-128]                                                                                          limit the available ram that can be used while processing

face analyser:
  --face-analyser-order {left-right,right-left,top-bottom,bottom-top,small-large,large-small,best-worst,worst-best}      specify the order in which the face analyser detects faces.
  --face-analyser-age {child,teen,adult,senior}                                                                          filter the detected faces based on their age
  --face-analyser-gender {female,male}                                                                                   filter the detected faces based on their gender
  --face-detector-model {retinaface,yoloface,yunet}                                                                      choose the model responsible for detecting the face
  --face-detector-size FACE_DETECTOR_SIZE                                                                                specify the size of the frame provided to the face detector
  --face-detector-score [0.0-1.0]                                                                                        filter the detected faces base on the confidence score

face selector:
  --face-selector-mode {reference,one,many}                                                                              use reference based tracking with simple matching
  --reference-face-position REFERENCE_FACE_POSITION                                                                      specify the position used to create the reference face
  --reference-face-distance [0.0-1.5]                                                                                    specify the desired similarity between the reference face and target face
  --reference-frame-number REFERENCE_FRAME_NUMBER                                                                        specify the frame used to create the reference face

face mask:
  --face-mask-types FACE_MASK_TYPES [FACE_MASK_TYPES ...]                                                                mix and match different face mask types (choices: box, occlusion, region)
  --face-mask-blur [0.0-1.0]                                                                                             specify the degree of blur applied the box mask
  --face-mask-padding FACE_MASK_PADDING [FACE_MASK_PADDING ...]                                                          apply top, right, bottom and left padding to the box mask
  --face-mask-regions FACE_MASK_REGIONS [FACE_MASK_REGIONS ...]                                                          choose the facial features used for the region mask (choices: skin, left-eyebrow, right-eyebrow, left-eye, right-eye, eye-glasses, nose, mouth, upper-lip, lower-lip)

frame extraction:
  --trim-frame-start TRIM_FRAME_START                                                                                    specify the the start frame of the target video
  --trim-frame-end TRIM_FRAME_END                                                                                        specify the the end frame of the target video
  --temp-frame-format {bmp,jpg,png}                                                                                      specify the temporary resources format
  --temp-frame-quality [0-100]                                                                                           specify the temporary resources quality
  --keep-temp                                                                                                            keep the temporary resources after processing

output creation:
  --output-image-quality [0-100]                                                                                         specify the image quality which translates to the compression factor
  --output-video-encoder {libx264,libx265,libvpx-vp9,h264_nvenc,hevc_nvenc}                                              specify the encoder use for the video compression
  --output-video-preset {ultrafast,superfast,veryfast,faster,fast,medium,slow,slower,veryslow}                           balance fast video processing and video file size
  --output-video-quality [0-100]                                                                                         specify the video quality which translates to the compression factor
  --output-video-resolution OUTPUT_VIDEO_RESOLUTION                                                                      specify the video output resolution based on the target video
  --output-video-fps OUTPUT_VIDEO_FPS                                                                                    specify the video output fps based on the target video
  --skip-audio                                                                                                           omit the audio from the target video

frame processors:
  --frame-processors FRAME_PROCESSORS [FRAME_PROCESSORS ...]                                                             load a single or multiple frame processors. (choices: face_debugger, face_enhancer, face_swapper, frame_enhancer, lip_syncer, ...)
  --face-debugger-items FACE_DEBUGGER_ITEMS [FACE_DEBUGGER_ITEMS ...]                                                    load a single or multiple frame processors (choices: bounding-box, landmark-5, landmark-68, face-mask, score, age, gender)
  --face-enhancer-model {codeformer,gfpgan_1.2,gfpgan_1.3,gfpgan_1.4,gpen_bfr_256,gpen_bfr_512,restoreformer_plus_plus}  choose the model responsible for enhancing the face
  --face-enhancer-blend [0-100]                                                                                          blend the enhanced into the previous face
  --face-swapper-model {blendswap_256,inswapper_128,inswapper_128_fp16,simswap_256,simswap_512_unofficial,uniface_256}   choose the model responsible for swapping the face
  --frame-enhancer-model {real_esrgan_x2plus,real_esrgan_x4plus,real_esrnet_x4plus}                                      choose the model responsible for enhancing the frame
  --frame-enhancer-blend [0-100]                                                                                         blend the enhanced into the previous frame
  --lip-syncer-model {wav2lip_gan}                                                                                       choose the model responsible for syncing the lips

uis:
  --ui-layouts UI_LAYOUTS [UI_LAYOUTS ...]                                                                               launch a single or multiple UI layouts (choices: benchmark, default, webcam, ...)
```

<h3 id="9">🚘3D高斯飞溅实时辐射场渲染:gaussian-splatting</h3>

---

- 项目地址：https://github.com/graphdeco-inria/gaussian-splatting
- 推荐理由：一个用于3D实时辐射场渲染的项目。它利用高斯飞溅技术来实现高质量的辐射场渲染，适用于图形渲染和可视化领域。这个项目为研究和应用实时渲染的开发者提供了有价值的工具和资源。

Then run

```python
python convert.py -s <location> --skip_matching [--resize] #If not resizing, ImageMagick is not needed
```
