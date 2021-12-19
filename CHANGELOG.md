### v0.6

- изучена [документация](https://google.github.io/mediapipe/) mediapipe
- изучены примерные [нормы](https://kachestvolife.club/mebel-2/kak-pravilno-sidet-za-stolom-kak-virabotat-pravilnuyu), как надо сидеть за столом
![Нормы](./main/src/photos/optional/sprint6_0.jpg?raw=true "Нормы")

- написан скрипт, считающий углы между туловищем и руками, туловищем и головой и туловищем и ногами: считаем текущий угол, разницу с нужным по модулю, умножаем её на вес (для коррекции), складываем все ошибки, получаем число, которое, если сесть прям идеально, будет равно 0.
![Относительно хорошо](./main/src/photos/optional/sprint6_1.png?raw=true "Относительно хорошо")
![Такое себе](./main/src/photos/optional/sprint6_2.png?raw=true "Такое себе")

Чтобы результаты были лучше качественнее, надо узнать нормативы у профессионалов и задавать допустимый интервал, в который может попадать угол.

### v0.5

В этой итерации по проекту ничего не было готово, т.к. у меня были сильно загруженные 2 недели, а под конец я умудрилась заболеть.

### v0.4
- пройден финал конкурса проектов УМНИК (16 ноября, результаты обещали в начале декабря)
![УМНИК](./main/src/photos/optional/sprint4_0.jpg?raw=true "UMNIK")
- установлена реализация OpenPose ([github](https://github.com/CMU-Perceptual-Computing-Lab/openpose))). Понадобилось больше 12 Гб свободного пространства, чтобы установить все необходимые зависимости и дополнительные приложения, и километр нервов, чтобы это всё запустилось. Выглядит версия вполне прилично, но работает очень медленно: 0.1 FPS - это даже не огорчительно, это неприлично.
![sprint4_1](./main/src/photos/optional/sprint4_1.jpg?raw=true "sprint4_1")
Кадр меняется раз в 10 секунд в лучшем случае: иногда FPS опускается до 0, и тогда требуется до 30-60 секунд, как на камере, так и на видео. 10-секундное видео парсилось час. Это обусловлено тем, что OpenPose написан под CUDA NVidea, а у меня AMD. Приходится пользоваться CPU, но, несмотря на то, что у меня 12 Гб, этого не хватает. С точки зрения производительности моего железа я просто не смогу пользоваться этим вариантом.
- произведено сравнение MediaPipe и OpenPose
![MediaPipe](./main/src/photos/optional/sprint4_2.jpg?raw=true "MediaPipe")
![OpenPose](./main/src/photos/optional/sprint4_3.jpg?raw=true "OpenPose")
Здесь можно видеть, что MediaPipe, как бы он ни был быстрее, хуже показывает изменения осанки, но только за счёт того, что там отсутствует линия, соединяющая плечи и нос. Такое ощущение, что точек, на самом деле, нужно только 5: нос, плечи и 2 точки позвоночника. Остальное, в целом, даже отслеживать не обязательно, но как это сделать - я не знаю.
- были написаны 2 функции, сравнивающие позы между собой: первая считает схожесть по отклонению друг от друга, вторая основана на косинусе угла между нормализованными векторами (метод взят из NLP). В первом случае на фото сравнивались соседние фреймы, во втором - позы из 2 разных видео
![Результаты сравнений](./main/src/photos/optional/sprint4_5.jpg?raw=true "Results")


### v0.3

- было проведено несколько часов бесплодных попыток запуска версии на tensorflow 1.x с прошлого спринта. Не вышло ни у меня, ни у Антона Сергеевича, моего научного руководителя.
- найден рефакторинг предыдущей версии кода с git, адаптированный под tensorflow 2.x ([github](https://github.com/rwightman/posenet-python))).
Плюсы - смогла подключиться к камере. Получилась вот такая красота, и я поняла, что эта версия не подойдёт
![sprint3_1](./main/src/photos/optional/sprint3_1.jpg?raw=true "sprint3_1")
- найдена рабочая версия кода с прошлой версии - тоже на tensorflow 1.x ([github](https://github.com/kr1210/Human-Pose-Compare))
Эта версия была ну очень красиво описана в [статье](https://medium.com/analytics-vidhya/human-pose-comparison-and-action-scoring-using-deep-learning-opencv-python-c2bdf0ddecba), но по факту оказалась жестоким разочарованием.
![Ожидание](./main/src/photos/optional/sprint3_2.png?raw=true "sprint3_2")
![Реальность](./main/src/photos/optional/sprint3_3.png?raw=true "sprint3_3")
Видео для сравнения с эталонным каким-то образом загружается в .pickle-файл, и я не разобралась, как это делается. При попытке запуска с другим видео выдаёт ошибку, без сравнений.
- после поисков сделан вывод, что подходящей готовой реализации не существует

Я решила вернуться к самой первой версии на mediapipe ([paper](./main/other/mediapipe 2006.10204v1.pdf)), которая неожиданно очень хорошо себя показала, и оказалось, что эта библиотека строит 3D-граф, что как раз то, что нужно.

Список изученных статей по Keras и TensorFlow (спойлер: там всё примерно одно и то же, мне особо не помогло):
1. [Краткое введение в тензоры](https://habr.com/ru/post/261563/)
2. [Нежное введение в тензоры для машинного обучения с NumPy](https://www.machinelearningmastery.ru/introduction-to-tensors-for-machine-learning/)
3. [Тензоры в TensorFlow](https://habr.com/ru/post/484214/)
4. [Букварь по TensorFlow и Keras: прошлое (TF1) настоящее (TF2)](https://coderoad.ru/59112527/%D0%91%D1%83%D0%BA%D0%B2%D0%B0%D1%80%D1%8C-%D0%BF%D0%BE-TensorFlow-%D0%B8-Keras-%D0%BF%D1%80%D0%BE%D1%88%D0%BB%D0%BE%D0%B5-TF1-%D0%BD%D0%B0%D1%81%D1%82%D0%BE%D1%8F%D1%89%D0%B5%D0%B5-TF2)
5. [Краткое руководство по TensorFlow 2 для начинающих](https://www.tensorflow.org/tutorials/quickstart/beginner)
6. [Базовая классификация: классифицируйте изображения одежды](https://www.tensorflow.org/tutorials/keras/classification)
7. [Детектор приседаний на OpenCV и Tensorflow](https://habr.com/ru/post/501362/)
8. [Почему TensorFlow 2 намного медленнее, чем TensorFlow 1?](https://qastack.ru/programming/58441514/why-is-tensorflow-2-much-slower-than-tensorflow-1)
9. [Детектирование частей тела с помощью глубоких нейронных сетей](https://habr.com/ru/company/JetBrains-education/blog/354850/)


### v0.2
- прочитана книга "Грокаем Глубокое обучение"
- найдена готовая реализация сравнения точек в OpenCV через библиотеку TensorFlow ([Статья](https://medium.com/analytics-vidhya/human-pose-comparison-and-action-scoring-using-deep-learning-opencv-python-c2bdf0ddecba))
- отсняты и размечены видео (фронтальную съёмку надо переделывать)
![sprint2_down](./main/src/photos/optional/sprint2_down.png?raw=true "sprint2_down")
![sprint2_up](./main/src/photos/optional/sprint2_up.jpg?raw=true "sprint2_up")

### v0.1
- опробованы библиотеки OpenCV и mediapipe на коротких видео
- написан код, размечающий суставы на видео.
![sprint1](./main/src/photos/optional/sprint1.png?raw=true "sprint1")
