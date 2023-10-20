# mouse.py
import pyautogui

class Mouse():
    @classmethod
    def move(cls, x=None, y=None, duration=None):
        '''
        przesuwa kursor myszy o określoną liczbę pikseli względem aktualnej pozycji. Przyjmuje ona dwa argumenty: x i y, oznaczające odpowiednio liczbę pikseli, o jaką ma zostać przesunięty kursor w poziomie i pionie.
        :param x:
        :param y:
        :param duration:
        :return:
        '''
        if x is not None and y is not None:
            if duration:
                pyautogui.move(x, y, duration)
            else:
                pyautogui.move(x, y)
        else:
            raise ValueError("Both x and y coordinates must be provided")

    @classmethod
    def moveTo(cls, x=None, y=None, duration=None):
        '''
        przesuwa kursor myszy do podanej pozycji
        :param x:
        :param y:
        :param duration:
        :return:
        '''
        if x is not None and y is not None:
            if duration:
                pyautogui.moveTo(x, y, duration)
            else:
                pyautogui.moveTo(x, y)
        else:
            raise ValueError("Both x and y coordinates must be provided")

        class Left():
            pass

    class Left:
        @classmethod
        def down(cls, x=None, y=None):
            if x is not None and y is not None:
                pyautogui.mouseDown(x=x, y=y, button='left')
            else:
                pyautogui.mouseDown(button='left')

        @classmethod
        def up(cls, x=None, y=None):
            if x is not None and y is not None:
                pyautogui.mouseUp(x=x, y=y, button='left')
            else:
                pyautogui.mouseUp(button='left')

        @classmethod
        def click(cls, x=None, y=None):
            if x is not None and y is not None:
                pyautogui.click(x=x, y=y, button='left')
            else:
                pyautogui.click(button='left')

        @classmethod
        def doubleClick(cls, x=None, y=None):
            if x is not None and y is not None:
                pyautogui.doubleClick(x=x, y=y, button='left')
            else:
                pyautogui.doubleClick(button='left')

        @classmethod
        def dragTo(cls, x=None, y=None):
            if x is not None and y is not None:
                pyautogui.dragTo(x, y, 1, button='left')
            else:
                pass

    class Right:
        @classmethod
        def down(cls, x=None, y=None):
            if x is not None and y is not None:
                pyautogui.mouseDown(x=x, y=y, button='right')
            else:
                pyautogui.mouseDown(button='right')

        @classmethod
        def up(cls, x=None, y=None):
            if x is not None and y is not None:
                pyautogui.mouseUp(x=x, y=y, button='right')
            else:
                pyautogui.mouseUp(button='right')

        @classmethod
        def click(cls, x=None, y=None):
            if x is not None and y is not None:
                pyautogui.click(x=x, y=y, button='right')
            else:
                pyautogui.click(button='right')

        @classmethod
        def doubleClick(cls, x=None, y=None):
            if x is not None and y is not None:
                pyautogui.doubleClick(x=x, y=y, button='right')
            else:
                pyautogui.doubleClick(button='right')

        @classmethod
        def dragTo(cls, x=None, y=None):
            if x is not None and y is not None:
                pyautogui.dragTo(x, y, 1, button='right')
            else:
                pass

    class Scroll:
        def up(self, units):
            pyautogui.scroll(units)

        def down(self, units):
            pyautogui.scroll(-units)
