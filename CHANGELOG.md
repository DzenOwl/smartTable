### v0.3

- было проведено несколько часов бесплодных попыток запуска версии на tensorflow 1.x с прошлого спринта. Не вышло ни у меня, ни у Антона Сергеевича, моего научного руководителя.
- найден рефакторинг предыдущей версии кода с git, адаптированный под tensorflow 2.x ([github](https://github.com/rwightman/posenet-python))). 
Плюсы - смогла подключиться к камере. Получилась вот такая красота, и я поняла, что эта версия не подойдёт
![sprint3_1](./main/photos/optional/sprint3_1.jpg?raw=true "sprint3_1")
- найдена рабочая версия кода с прошлой версии - тоже на tensorflow 1.x ([github](https://github.com/kr1210/Human-Pose-Compare)) 
Эта версия была ну очень красиво описана в [статье](https://medium.com/analytics-vidhya/human-pose-comparison-and-action-scoring-using-deep-learning-opencv-python-c2bdf0ddecba), но по факту оказалась жестоким разочарованием.
![Ожидание](./main/photos/optional/sprint3_2.png?raw=true "sprint3_2")
![Реальность](./main/photos/optional/sprint3_3.png?raw=true "sprint3_3")
Видео для сравнения с эталонным каким-то образом загружается в .pickle-файл, и я не разобралась, как это делается. При попытке запуска с другим видео выдаёт ошибку, без сравнений.
- после поисков сделан вывод, что подходящей готовой реализации не существует

Я решила вернуться к самой первой версии на mediapipe ([paper](./main/other/mediapipe 2006.10204v1.pdf)), которая неожиданно очень хорошо себя показала, и оказалось, что эта библиотека строит 3D-граф, что как раз то, что нужно.

Список изученных статей по Keras и TensorFlow:
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
![sprint2_down](./main/photos/optional/sprint2_down.png?raw=true "sprint2_down")
![sprint2_up](./main/photos/optional/sprint2_up.jpg?raw=true "sprint2_up")

### v0.1
- опробованы библиотеки OpenCV и mediapipe на коротких видео
- написан код, размечающий суставы на видео.
![sprint1](./main/photos/optional/sprint1.png?raw=true "sprint1")
