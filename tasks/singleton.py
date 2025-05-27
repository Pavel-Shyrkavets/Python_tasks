class Singleton:
    single = False

    @staticmethod
    def inst():
        if not Singleton.single:
            Singleton.single = Singleton()

        return Singleton.single
