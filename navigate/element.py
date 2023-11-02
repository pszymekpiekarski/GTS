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
        def moveTo(cls, image_path, time_limit=None, duration=0.5, x=None, y=None, region=None):
            """Przesuwa kursor na środek znalezionego obrazka w określonym czasie"""

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

                        pyautogui.moveTo(target_x, target_y, duration=duration)


                        return round(time.time() - start_time, 2)
                    else:
                        if time.time() - start_time > time_limit:
                            return False
                except Exception as e:
                    print(e)

        class Mouse:
            class Left:
                @classmethod
                def click(cls, image_path, time_limit=None, x=None, y=None, region=None):
                    if time_limit is None or time_limit <= 0:
                        time_limit = float('inf')
                    start_time = time.time()

                    while True:
                        try:
                            if region:
                                position = pyautogui.locateOnScreen(image_path, region=region, confidence=0.9)
                            else:
                                position = pyautogui.locateOnScreen(image_path, confidence=0.9)

                            if position:
                                x1, y1, width, height = position  # Extract coordinates
                                target_x = x1 + (x if x is not None else width // 2)
                                target_y = y1 + (y if y is not None else height // 2)

                                pyautogui.click(target_x, target_y, button='left')
                                return round(time.time() - start_time, 2)
                            else:
                                if time.time() - start_time > time_limit:
                                    return False
                        except Exception as e:
                            print(e)

                @classmethod
                def doubleClick(cls, image_path, time_limit=None, x=None, y=None, region=None):
                    if time_limit is None or time_limit <= 0:
                        time_limit = float('inf')
                    start_time = time.time()

                    while True:
                        try:
                            if region:
                                position = pyautogui.locateOnScreen(image_path, region=region, confidence=0.9)
                            else:
                                position = pyautogui.locateOnScreen(image_path, confidence=0.9)

                            if position:
                                x1, y1, width, height = position  # Extract coordinates
                                target_x = x1 + (x if x is not None else width // 2)
                                target_y = y1 + (y if y is not None else height // 2)

                                pyautogui.doubleClick(target_x, target_y, button='left')
                                return round(time.time() - start_time, 2)
                            else:
                                if time.time() - start_time > time_limit:
                                    return False
                        except Exception as e:
                            print(e)

            class Right:
                @classmethod
                def click(cls, image_path, time_limit=None, x=None, y=None, region=None):
                    if time_limit is None or time_limit <= 0:
                        time_limit = float('inf')
                    start_time = time.time()

                    while True:
                        try:
                            if region:
                                position = pyautogui.locateOnScreen(image_path, region=region, confidence=0.9)
                            else:
                                position = pyautogui.locateOnScreen(image_path, confidence=0.9)

                            if position:
                                x1, y1, width, height = position  # Extract coordinates
                                target_x = x1 + (x if x is not None else width // 2)
                                target_y = y1 + (y if y is not None else height // 2)

                                pyautogui.click(target_x, target_y, button='right')
                                return round(time.time() - start_time, 2)
                            else:
                                if time.time() - start_time > time_limit:
                                    return False
                        except Exception as e:
                            print(e)

                @classmethod
                def doubleClick(cls, image_path, time_limit=None, x=None, y=None, region=None):
                    if time_limit is None or time_limit <= 0:
                        time_limit = float('inf')
                    start_time = time.time()

                    while True:
                        try:
                            if region:
                                position = pyautogui.locateOnScreen(image_path, region=region, confidence=0.9)
                            else:
                                position = pyautogui.locateOnScreen(image_path, confidence=0.9)

                            if position:
                                x1, y1, width, height = position  # Extract coordinates
                                target_x = x1 + (x if x is not None else width // 2)
                                target_y = y1 + (y if y is not None else height // 2)

                                pyautogui.doubleClick(target_x, target_y, button='right')
                                return round(time.time() - start_time, 2)
                            else:
                                if time.time() - start_time > time_limit:
                                    return False
                        except Exception as e:
                            print(e)
