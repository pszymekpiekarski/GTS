import pyautogui
import time



class Element:

    class Image:
        @classmethod
        def isExist(cls, image_path, region=None):
            while True:
                if region:
                    position = pyautogui.locateOnScreen(image_path, region=region, confidence=0.9)
                else:
                    position = pyautogui.locateOnScreen(image_path, confidence=0.9)

                if not position:
                    return True
                else:
                    return False


        @classmethod
        def waitForDisappear(cls, image_path, time_limit=None, region=None):
            if time_limit is None:
                time_limit = float('inf')
            start_time = time.time()
            while True:
                if region:
                    position = pyautogui.locateOnScreen(image_path, region=region, confidence=0.9)
                else:
                    position = pyautogui.locateOnScreen(image_path, confidence=0.9)

                if not position:
                    return round(time.time() - start_time, 2)
                else:
                    if time.time() - start_time > time_limit:
                        return False
                    time.sleep(1)

        @classmethod
        def waitForAppear(cls, image_path, time_limit=None, region=None):
            if time_limit is None:
                time_limit = float('inf')
            start_time = time.time()
            while True:
                if region:
                    position = pyautogui.locateOnScreen(image_path, region=region, confidence=0.9)
                else:
                    position = pyautogui.locateOnScreen(image_path, confidence=0.9)

                if position:
                    return round(time.time() - start_time, 2)
                else:
                    if time.time() - start_time > time_limit:
                        return False
                    time.sleep(1)

        @classmethod
        def focus(cls, image_path, time_limit=None, x=None, y=None, region=None):
            """Czeka aż się pojawi obrazek, przesuwa kursor na środek znalezionego obrazka bez opóźnienia"""

            if time_limit is None or time_limit <= 0:
                time_limit = float('inf')
            start_time = time.time()

            while True:
                try:
                    if region:
                        position_found = pyautogui.locateOnScreen(image_path, region=region, confidence=0.9)
                    else:
                        position_found = pyautogui.locateOnScreen(image_path, confidence=0.9)

                    if position_found:
                        x1, y1, width, height = position_found  # Extract coordinates
                        if x is None and y is None:
                            target_x = x1 + width // 2
                            target_y = y1 + height // 2
                        else:
                            target_x = x1 + x
                            target_y = y1 + y

                        pyautogui.moveTo(target_x, target_y)

                        return round(time.time() - start_time, 2)
                    else:
                        if time.time() - start_time > time_limit:
                            return False
                except Exception as e:
                    print(e)

        @classmethod
        def moveTo(cls, image_path, time_limit=None, duration=2, position='center', region=None, offset=0):
            """Przesuwa kursor na środek znalezionego obrazka w określonym czasie"""
            if time_limit is None or time_limit <= 0:
                time_limit = float('inf')
            start_time = time.time()

            while True:
                try:
                    screenshot = pyautogui.screenshot()

                    if region:
                        position_found = pyautogui.locateOnScreen(image_path, region=region, confidence=0.9)
                    else:
                        position_found = pyautogui.locateOnScreen(image_path, confidence=0.9)
                    if position_found:
                        x, y, width, height = position_found
                        center_x, center_y = x + width / 2, y + height / 2
                        if position == 'center':
                            pyautogui.moveTo(center_x, center_y, duration=duration)
                        elif position == 'left':
                            pyautogui.moveTo(x + offset, center_y, duration=duration)
                        elif position == 'right':
                            pyautogui.moveTo(x + width - offset, center_y, duration=duration)
                        elif position == 'top':
                            pyautogui.moveTo(center_x, y + offset, duration=duration)
                        elif position == 'bottom':
                            pyautogui.moveTo(center_x, y + height - offset, duration=duration)
                        return round(time.time() - start_time, 2)
                    else:
                        if time.time() - start_time > time_limit:
                            return False
                except Exception as e:
                    print(e)

        class Mouse:
            class Left:
                @classmethod
                def click(cls, image_path, time_limit=None):
                    if time_limit is None or time_limit <= 0:
                        time_limit = float('inf')
                    start_time = time.time()
                    while True:
                        try:
                            screenshot = pyautogui.screenshot()
                            position = pyautogui.locateOnScreen(image_path, confidence=0.9)
                            if position:
                                pyautogui.click(position, button='left')
                                return round(time.time() - start_time, 2)
                            else:
                                if time.time() - start_time > time_limit:
                                    return False
                        except Exception as e:
                            print(e)

                @classmethod
                def doubleClick(cls, image_path, time_limit=None):
                    if time_limit is None or time_limit <= 0:
                        time_limit = float('inf')
                    start_time = time.time()
                    while True:
                        try:
                            position = pyautogui.locateOnScreen(image_path, confidence=0.9)
                            print(str(position))
                            if position:
                                pyautogui.doubleClick(position, button='left')
                                return round(time.time() - start_time, 2)
                            else:
                                if time.time() - start_time > time_limit:
                                    return False
                        except Exception as e:
                            print(e)

            class Right:
                @classmethod
                def click(cls, image_path, time_limit=None):
                    if time_limit is None or time_limit <= 0:
                        time_limit = float('inf')
                    start_time = time.time()
                    while True:
                        try:
                            screenshot = pyautogui.screenshot()
                            position = pyautogui.locateOnScreen(image_path, confidence=0.9)
                            if position:
                                pyautogui.click(position, button='right')
                                return round(time.time() - start_time, 2)
                            else:
                                if time.time() - start_time > time_limit:
                                    return False
                        except Exception as e:
                            print(e)

                @classmethod
                def doubleClick(cls, image_path, time_limit=None):
                    if time_limit is None or time_limit <= 0:
                        time_limit = float('inf')
                    start_time = time.time()
                    while True:
                        try:
                            position = pyautogui.locateOnScreen(image_path, confidence=0.9)
                            print(str(position))
                            if position:
                                pyautogui.doubleClick(position, button='right')
                                return round(time.time() - start_time, 2)
                            else:
                                if time.time() - start_time > time_limit:
                                    return False
                        except Exception as e:
                            print(e)


