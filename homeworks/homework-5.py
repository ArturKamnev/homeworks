class Streamer:
    def live(self):
        return "Запускаю стрим! Подписывайтесь, ставьте лайки!"

    def earn(self):
        return "Заработал 500 донатов за 2 часа"


class TikToker:
    def live(self):
        return "Снимаю трендовый тикток под песню месяца!"

    def viral(self):
        return "Набрал 3 миллиона просмотров за сутки!"


class Mutant:
    def live(self):
        return "Я... я свечусь в темноте... это мой вайб..."

    def superpower(self):
        return "Летаю и стреляю лазерами из глаз"


class GlowStreamer(Streamer, Mutant):
    def ultimate_content(self):
        return f"{self.live()} \n{self.earn()} \n{self.superpower()}"

class ViralCyborg(TikToker, Mutant):
    def ultimate_content(self):
        return f"{self.live()} \n {self.viral()} \n {self.superpower()}"

class DonateMage(Streamer, TikToker):
    def ultimate_content(self):
        return (f"{self.live()} \n {self.earn()} \n {self.viral()}")


streamer = GlowStreamer()
cyborg = ViralCyborg()
mage = DonateMage()

print(GlowStreamer.mro())
print(ViralCyborg.mro())
print(DonateMage.mro())


print(mage.live()) # Сработает метод .live() у род класса Streamer т. к. в классе маге нет этого метода и он берет из первого род класса
print(cybord.live()) # Сработает метод .live() у род класса TikToker т. к. в классе киборг нет этого метода и он берет из первого род класса
print(streamer.live()) # Сработает метод .live() у класса Streamer так как первый идет класс GlowStreamer но у него этого метода нет и он переходит в первый указанный родительнский класс