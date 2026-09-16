from abc import ABC, abstractmethod
class File(ABC):
    def __init__(self, filename, size_mb):
        self.filename = filename
        self.size_mb = size_mb

    @abstractmethod
    def open(self):
        pass

    @abstractmethod
    def get_file_info(self):
        pass


class TextFile(File):
    def __init__(self, filename, size_mb, word_count):
        super().__init__(filename, size_mb)
        self.word_count = word_count

    def open(self):
        print(f"Открываем текстовый файл '{self.filename}':\n--- Привет, мир! Это содержимое текстового файла. ---")

    def get_file_info(self):
        print(f"[Текст] Имя: {self.filename}, Размер: {self.size_mb} МБ, Количество слов: {self.word_count}")


class ImageFile(File):
    def __init__(self, filename, size_mb, resolution):
        super().__init__(filename, size_mb)
        self.resolution = resolution

    def open(self):
        print(f"Открываем изображение '{self.filename}':")
        print(" /\\_/\\\n( o.o )\n > ^ < ")

    def get_file_info(self):
        print(f"[Изображение] Имя: {self.filename}, Размер: {self.size_mb} МБ, Разрешение: {self.resolution}")


class AudioFile(File):
    def __init__(self, filename, size_mb, duration_sec):
        super().__init__(filename, size_mb)
        self.duration_sec = duration_sec

    def open(self):
        print(f"Воспроизведение аудиофайла '{self.filename}'...")

    def get_file_info(self):
        print(f"[Аудио] Имя: {self.filename}, Размер: {self.size_mb} МБ, Длительность: {self.duration_sec} сек.")


class VideoFile(File):
    def __init__(self, filename, size_mb, duration_sec):
        super().__init__(filename, size_mb)
        self.duration_sec = duration_sec

    def open(self):
        print(f"Воспроизведение видео '{self.filename}' в полноэкранном режиме...")

    def get_file_info(self):
        print(f"[Видео] Имя: {self.filename}, Размер: {self.size_mb} МБ, Длительность: {self.duration_sec} сек.")


class ArchiveFile(File):
    def open(self):
        print("Распаковка архива...")


files = [
    TextFile("notes.txt", 0.1, 150),
    ImageFile("cat.png", 2.5, "1920x1080"),
    AudioFile("song.mp3", 8.3, 210),
    VideoFile("movie.mp4", 1200.0, 5400)
]

print("--- ОБРАБОТКА ФАЙЛОВ В ЦИКЛЕ ---")
for file in files:
    file.open()
    file.get_file_info()
    print("-" * 40)

