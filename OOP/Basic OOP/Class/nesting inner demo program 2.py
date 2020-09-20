class human:
    class head:
        def talk(self):
            print('we can talking..')

        class brain:
            def think(self):
                print('We can think')


h = human()
hd = h.head()
hd.talk()
b = hd.brain()
b.think()
